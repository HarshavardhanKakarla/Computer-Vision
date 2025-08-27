import os
import cv2
import PIL
import numpy as np
import google.generativeai as genai
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from mediapipe.python.solutions import hands, drawing_utils
from warnings import filterwarnings

filterwarnings(action='ignore')

class calculator:

    def streamlit_config(self):
        st.set_page_config(page_title='Calculator', layout="wide")
        page_background_color = """
        <style>
        [data-testid="stHeader"] { background: rgba(75,75,75,0); }
        .block-container { padding-top: 0rem; }
        </style>
        """
        st.markdown(page_background_color, unsafe_allow_html=True)
        st.markdown(f'<h1 style="text-align: center;">Virtual Calculator and Canva</h1>', unsafe_allow_html=True)
        add_vertical_space(1)

    def __init__(self):
        # API Key fetching mechanism, supporting both local (.env) and Streamlit Secrets
        api_key = None
        if "GOOGLE_API_KEY" in st.secrets:
            api_key = st.secrets["GOOGLE_API_KEY"]
        else:
            try:
                from dotenv import load_dotenv
                load_dotenv()
                api_key = os.environ.get('GOOGLE_API_KEY')
            except Exception:
                api_key = None
        if not api_key:
            st.error("GOOGLE_API_KEY not found in Streamlit secrets or .env file! Set it up securely before running.")
        self.api_key = api_key

        # Webcam and imaging setup
        self.cap = cv2.VideoCapture(0)
        self.cap.set(propId=cv2.CAP_PROP_FRAME_WIDTH, value=950)
        self.cap.set(propId=cv2.CAP_PROP_FRAME_HEIGHT, value=550)
        self.cap.set(propId=cv2.CAP_PROP_BRIGHTNESS, value=130)
        self.imgCanvas = np.zeros(shape=(550, 950, 3), dtype=np.uint8)
        self.mphands = hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
        self.p1, self.p2 = 0, 0
        self.p_time = 0
        self.fingers = []

    def process_frame(self):
        success, img = self.cap.read()
        if not success:
            st.error("Error: Could not read from webcam.")
            return
        img = cv2.resize(src=img, dsize=(950, 550))
        self.img = cv2.flip(src=img, flipCode=1)
        self.imgRGB = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

    def process_hands(self):
        result = self.mphands.process(image=self.imgRGB)
        self.landmark_list = []
        if result.multi_hand_landmarks:
            for hand_lms in result.multi_hand_landmarks:
                drawing_utils.draw_landmarks(
                    image=self.img, landmark_list=hand_lms,
                    connections=hands.HAND_CONNECTIONS)
                for id, lm in enumerate(hand_lms.landmark):
                    h, w, c = self.img.shape
                    x, y = lm.x, lm.y
                    cx, cy = int(x * w), int(y * h)
                    self.landmark_list.append([id, cx, cy])

    def identify_fingers(self):
        self.fingers = []
        if self.landmark_list != []:
            for id in [4, 8, 12, 16, 20]:
                if id != 4:
                    if self.landmark_list[id][2] < self.landmark_list[id - 2][2]:
                        self.fingers.append(1)
                    else:
                        self.fingers.append(0)
                else:
                    if self.landmark_list[id][1] < self.landmark_list[id - 2][1]:
                        self.fingers.append(1)
                    else:
                        self.fingers.append(0)
            for i in range(0, 5):
                if self.fingers[i] == 1:
                    cx, cy = self.landmark_list[(i + 1) * 4][1], self.landmark_list[(i + 1) * 4][2]
                    cv2.circle(img=self.img, center=(cx, cy), radius=5, color=(255, 0, 255), thickness=1)

    def handle_drawing_mode(self):
        if sum(self.fingers) == 2 and self.fingers[0] == self.fingers[1] == 1:
            cx, cy = self.landmark_list[8][1], self.landmark_list[8][2]
            if self.p1 == 0 and self.p2 == 0:
                self.p1, self.p2 = cx, cy
            cv2.line(self.imgCanvas, (self.p1, self.p2), (cx, cy), (255, 255, 255), 5)
            self.p1, self.p2 = cx, cy
        elif sum(self.fingers) == 3 and self.fingers[0] == self.fingers[1] == self.fingers[2] == 1:
            self.p1, self.p2 = 0, 0
        elif sum(self.fingers) == 2 and self.fingers[0] == self.fingers[2] == 1:
            cx, cy = self.landmark_list[12][1], self.landmark_list[12][2]
            if self.p1 == 0 and self.p2 == 0:
                self.p1, self.p2 = cx, cy
            cv2.line(self.imgCanvas, (self.p1, self.p2), (cx, cy), (0, 0, 0), 15)
            self.p1, self.p2 = cx, cy
        elif sum(self.fingers) == 2 and self.fingers[0] == self.fingers[4] == 1:
            self.imgCanvas = np.zeros(shape=(550, 950, 3), dtype=np.uint8)

    def blend_canvas_with_feed(self):
        img = cv2.addWeighted(self.img, 0.7, self.imgCanvas, 1, 0)
        imgGray = cv2.cvtColor(self.imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        self.img = cv2.bitwise_or(img, self.imgCanvas)

    def display_instructions(self):
     instructions = """
        ### How to Use Virtual Calculator and Canvas
    
        - **Both Thumb and Index Fingers Up (✌️)**: Drawing mode - draw on the canvas.
        - **Thumb, Index & Middle Fingers Up (👌)**: Disable drawing (stop connecting points).
        - **Both Thumb and Middle Fingers Up**: Erase drawing lines by moving the middle finger.
        - **Both Thumb and Pinky Fingers Up**: Clear the entire canvas (reset).
        - **Index and Middle Fingers Up**: Trigger analysis of the drawing via AI.

    Make sure your hand is clearly visible to the webcam for best detection.
    """

     st.markdown(instructions)


    def analyze_image_with_genai(self):
        imgCanvas = cv2.cvtColor(self.imgCanvas, cv2.COLOR_BGR2RGB)
        imgCanvas = PIL.Image.fromarray(imgCanvas)
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        prompt = (
            "Analyze the image and provide the following:\n"
            "* The mathematical equation represented in the image.\n"
            "* The solution to the equation.\n"
            "* A short and sweet explanation of the steps taken to arrive at the solution.")
        response = model.generate_content([prompt, imgCanvas])
        return response.text

    def main(self):
        self.display_instructions()
        col1, _, col3 = st.columns([0.8, 0.02, 0.18])
        with col1:
            stframe = st.empty()
        with col3:
            st.markdown(f'<h5 style="text-position:center;color:green;">OUTPUT:</h5>', unsafe_allow_html=True)
            result_placeholder = st.empty()
        while True:
            if not self.cap.isOpened():
                add_vertical_space(5)
                st.markdown('<h4 style="text-position:center; color:orange;">Error: Could not open webcam. \
                    Please ensure your webcam is connected and try again</h4>', unsafe_allow_html=True)
                break
            
            self.process_frame()
            
            self.process_hands()
            self.identify_fingers()
            self.handle_drawing_mode()
            self.blend_canvas_with_feed()
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            stframe.image(self.img, channels="RGB")
            if sum(self.fingers) == 2 and self.fingers[1] == self.fingers[2] == 1:
                result = self.analyze_image_with_genai()
                result_placeholder.write(f"Result: {result}")
        self.cap.release()
        cv2.destroyAllWindows()

try:
    calc = calculator()
    calc.streamlit_config()
    calc.main()
except Exception as e:
    add_vertical_space(5)
    st.markdown(f'<h5 style="text-position:center;color:orange;">{e}</h5>', unsafe_allow_html=True)

import streamlit as st
import cv2
import mediapipe as mp
import pyautogui
import math

# Function to calculate Euclidean distance
def euclidean_distance(landmark1, landmark2, frame_w, frame_h):
    x1, y1 = int(landmark1.x * frame_w), int(landmark1.y * frame_h)
    x2, y2 = int(landmark2.x * frame_w), int(landmark2.y * frame_h)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    # Streamlit app title and description
    st.title("Eye Controlled Mouse Application")
    st.write("Control your mouse pointer and perform clicks with your eyes!")

    # Initialize components for face mesh detection and video capture
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()

    stframe = st.empty()  # Placeholder to display video frames in Streamlit
    st.title("Instructions to use")
    st.write("1.Ensure proper lighting and that your face is clearly visible to the webcam.")
    st.write("2.Use your **Right Eye** to control the movement of the mouse pointer across the screen.")
    st.write("3.Close your **left eye** to simulate a mouse click.")
    st.write("4.Press the **'Q' key** to safely exit the application.")
    # Processing webcam feed
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)  # Flip frame horizontally
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape

        if landmark_points:
            landmarks = landmark_points[0].landmark

            # Draw eye landmarks
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))  # Draw landmarks

                if id == 1:  # Right eye for controlling mouse
                    screen_x = int(screen_w * landmark.x)
                    screen_y = int(screen_h * landmark.y)
                    pyautogui.moveTo(screen_x, screen_y)

            # Detect blinking based on the left eye
            left_eye_top = landmarks[159]
            left_eye_bottom = landmarks[145]

            # Calculate the distance between the two points
            eye_open_distance = euclidean_distance(left_eye_top, left_eye_bottom, frame_w, frame_h)

            # Visualize the landmarks used for blinking detection
            cv2.circle(frame, (int(left_eye_top.x * frame_w), int(left_eye_top.y * frame_h)), 3, (0, 255, 255), -1)
            cv2.circle(frame, (int(left_eye_bottom.x * frame_w), int(left_eye_bottom.y * frame_h)), 3, (0, 255, 255), -1)

            # Check if eye is closed (adjust threshold as necessary)
            if eye_open_distance < 5:  # Adjust threshold based on testing
                pyautogui.click()
                pyautogui.sleep(1)  # Prevent multiple clicks

        # Convert frame for display
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame, channels="RGB")  # Display frame in Streamlit

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cam.release()
    cv2.destroyAllWindows()

# Run the Streamlit app
if __name__ == "__main__":
    main()
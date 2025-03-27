# Eye-Controlled Mouse Application

This project is an **eye-controlled mouse application** that allows users to control their mouse pointer and perform click actions using only their eyes. It leverages computer vision techniques and facial landmark detection through **MediaPipe FaceMesh**.

---

## Features

- **Eye Movement Tracking**:
  - Control the mouse pointer using eye movement.
- **Blink Detection for Mouse Clicks**:
  - Detects blinks to simulate left mouse clicks.
- **Face Mesh Visualization**:
  - Highlights key facial landmarks for eye tracking and blink detection.
- **Streamlit Web Interface**:
  - Provides an intuitive web-based interface for running the application.
- **Real-Time Processing**:
  - Processes webcam feed in real-time to provide immediate interactions.

---

## Technology Stack

- **Streamlit**: For creating the web-based interface.
- **OpenCV**: For capturing and processing video frames.
- **MediaPipe**: For facial landmark and eye tracking.
- **PyAutoGUI**: For controlling the mouse and simulating click events.
- **Python**: The programming language used to develop the application.

---

## Setup Instructions

1. **Install Dependencies**:
   Make sure you have Python installed. Install the required libraries by running:
   ```bash
   pip install streamlit opencv-python mediapipe  pyautogui


## Run in your Computer
1. Clone or Download the Repository: 
   git clone <Repository_Name>
   cd virtual keyboard

2. Run the Application: Execute the script:
   streamlit run app.py

---


## How to Use

1. **Launch the Application**:
   - Run the script in a Python-supported environment.
   - Allow webcam access when prompted.
   - Ensure proper lighting and that your face is clearly visible to the webcam.

2. **Move the Mouse Pointer**:
   - Use your **right eye** to control the movement of the mouse pointer across the screen.
   - The pointer moves based on the detected position of specific eye landmarks.

3. **Perform a Click**:
   - Close your **left eye** to simulate a mouse click.
   - The application detects blinking by measuring the vertical distance between key points on the left eye.

4. **Quit the Application**:
   - Press the **'Q' key** to safely exit the application.

---

## Key Functionalities

- **Eye Movement Tracking**:
  - Tracks the movement of the user's right eye to control the mouse pointer.

- **Blink Detection for Clicks**:
  - Detects blinks from the left eye to perform mouse click actions.

- **Face Mesh Visualization**:
  - Displays the detected landmarks and highlights areas used for interaction.

- **Streamlit Web Interface**:
  - Runs the application within a web browser using the Streamlit framework.

---

## Known Issues

- **Lighting Sensitivity**:
  - Accuracy may decrease in low-light environments or with uneven lighting.

- **Calibration**:
  - The pointer control might require fine-tuning for different users or screen resolutions.

- **Resource Intensive**:
  - Continuous video processing may affect performance on low-end systems.

- **Blink Misinterpretation**:
  - The blink detection threshold might need adjustment for different face shapes or distances from the webcam.

---

## Future Enhancements

1. **Additional Mouse Actions**:
   - Implement right-click, drag-and-drop, and scrolling gestures.

2. **Adaptive Sensitivity**:
   - Automatically adjust detection thresholds based on environmental conditions.

3. **Multi-Screen Support**:
   - Extend functionality to handle multiple monitor setups.

4. **User Calibration**:
   - Add an initial calibration step for better personalization and accuracy.

5. **Portable Version**:
   - Develop a cross-platform version for mobile and tablet devices.

6. **Gesture Customization**:
   - Allow users to define their own gestures for specific actions.

---

## Acknowledgments

This project utilizes the following tools and libraries:
- **Streamlit**: For creating the web interface.
- **OpenCV**: For video frame capture and processing.
- **MediaPipe**: For facial landmark and eye tracking.
- **PyAutoGUI**: For mouse control and interaction.
- **Python**: The programming language used to develop the project.






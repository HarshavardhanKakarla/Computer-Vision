# Hand Gesture Virtual Keyboard

This project is a **hand gesture-based virtual keyboard** application that allows users to type on a virtual keyboard using hand gestures detected via a webcam. The application leverages **computer vision** and **hand tracking** to enable interaction with the keyboard. It is built using Python and utilizes libraries such as OpenCV, cvzone, and pynput.

---

## Features
- **Gesture-Based Typing**: Use hand gestures to select and press virtual keys.
- **Save Functionality**: Save the typed text to a timestamped file.
- **Clear Functionality**: Clear the current typed text in the virtual text box.
- **Exit Gesture**: Close the program using a fist gesture.
- **Real-Time Hand Tracking**: Detect and track hand movements using cvzone's `HandDetector`.

---

## Technology Stack
- **Python**
- **OpenCV**: For capturing and processing the video feed.
- **cvzone**: For hand detection and drawing UI elements.
- **pynput**: To emulate keyboard functionality.
- **NumPy**: For efficient mathematical operations.
- **os and datetime**: For file handling and timestamping.

---

## Setup Instructions
1. **Install Dependencies**:
   Make sure you have Python installed. Install the required libraries by running:
   ```bash
   pip install opencv-python opencv-contrib-python cvzone numpy pynput


## Run in your Computer
1. Clone or Download the Repository: 
   git clone <Repository_Name>
   cd virtual keyboard

2. Run the Application: Execute the script:
   python app.py


---

## How to Use

1. **Launch the Application**:
   - Start the program to activate your webcam.
   - Ensure your hands are visible in the webcam feed for proper tracking.

2. **Typing**:
   - Hover your index finger over a key on the virtual keyboard and make a pinch gesture to select and type the key.
   - Use special buttons:
     - **SAVE**: Press to store the current text into a `.txt` file.
     - **CLEAR**: Press to delete the text in the input box.

3. **Closing the Application**:
   - Make a **fist gesture** to exit the program safely. The current text is saved automatically before exiting.

4. **Accessing Saved Files**:
   - All saved files are located in the `typed_texts` folder, with filenames generated based on the timestamp.

---

## Key Functionalities

- **Gesture-Based Typing**: Utilize hand gestures for typing in real-time.
- **Dynamic Button Creation**: All virtual buttons are dynamically positioned for efficient interaction.
- **Save Feature**: Stores typed content to a `.txt` file with a timestamp for easy retrieval.
- **Clear Feature**: Provides the ability to quickly erase typed content from the input box.
- **Exit Gesture**: Close the application using a fist gesture, ensuring that the typed text is saved before exiting.

---

## Known Issues

- **Gesture Sensitivity**: Accuracy may be impacted under poor lighting conditions or if the hand movements are fast.
- **Hardware Dependency**: Requires a well-functioning webcam for optimal performance.
- **Tracking Challenges**: Occluded hands or excessive background noise may interfere with gesture detection.
- **Pinch Detection**: The pinch gesture may occasionally misfire, particularly when fingers are not fully visible to the camera.

---

## Future Enhancements

- **Multilingual Keyboard Support**: Add options for various language keyboards.
- **Advanced Gestures**: Implement additional gestures for features like copy-paste or undo-redo.
- **User Feedback System**: Provide real-time feedback for detected gestures to enhance user experience.
- **Adaptive Sensitivity**: Introduce dynamic adjustments to improve gesture recognition in varying environmental conditions.
- **Cloud Integration**: Store typed content directly to the cloud for easy access across devices.
- **Mobile Compatibility**: Extend the application to mobile platforms for wider accessibility.

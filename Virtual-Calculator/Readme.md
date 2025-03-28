# Virtual Calculator with Gesture and AI Capabilities
  or
# Virtual Canva with gesture

This project is an innovative **Virtual Calculator** that combines **gesture recognition** and **AI analysis**. Users can draw mathematical equations using their fingers in real-time, and the application processes the input using generative AI to analyze and solve the equations.  

or   

This project can be modified by removing google api(AI) section and can be developed as another project, which can be used for drawing virtually with gestures. 


---

## Features

- **Gesture-Based Drawing**:
  - Draw mathematical equations or figures directly using finger gestures captured by a webcam.
  
- **Real-Time Hand Tracking**:
  - Leverages MediaPipe Hands for accurate detection and tracking of hand gestures and finger positions.

- **AI-Driven Analysis**:
  - Integrates Google's Generative AI to analyze and solve equations drawn by the user.

- **Dynamic Canvas**:
  - A virtual canvas that supports drawing, erasing, and resetting to manage input easily.

- **Streamlit Integration**:
  - User-friendly web interface powered by Streamlit for seamless interaction.

---

## Technology Stack

- **Streamlit**: Provides a lightweight and interactive web interface.
- **OpenCV**: Processes and displays video streams from the webcam.
- **MediaPipe**: Handles real-time hand detection and landmark tracking.
- **NumPy**: Used for efficient image and matrix operations.
- **Pillow (PIL)**: For converting numpy arrays to image objects.
- **Google Generative AI (genai)**: Implements AI-powered content generation for analyzing drawn inputs.

---

## Setup Instructions

### Install Dependencies

1. Ensure Python is installed on your system, then run the following command to install required libraries:
    ```bash
     pip install streamlit opencv-python mediapipe numpy pillow google-generativeai streamlit-extras python-dotenv

---

## Clone Repository

    To get started, clone this repository to your local machine using the following commands:
    ```bash
    git clone <repository_url>
    cd <repository_folder>

---

## Google API Key

To enable AI-powered functionalities in the application, you must configure your Google API key:

1. **Obtain the API Key**:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Set up a project and enable the necessary APIs.
   - Generate an API key.

2. **Set Up the API Key**:
   - Create a `.env` file in the root directory of the project.
   - Add the following content to the file:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

---

## How to Use

1. **Run the Application**:
   - Open a terminal in the project directory.
   - Start the application using the following command:
     ```bash
     streamlit run app.py
     ```

2. **Draw on the Canvas**:
   - Use your hand gestures to interact with the virtual canvas:
     - **Drawing Mode**: Index finger and thumb up.
     - **Move on Screen**: Thumb, Index & Middle Fingers UP (Disable the Points Connection)
     - **Erase Mode**: Thumb and middle finger up.
     - **Reset Canvas**: Thumb and pinky finger up.

3. **Analyze the Drawing**:
   - Activate AI analysis by showing your index and middle fingers.
   - Results will be displayed on the right-hand side in the output panel.

4. **Exit the Application**:
   - To quit, close the Streamlit server running in your terminal.

---

## Key Functionalities

- **Gesture-Based Drawing**:
  - Use hand gestures to draw mathematical equations or shapes.

- **AI Analysis**:
  - Analyze the equations and provide solutions using Google's Generative AI.

- **Real-Time Feedback**:
  - Visualize your drawings directly on a virtual canvas with real-time updates.

- **Interactive Modes**:
  - Switch between drawing, erasing, and resetting using specific hand gestures.

- **User-Friendly Interface**:
  - Access the application through a browser with an intuitive interface powered by Streamlit.

---

## Known Issues

- **Gesture Recognition**:
  - May struggle in environments with poor lighting or obstructed hand visibility.

- **Performance Limitations**:
  - Requires a machine with sufficient processing power for real-time analysis.

- **API Dependency**:
  - Relies on valid API credentials, which may limit functionality if quota or errors occur.

- **Gesture Sensitivity**:
  - Incorrect gestures may occasionally be misinterpreted, leading to unintentional actions.

---

## Future Enhancements

1. **Advanced Mathematical Operations**:
   - Support for solving calculus, graph plotting, and 3D visualizations.

2. **Multi-Gesture Customization**:
   - Allow users to personalize hand gestures for specific tasks.

3. **Offline AI Functionality**:
   - Develop an offline model to process equations locally without API dependencies.

4. **Extended Language Support**:
   - Enable multi-language compatibility for instructions and analysis.

5. **Optimized Performance**:
   - Improve computation efficiency for smoother real-time processing.

6. **Mobile Integration**:
   - Create a mobile version for smartphones and tablets.



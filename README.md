
# Vision.ai

**Vision.ai** is a Flask-based web application that allows users to control their computer's mouse and click functionalities using hand gestures. It leverages the power of computer vision libraries such as OpenCV and MediaPipe to detect and track hand movements in real-time, mapping hand gestures to mouse actions.

## Features

- **Hand Gesture Tracking**: Detects and tracks the movement of your hand in real-time using MediaPipe's hand landmark detection.
- **Mouse Control**: Moves the mouse cursor based on the movement of the index finger and performs a click when the thumb and index fingers come close together.
- **Web Interface**: A simple web-based interface powered by Flask to control the application.

## Installation

To get started with **Vision.ai**, you'll need to clone this repository and install the necessary dependencies.

1. Clone the repository:
    ```bash
    git clone https://github.com/Sandmish123/Vision.ai.git
    cd Vision.ai
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

   Make sure to add the `requirements.txt` file with the following content:
    ```
    Flask==2.0.1
    opencv-python==4.5.1.48
    mediapipe==0.8.6
    pyautogui==0.9.52
    ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`. The application will open the webcam feed and start detecting hand gestures.

3. **Control the mouse**: Move your hand in front of the webcam. The index finger's position will move the mouse cursor, and a click will occur when the thumb and index finger come close together.

## Code Overview

- **Flask Web Server**: The Flask app serves the interface and handles requests to start the hand tracking process.
- **MediaPipe Hand Landmark Detection**: The app uses MediaPipe to track the hand's landmarks and calculate the position of the index finger and thumb.
- **PyAutoGUI**: The library is used to control the mouse and simulate clicks based on hand gestures.

## Technologies Used

- **Flask**: For building the web server and rendering the frontend.
- **OpenCV**: For accessing the webcam and processing video frames.
- **MediaPipe**: For hand gesture recognition and landmark detection.
- **PyAutoGUI**: For controlling the mouse based on hand gestures.

## Future Improvements

- Support for multi-hand tracking.
- Integration with more hand gestures for advanced controls.
- Option to customize mouse sensitivity and click actions.
- Real-time feedback and performance optimization.


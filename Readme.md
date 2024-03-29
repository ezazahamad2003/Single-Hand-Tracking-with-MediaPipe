# Single-Hand Tracking with MediaPipe

This project utilizes OpenCV and MediaPipe to track a single hand's movement in real-time through a webcam feed. It draws landmarks on the detected hand and surrounds it with a bounding box that moves and resizes dynamically with the hand's position and gestures. The application is designed to ignore additional hands, focusing solely on the first detected hand in the scene.

## Features

- Real-time hand tracking
- Dynamic bounding box around the hand
- Single-hand focus for cleaner tracking
- Visual feedback for hand position and gestures

## Prerequisites

Before you run this project, make sure you have the following installed:
- Python 3.6 or later
- OpenCV
- MediaPipe

You can install the necessary Python packages using pip:

```bash
pip install opencv-python mediapipe numpy
```

## Running the Application

To start hand tracking, simply run the script from your command line:

```bash
python hand_tracking.py
```

Ensure your webcam is connected and permitted to be used by the application. The program will open a window showing the live feed from your webcam. Once a hand is detected, it will be highlighted with landmarks and a bounding box.

To exit the application, press the `ESC` key.

## How It Works

The application initializes the webcam and processes each frame using MediaPipe's hand tracking solution. It flips the image for a mirror view and converts it to RGB for MediaPipe processing. When a hand is detected, landmarks are drawn, and a bounding box is calculated based on the extremities of these landmarks. The application then draws this bounding box on the frame, adjusting its size and position as the hand moves. The processing loop continues until the `ESC` key is pressed, at which point the application releases the webcam and exits.

## Customization

You can customize several aspects of the application, including:

- `min_detection_confidence` and `min_tracking_confidence` in the `mp_hands.Hands()` constructor to adjust the model's sensitivity.
- The `padding` value used when drawing the bounding box, to change how tightly the box fits around the hand.
- The colors and thickness of the drawn landmarks and bounding box.

Explore the MediaPipe documentation and OpenCV tutorials to learn more about what you can do with these powerful tools.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.


import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1) as hands:  # Limit the max number of hands to detect/process to 1
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        # Calculating the bounding box for the first hand
        h, w, _ = image.shape
        landmark_array = np.array([(lm.x, lm.y) for lm in hand_landmarks.landmark])
        x_min, y_min = np.min(landmark_array, axis=0)
        x_max, y_max = np.max(landmark_array, axis=0)

        x_min, x_max = int(x_min * w), int(x_max * w)
        y_min, y_max = int(y_min * h), int(y_max * h)

        padding = 20
        x_min, x_max = max(x_min - padding, 0), min(x_max + padding, w)
        y_min, y_max = max(y_min - padding, 0), min(y_max + padding, h)

        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        
        # Once the first hand is processed, break the loop to ignore other hands
        break

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

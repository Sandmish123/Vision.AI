import cv2
import mediapipe
import pyautogui

# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Error: Unable to open camera.")
# else:
#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read() 

#         if ret:
#             # Display the frame
#             cv2.imshow('frame', frame)

#         # Check if the user pressed the 'q' key
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the camera
#     cap.release()

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui

# # Initialize MediaPipe hands module
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands()

# # Capture video from webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # Convert the frame to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     # Detect hands in the frame
#     results = hands.process(frame_rgb)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Extract hand landmarks
#             # You can use hand_landmarks to track hand movement or detect gestures
            
#             # Draw hand landmarks on the frame
#             # Example: cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            
#             # Map hand movement to mouse movement
#             # Example: pyautogui.moveTo(cx, cy)
    
#     # Display output
#         cv2.imshow('Hand Tracking', frame)
    
#     # Exit on ESC
#     if cv2.waitKey(1) == 27:
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp

# # Initialize MediaPipe hands module
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # Initialize MediaPipe drawing module
# mp_draw = mp.solutions.drawing_utils

# # Capture video from webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the frame to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detect hands in the frame
#     results = hands.process(frame_rgb)

#     # Draw hand landmarks and gesture annotations
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             # Get hand gesture
#             if hands:
#                 landmarks = hand_landmarks.landmark
#                 # Use the landmarks to determine hand gesture
#                 # Example: You can use the position of landmarks to recognize gestures
#                 # For example, make a fist, spread fingers, etc.

#     # Display output
#     cv2.imshow('Hand Gesture Recognition', frame)

#     # Exit on ESC
#     if cv2.waitKey(1) == 27:
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui

# # Initialize MediaPipe hands module
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # Initialize MediaPipe drawing module
# mp_draw = mp.solutions.drawing_utils

# # Capture video from webcam
# cap = cv2.VideoCapture(0)

# # Get screen dimensions
# screen_width, screen_height = pyautogui.size()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the frame to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detect hands in the frame
#     results = hands.process(frame_rgb)

#     # Draw hand landmarks
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             # Get index finger tip position
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             # Convert normalized coordinates to screen coordinates
#             index_finger_x = int(index_finger_tip.x * screen_width)
#             index_finger_y = int(index_finger_tip.y * screen_height)
            
#             # Move mouse cursor
#             pyautogui.moveTo(index_finger_x, index_finger_y)

#             # Check if thumb is in clicking position (e.g., near index finger)
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             thumb_x = int(thumb_tip.x * screen_width)
#             thumb_y = int(thumb_tip.y * screen_height)
#             # Example condition for clicking (adjust as needed)
#             if abs(thumb_x - index_finger_x) < 20 and abs(thumb_y - index_finger_y) < 20:
#                 # Perform mouse click action
#                 pyautogui.click()
    
#     # Display output
#     cv2.imshow('Hand Gesture Recognition', frame)
    
#     # Exit on ESC
#     if cv2.waitKey(1) == 27:
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# import pyautogui
# import math

# # Initialize MediaPipe hands module
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # Initialize MediaPipe drawing module
# mp_draw = mp.solutions.drawing_utils

# # Capture video from webcam
# cap = cv2.VideoCapture(0)

# # Get screen dimensions
# screen_width, screen_height = pyautogui.size()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the frame to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detect hands in the frame
#     results = hands.process(frame_rgb)

#     # Draw hand landmarks
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             # Get index finger tip position
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             index_finger_x = int(index_finger_tip.x * screen_width)
#             index_finger_y = int(index_finger_tip.y * screen_height)
#             print("(x,y)","(",index_finger_x,index_finger_y,")")
            
#                # Move mouse cursor
#             pyautogui.moveTo(index_finger_x, index_finger_y)
            
#             # Get thumb tip position
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             thumb_x = int(thumb_tip.x * screen_width)
#             thumb_y = int(thumb_tip.y * screen_height)

#             # Calculate Euclidean distance between thumb and index finger
#             distance = math.sqrt((index_finger_x - thumb_x)**2 + (index_finger_y - thumb_y)**2)

#             # Example condition for clicking (adjust threshold as needed)
#             if distance < 10:  # Adjust threshold as needed
#                 # Perform mouse click action
#                 pyautogui.click()
    
#     # Display output
#     cv2.imshow('Hand Gesture Recognition', frame)
    
#     # Exit on ESC
#     if cv2.waitKey(1) == 27:
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# import pyautogui
# import math

# # Initialize MediaPipe hands module
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # Initialize MediaPipe drawing module
# mp_draw = mp.solutions.drawing_utils

# # Capture video from webcam
# cap = cv2.VideoCapture(0)

# # Get screen dimensions
# screen_width, screen_height = pyautogui.size()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert the frame to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detect hands in the frame
#     results = hands.process(frame_rgb)

#     # Draw hand landmarks
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
#             # Get index finger tip position
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#             index_finger_x = int(index_finger_tip.x * screen_width)
#             index_finger_y = int(index_finger_tip.y * screen_height)
#             print("(x,y)","(",index_finger_x,index_finger_y,")")
            
#             # Move mouse cursor
#             pyautogui.moveTo(index_finger_x, index_finger_y)
            
#             # Get thumb tip position
#             thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             thumb_x = int(thumb_tip.x * screen_width)
#             thumb_y = int(thumb_tip.y * screen_height)

#             # Calculate Euclidean distance between thumb and index finger
#             distance = math.sqrt((index_finger_x - thumb_x)**2 + (index_finger_y - thumb_y)**2)

#             # Example condition for clicking (adjust threshold as needed)
#             if distance < 10:  # Adjust threshold as needed
#                 # Perform mouse click action
#                 pyautogui.click()
    
#     # Limit display updates to every 5 frames
#     if cap.get(cv2.CAP_PROP_POS_FRAMES) % 5 == 0:
#         cv2.imshow('Hand Gesture Recognition', frame)
    
#     # Exit on ESC
#     if cv2.waitKey(1) == 27:
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()



from flask import Flask, render_template, request
import cv2
import mediapipe as mp
import pyautogui
import math

app = Flask(__name__)

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)


# Initialize MediaPipe drawing module
mp_draw = mp.solutions.drawing_utils

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track_hand', methods=['POST'])
def track_hand():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_finger_x = int(index_finger_tip.x * screen_width)
                index_finger_y = int(index_finger_tip.y * screen_height)
                pyautogui.moveTo(index_finger_x, index_finger_y)

                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_x = int(thumb_tip.x * screen_width)
                thumb_y = int(thumb_tip.y * screen_height)

                distance = math.sqrt((index_finger_x - thumb_x)**2 + (index_finger_y - thumb_y)**2)

                if distance < 10:  
                    pyautogui.click()
             # Limit display updates to every 5 frames
        if cap.get(cv2.CAP_PROP_POS_FRAMES) % 5 == 0:
            cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return 'Hand tracking completed'

if __name__ == '__main__':
    app.run(debug=True)

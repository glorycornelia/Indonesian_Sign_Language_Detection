import cv2
import streamlit as st
import numpy as np
import mediapipe as mp
from PIL import Image
from tensorflow.keras.models import load_model

# Initialize MediaPipe and other settings
mp_holistic = mp.solutions.holistic  # Holistic model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results
    
def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, lh, rh])

sequence = []
sentence = []
threshold = 0.5
actions = np.array(['halo', 'selamat pagi', 'selamat siang', 'selamat sore', 'selamat malam',
                    'apa kabar', 'sampai jumpa lagi', 'perkenalkan', 'aku', 'kamu', 
                    'maaf', 'tolong', 'terima kasih', 'sama-sama', 'ya', 'tidak', 'mau', 
                    'tidak mau', 'suka', 'makanan'])
model = load_model('model6.h5')

cap = cv2.VideoCapture(0)
st.title("Deteksi Bahasa Isyarat")
st.subheader("Aplikasi penerjemah bahasa isyarat SIBI menggunakan mediapipe dan metode LSTM")
st.text("Projek skripsi Glory Cornelia Patining Kurik")

# Set up Streamlit elements
video_placeholder = st.empty()  # Placeholder for video
text_placeholder = st.empty()   # Placeholder for text
stop_button_pressed = st.button('Berhenti')

# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened() and not stop_button_pressed:

        ret, frame = cap.read()
        if not ret:
            st.error("Error: Cannot receive frame. Exiting ...")
            break

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        
        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-20:]
        
        if len(sequence) == 20:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            
            # Prediction text
            prediction_text = actions[np.argmax(res)]
            if res[np.argmax(res)] > threshold: 
                if len(sentence) > 0: 
                    if actions[np.argmax(res)] != sentence[-1]:
                        sentence.append(prediction_text)
                else:
                    sentence.append(prediction_text)

            if len(sentence) > 5: 
                sentence = sentence[-5:]
        
        # Convert BGR image to RGB for Streamlit
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Update Streamlit placeholders
        video_placeholder.image(image_rgb, channels="RGB")
        text_placeholder.text(' '.join(sentence))
        
        # Stop capturing on user interaction (add a button to stop streaming)
        if cv2.waitKey(10) & 0xFF == ord('q') or stop_button_pressed:
            break

cap.release()
cv2.destroyAllWindows()
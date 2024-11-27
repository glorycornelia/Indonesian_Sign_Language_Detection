import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
from tensorflow.keras.models import load_model
import mediapipe as mp

# Load the trained LSTM model
model = load_model('my_model.h5')
actions = np.array(['halo', 'selamat pagi', 'selamat siang', 'selamat sore', 'selamat malam',
                    'apa kabar', 'sampai jumpa lagi', 'perkenalkan', 'aku', 'kamu',
                    'maaf', 'tolong', 'terima kasih', 'sama-sama', 'ya', 'tidak', 'mau',
                    'tidak mau', 'suka', 'makanan'])

# Mediapipe setup
mp_holistic = mp.solutions.holistic

# Helper functions
def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33 * 4)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21 * 3)
    return np.concatenate([pose, lh, rh])

# Thread for video capture and processing
class CameraThread(QThread):
    frame_updated = pyqtSignal(np.ndarray)
    prediction_updated = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.sequence = []
        self.cap = None

    def run(self):
        self.cap = cv2.VideoCapture(0)
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    break
                image, results = mediapipe_detection(frame, holistic)
                keypoints = extract_keypoints(results)
                self.sequence.append(keypoints)
                self.sequence = self.sequence[-20:]

                if len(self.sequence) == 20:
                    prediction = model.predict(np.expand_dims(self.sequence, axis=0))[0]
                    self.prediction_updated.emit(actions[np.argmax(prediction)])

                self.frame_updated.emit(image)

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.quit()
        self.wait()

# Main application window
class SignLanguageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Language Detection")
        self.setGeometry(200, 200, 900, 700)
        self.setStyleSheet("background-color: #f7f7f7; font-family: Arial;")

        self.camera_thread = CameraThread()
        self.camera_thread.frame_updated.connect(self.update_frame)
        self.camera_thread.prediction_updated.connect(self.update_prediction)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_video = QLabel()
        self.label_video.setStyleSheet("border: 2px solid black; background-color: #000;")
        self.label_video.setFixedSize(640, 480)
        layout.addWidget(self.label_video)

        self.label_prediction = QLabel("Translated Text: ")
        self.label_prediction.setStyleSheet("font-size: 20px; color: #333; padding: 10px;")
        layout.addWidget(self.label_prediction)

        self.button_open = QPushButton("Open Camera")
        self.button_open.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
                font-size: 16px; 
                border-radius: 5px; 
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.button_open.clicked.connect(self.start_camera)
        layout.addWidget(self.button_open)

        self.button_close = QPushButton("Close Camera")
        self.button_close.setStyleSheet("""
            QPushButton {
                background-color: #f44336; 
                color: white; 
                font-size: 16px; 
                border-radius: 5px; 
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
        """)
        self.button_close.clicked.connect(self.stop_camera)
        layout.addWidget(self.button_close)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_camera(self):
        self.camera_thread.running = True
        self.camera_thread.start()

    def stop_camera(self):
        self.camera_thread.stop()
        self.label_video.clear()
        self.label_video.setText("Camera feed will appear here.")
        self.label_prediction.setText("Translated Text: ")

    def update_frame(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        bytes_per_line = channel * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.label_video.setPixmap(QPixmap.fromImage(q_image))

    def update_prediction(self, text):
        self.label_prediction.setText(f"Translated Text: {text}")

# Main application entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignLanguageApp()
    window.show()
    sys.exit(app.exec_())
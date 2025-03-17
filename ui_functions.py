from main import *

# Load the trained LSTM model
model = load_model('Preprocessing/models/model_windowed_seq_5.h5')
actions = np.array(['halo', 'apa kabar', 'aku', 'kamu', 'maaf', 'tolong', 'ya', 'tidak', 'suka', 'makanan', 
                    'selamat pagi', 'selamat siang', 'selamat sore', 'selamat malam', 'sampai jumpa lagi', 
                    'perkenalkan', 'terima kasih', 'sama-sama', 'mau', 'tidak mau'])

# Mediapipe setup
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

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

def draw_styled_landmarks(image, results):
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=1, circle_radius=3), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=1, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=1, circle_radius=3), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=1, circle_radius=1)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=1, circle_radius=3), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=1, circle_radius=1)
                             ) 

class CameraThread(QThread):    # Windowed Sequence
    frame_updated = Signal(np.ndarray)
    prediction_updated = Signal(str)
    indicator_updated = Signal(str)  # Signal for indicator (red/green)

    def __init__(self):
        super().__init__()
        self.running = False
        self.sequence = []
        self.sentence = []
        self.threshold = 0.75
        self.frame_counter = 0  # Count total frames
        self.processing = False  # Indicator flag
        self.lock = threading.Lock()

        self.window_size = 10  # Window size for input
        self.stride = 5  # Stride for moving window
        self.prediction_interval = 30  # Predict every 30 frames

        # Load RealSense camera
        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(config)

    def run(self):
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            self.running = True

            while self.running:
                frames = self.pipeline.wait_for_frames()
                color_frame = frames.get_color_frame()
                if not color_frame:
                    continue

                frame = np.asanyarray(color_frame.get_data())
                self.frame_counter += 1  # Count total frames
                
                # Capture keypoints every frame
                image, results = mediapipe_detection(frame, holistic)
                keypoints = extract_keypoints(results)

                with self.lock:
                    self.sequence.append(keypoints)
                    if len(self.sequence) > self.window_size:
                        self.sequence.pop(0)  # Keep last `window_size` frames

                # Predict every 30 frames
                if self.frame_counter % self.prediction_interval == 0 and len(self.sequence) == self.window_size:
                    self.processing = True  # Start processing
                    self.indicator_updated.emit("red")  # Set indicator to red

                    prediction = model.predict(np.expand_dims(self.sequence, axis=0))[0]
                    predicted_action = actions[np.argmax(prediction)]

                    if prediction[np.argmax(prediction)] > self.threshold:
                        if len(self.sentence) == 0 or predicted_action != self.sentence[-1]:
                            self.sentence.append(predicted_action)
                        self.sentence = self.sentence[-5:]

                    self.prediction_updated.emit(' '.join(self.sentence))

                    # Maintain stride: keep last `stride` frames
                    with self.lock:
                        self.sequence = self.sequence[-self.stride:]

                    self.processing = False  # Resume frame capture
                    self.indicator_updated.emit("green")  # Set indicator to green

                self.frame_updated.emit(frame)

    def stop(self):
        self.running = False
        self.pipeline.stop()
        self.quit()
        self.wait()

class UIFunctions(MainWindow):

    def __init__(self, main_window):
        self.main_window = main_window  # Reference to MainWindow
        self.ui = main_window.ui
        self.camera_thread = None

        # Connect buttons
        self.ui.btn_open_camera.clicked.connect(self.start_camera)
        self.ui.btn_close_camera.clicked.connect(self.stop_camera)
        self.ui.btn_video_upload.clicked.connect(self.upload_video)
        self.ui.btn_detection.clicked.connect(self.process_and_predict_video)

    def start_camera(self):
        """ Start the camera only if page_2 is active. """
        if self.ui.stackedWidget.currentWidget() == self.ui.page_2:
            self.camera_thread = CameraThread()
            self.camera_thread.frame_updated.connect(self.update_camera_feed)
            self.camera_thread.prediction_updated.connect(self.update_prediction_label)
            self.camera_thread.indicator_updated.connect(self.update_indicator)
            self.camera_thread.running = True
            self.camera_thread.start()

    def stop_camera(self):
        """ Stop the camera and clear the QLabel display. """
        if self.camera_thread:
            self.camera_thread.stop()
            self.camera_thread = None
            self.ui.camera_box.clear()
            self.ui.indicator.setStyleSheet(u"background-color: rgb(255, 157, 218);")

    def update_camera_feed(self, image):
        """ Update QLabel with camera feed. """
        frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = frame_rgb.shape
        bytes_per_line = channel * width
        qimage = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.ui.camera_box.setPixmap(QPixmap.fromImage(qimage))

    def update_prediction_label(self, text):
        """ Update QLabel with predictions. """
        self.ui.label_content_text_display.setText(text)

    def update_indicator(self, color):
        if color == "red":
            self.ui.indicator.setStyleSheet("background-color: red;")
        else:
            self.ui.indicator.setStyleSheet("background-color: green;")

    def upload_video(self):
        """Opens a file dialog to select a video and stores frames in memory."""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Video", "", "Video Files (*.mp4 *.avi *.mov)")

        if file_path:
            self.ui.label_video_text.setText(file_path.split("/")[-1])  # Show filename in UI
            self.main_window.video_data = self.load_video(file_path)

    def load_video(self, video_path):
        """Reads video frames into memory without saving it locally."""
        cap = cv2.VideoCapture(video_path)
        frames = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        cap.release()
        return frames

    def process_and_predict_video(self):
        """Processes the uploaded video, extracts keypoints, and makes predictions."""
        if not hasattr(self.main_window, "video_data") or self.main_window.video_data is None:
            self.ui.label_content_text_display_2.setText("Please upload a video first.")
            return

        # Convert frames to LSTM input
        lstm_input = self.process_video_to_lstm_input(self.main_window.video_data)

        # Predict using the trained model
        prediction_label, _ = self.predict_video(lstm_input)

        # Display result
        self.ui.label_content_text_display_2.setText(prediction_label)

    def process_video_to_lstm_input(self, video_frames, target_frame_count=30):
        """Processes a list of frames, extracts MediaPipe landmarks, and formats input for LSTM."""
        frame_count = len(video_frames)
        frame_interval = frame_count // target_frame_count if frame_count > target_frame_count else 1
        frames_data = []

        mp_holistic = mp.solutions.holistic
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            for i in range(target_frame_count):
                frame_idx = i * frame_interval
                if frame_idx >= frame_count:
                    break

                frame = video_frames[frame_idx]

                # Extract landmarks from the frame
                image, results = mediapipe_detection(frame, holistic)
                keypoints = extract_keypoints(results)
                frames_data.append(keypoints)

        # Convert to numpy array
        frames_data = np.array(frames_data)  # Shape: (frame_count, 258)

        # Apply sliding window approach
        X_video = []
        for start in range(0, len(frames_data) - WINDOW_SIZE + 1, STRIDE):
            window = frames_data[start:start + WINDOW_SIZE]  # Shape: (10, 258)
            X_video.append(window)

        if not X_video:  # If the video is too short
            return None  # or handle padding

        return np.array(X_video)  # Shape: (num_windows, 10, 258)

    def predict_video(self, lstm_input):
        """Predicts the sign language gesture from processed LSTM input."""
        if lstm_input is None:
            return "Insufficient Frames", None  # Handle short videos

        lstm_input = np.array(lstm_input)  # Ensure it's an array
        predictions = model.predict(lstm_input)  # Shape: (num_windows, num_classes)

        # Aggregate predictions (e.g., majority vote or average probabilities)
        avg_prediction = np.mean(predictions, axis=0)  # Averaging over windows
        predicted_class = np.argmax(avg_prediction)  # Highest probability class index
        predicted_label = actions[predicted_class]  # Convert to class label

        return predicted_label, avg_prediction

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
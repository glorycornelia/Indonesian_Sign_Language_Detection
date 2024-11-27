import React, { useState, useRef, useEffect } from "react";
import Webcam from "react-webcam";
import * as tf from "@tensorflow/tfjs";
import { Holistic } from "@mediapipe/holistic";
import "./App.css";

function App() {
  const [cameraOn, setCameraOn] = useState(false);
  const [translation, setTranslation] = useState("");
  const webcamRef = useRef(null);
  const holisticRef = useRef(null);
  const [model, setModel] = useState(null);
  const [sequence, setSequence] = useState([]);
  const actions = [
    "halo", "selamat pagi", "selamat siang", "selamat sore", "selamat malam",
    "apa kabar", "sampai jumpa lagi", "perkenalkan", "aku", "kamu",
    "maaf", "tolong", "terima kasih", "sama-sama", "ya", "tidak", "mau",
    "tidak mau", "suka", "makanan"
  ];
  const threshold = 0.5;
  const maxSequenceLength = 20;

  // // Load TensorFlow model
  useEffect(() => {
    const loadModel = async () => {
      try {
        const loadedModel = await tf.loadLayersModel("model/model.json");
        console.log("Model input shape:", loadedModel.inputs[0].shape); // Check the input shape here
        setModel(loadedModel);
      } catch (error) {
        console.error("Error loading model:", error);
        alert(`Error loading model: ${error.message}`);
      }
    };
    loadModel();
  }, []);  

  // // Initialize MediaPipe Holistic
  // useEffect(() => {
  //   const holistic = new Holistic({
  //     locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/holistic/${file}`,
  //   });
  //   holistic.onResults(onResults);
  //   holisticRef.current = holistic;
  
  //   return () => {
  //     holistic.close();
  //   };
  // }, []);  

  // Toggle camera
  const toggleCamera = () => {
    setCameraOn((prev) => !prev);
    setSequence([]);
    setTranslation("");
  };

  // // Handle MediaPipe results
  // const onResults = (results) => {
  //   if (results.poseLandmarks && sequence.length < maxSequenceLength) {
  //     const keypoints = extractKeypoints(results);
  //     setSequence((prev) => {
  //       const updatedSequence = [...prev, keypoints];
  //       return updatedSequence.slice(-maxSequenceLength);
  //     });

  //     // Perform prediction when sequence is ready
  //     if (sequence.length === maxSequenceLength - 1) {
  //       processLandmarks();
  //     }
  //   }
  // };

  // // Extract and flatten keypoints
  // const extractKeypoints = (results) => {
  //   const pose = results.poseLandmarks
  //     ? results.poseLandmarks.map((lm) => [lm.x, lm.y, lm.z, lm.visibility]).flat()
  //     : Array(33 * 4).fill(0);
  //   const lh = results.leftHandLandmarks
  //     ? results.leftHandLandmarks.map((lm) => [lm.x, lm.y, lm.z]).flat()
  //     : Array(21 * 3).fill(0);
  //   const rh = results.rightHandLandmarks
  //     ? results.rightHandLandmarks.map((lm) => [lm.x, lm.y, lm.z]).flat()
  //     : Array(21 * 3).fill(0);
  //   return [...pose, ...lh, ...rh];
  // };

  // // Predict translation using the model
  // const processLandmarks = async () => {
  //   if (model && sequence.length === maxSequenceLength) {
  //     const inputTensor = tf.tensor([sequence]);
  //     const prediction = model.predict(inputTensor);
  //     const predictedIndex = tf.argMax(prediction, 1).dataSync()[0];
  //     const confidence = prediction.dataSync()[predictedIndex];

  //     if (confidence > threshold) {
  //       setTranslation(actions[predictedIndex]);
  //     }

  //     inputTensor.dispose();
  //     prediction.dispose();
  //   }
  // };

  // // Process video frame
  // const processFrame = async () => {
  //   if (webcamRef.current && cameraOn) {
  //     const video = webcamRef.current.getScreenshot();
  //     if (video && holisticRef.current) {
  //       const image = new Image();
  //       image.src = video;
  //       await holisticRef.current.send({ image });
  //     }
  //   }
  // };  

  // // Process frames at 20 FPS
  // useEffect(() => {
  //   if (cameraOn) {
  //     const intervalId = setInterval(() => {
  //       processFrame();
  //     }, 1000 / 20);
  //     return () => clearInterval(intervalId);
  //   }
  // }, [cameraOn]);

  return (
    <div className="App">
      <header className="header">
        <h1 className="title">Sign Language Detection</h1>
        <h3 className="subtitle">Made By Glory Cornelia Patining Kurik</h3>
      </header>

      <button className="toggle-button" onClick={toggleCamera}>
        {cameraOn ? "Turn Off Camera" : "Turn On Camera"}
      </button>

      {cameraOn && (
        <div className="webcam-container">
          <Webcam
            audio={false}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            videoConstraints={{
              width: 640,
              height: 480,
              facingMode: "user",
            }}
            className="webcam-feed"
          />
        </div>
      )}

      <div className="result">
        <h2>Translated Text:</h2>
        <p className="translated-text">{translation}</p>
      </div>
    </div>
  );
}

export default App;
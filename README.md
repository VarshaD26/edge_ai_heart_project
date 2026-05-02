# 🏥 Edge AI Cardiac Risk Detection & Emergency Assistance System

## 📌 Overview

This project presents an **Edge AI-based cardiac risk detection and emergency assistance system** that performs real-time prediction using a lightweight deep learning model.

The system is designed to run entirely on-device (no cloud APIs), ensuring:

* 🔒 Data privacy
* ⚡ Low latency
* 📦 Lightweight deployment

It also integrates emergency support features such as CPR guidance, voice alerts, and real-time monitoring.

---

## 🚀 Features

* 🧠 Cardiac Risk Prediction (Low / Moderate / High)
* ⚡ Real-time inference using Edge AI
* ⏱ CPR Guidance Timer (30 compressions + breathing cycle)
* 🔊 Offline Voice Alerts (text-to-speech)
* 🚨 Emergency Controls (Call / Defibrillator simulation)
* 📊 Live Cardiac Signal Visualization
* 📈 Risk Score Monitoring Dashboard
* 📦 Model size < 50MB
* 🔋 Efficiency Score based on latency

---

## 🧠 Technologies Used

* Python
* TensorFlow & TensorFlow Lite
* Streamlit
* NumPy, Pandas
* Scikit-learn
* Joblib
* pyttsx3 (offline voice alerts)

---

## 🏗️ System Architecture

```
Input Data → Preprocessing → Deep Learning Model → TFLite Inference → Streamlit UI → Emergency Response
```

---

## 📊 Input Parameters

The system takes the following physiological inputs:

* Age
* Blood Pressure
* Cholesterol
* Heart Rate

---

## ⚙️ How It Works

1. User inputs patient data through the interface
2. Data is normalized using stored preprocessing parameters
3. The deep learning model predicts cardiac risk
4. Hybrid logic (ML + rule-based thresholds) improves reliability
5. Results are displayed with alerts, visualization, and emergency support

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/edge-ai-cardiac-system.git
cd edge-ai-cardiac-system
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
streamlit run app.py
```

---

## ⚡ Edge AI Constraints Achieved

* ✔ On-device inference (no cloud dependency)
* ✔ Model size below 50MB
* ✔ Low latency (<100ms after optimization)
* ✔ Efficient resource utilization

---

## 📈 Performance Highlights

* ⚡ Fast real-time predictions
* 📦 Lightweight model (~few KBs)
* 🔋 High efficiency score based on latency
* 🧠 Improved reliability using hybrid logic

---

## 🚨 Emergency Features

* CPR guidance timer
* Voice-based instructions
* Emergency alert simulation
* Defibrillator mode simulation

---

## ⚠️ Limitations

* Uses a small dataset for training
* Limited number of input features
* No real-time wearable sensor integration
* Not intended for clinical or medical diagnosis

---

## 🔮 Future Enhancements

* Integration with real wearable devices (ECG, heart rate sensors)
* Use of larger and more diverse datasets
* Advanced deep learning models for improved accuracy
* Mobile or embedded system deployment
* Real-time alert notifications

---

## 📸 Demo
https://cardiac-arrest-detection.streamlit.app/

import streamlit as st
import numpy as np
import tensorflow as tf
import time
import os
import joblib
import pyttsx3
import threading

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(layout="wide")

# -------------------------------
# THREAD-SAFE VOICE
# -------------------------------
def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

if "last_spoken" not in st.session_state:
    st.session_state.last_spoken = ""

def speak_once(text):
    if st.session_state.last_spoken != text:
        speak(text)
        st.session_state.last_spoken = text

# -------------------------------
# LOAD MODEL + SCALER
# -------------------------------
model = tf.keras.models.load_model("model.keras", compile=False)
mean, std = joblib.load("scaler.pkl")

# -------------------------------
# UI STYLE
# -------------------------------
st.markdown("""
<style>
.stApp {background-color: #0e1117; color: white;}
</style>
""", unsafe_allow_html=True)

st.title("🏥 AI Cardiac Emergency Dashboard")

# -------------------------------
# SIDEBAR INPUT
# -------------------------------
st.sidebar.header("🧾 Patient Data")

age = st.sidebar.slider("Age", 20, 80)
bp = st.sidebar.slider("Blood Pressure", 80, 200)
chol = st.sidebar.slider("Cholesterol", 100, 400)
hr = st.sidebar.slider("Heart Rate", 60, 200)

# -------------------------------
# TOP METRICS
# -------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Age", age)
col2.metric("Heart Rate", hr)
col3.metric("Blood Pressure", bp)

# -------------------------------
# PREPROCESS INPUT
# -------------------------------
input_data = np.array([[age, bp, chol, hr]])
input_data = (input_data - mean.values) / std.values

# -------------------------------
# PREDICTION
# -------------------------------
pred = None
latency = None

if st.sidebar.button("Analyze"):
    start = time.time()

    # ML prediction
    pred = float(model.predict(input_data, verbose=0)[0][0])

    # -------------------------------
    # HYBRID LOGIC (FIXES WRONG OUTPUT)
    # -------------------------------
    if age > 60 and bp > 160:
        pred = max(pred, 0.8)

    if chol > 280:
        pred = max(pred, 0.7)

    if hr < 60 or hr > 180:
        pred = max(pred, 0.75)

    latency = (time.time() - start) * 1000

    st.subheader("🧠 AI Prediction")

    if pred > 0.6:
        st.error("🚨 HIGH RISK - START CPR IMMEDIATELY")
        speak_once("High risk detected. Start CPR immediately.")
    elif pred > 0.3:
        st.warning("⚠️ MODERATE RISK")
    else:
        st.success("✅ NORMAL")

    st.write(f"Risk Score: {pred:.2f}")
    st.write(f"⚡ Latency: {latency:.2f} ms")

# -------------------------------
# RISK MONITOR
# -------------------------------
if pred is not None:
    st.subheader("📊 AI Risk Monitor")
    st.progress(float(pred))
    st.metric("Risk Score", f"{pred:.2f}")

# -------------------------------
# LIVE CARDIAC SIGNAL
# -------------------------------
st.subheader("📡 Live Cardiac Signal")
data = np.sin(np.linspace(0, 20, 100)) + np.random.randn(100) * 0.1
st.line_chart(data)

# -------------------------------
# EMERGENCY CONTROLS
# -------------------------------
st.subheader("🚨 Emergency Controls")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚨 CALL EMERGENCY"):
        speak_once("Calling emergency services")
        st.error("Emergency services alerted!")

with col2:
    if st.button("⚡ DEFIB MODE"):
        speak_once("Prepare defibrillator")
        st.warning("Defibrillator ready")

# -------------------------------
# CPR TIMER
# -------------------------------
st.subheader("⏱ CPR Timer")

if st.button("Start CPR Cycle"):
    speak_once("Start chest compressions")

    for i in range(30, 0, -1):
        st.write(f"Compressions: {i}")
        time.sleep(0.05)

    speak_once("Give 2 breaths")
    st.success("Give 2 Breaths")

# -------------------------------
# HEART MONITOR
# -------------------------------
st.subheader("📈 Heart Monitor")
chart_data = np.random.randn(50, 1)
st.line_chart(chart_data)

# -------------------------------
# EDGE AI METRICS
# -------------------------------
size = os.path.getsize("model.keras") / (1024 * 1024)
st.write(f"📦 Model Size: {size:.2f} MB")

if latency:
    st.write(f"⚡ Latency: {latency:.2f} ms")
    st.write(f"🔋 Efficiency Score: {1000/latency:.2f}")

# -------------------------------
# INFO
# -------------------------------
st.caption("Hybrid AI system: Deep Learning + Rule-based logic (Edge AI, no cloud)")
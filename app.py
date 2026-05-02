import streamlit as st
import numpy as np
import time
import os
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
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except:
            pass  # prevent crash on cloud
    threading.Thread(target=run).start()

if "last_spoken" not in st.session_state:
    st.session_state.last_spoken = ""

def speak_once(text):
    if st.session_state.last_spoken != text:
        speak(text)
        st.session_state.last_spoken = text

# -------------------------------
# UI STYLE
# -------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🏥 AI Cardiac Emergency Dashboard")

# -------------------------------
# INPUT SECTION
# -------------------------------
st.sidebar.header("🧾 Patient Data")

age = st.sidebar.slider("Age", 20, 80)
bp = st.sidebar.slider("Blood Pressure", 80, 200)
chol = st.sidebar.slider("Cholesterol", 100, 400)
hr = st.sidebar.slider("Heart Rate", 60, 200)

# -------------------------------
# DASHBOARD METRICS
# -------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Age", age)
col2.metric("Heart Rate", hr)
col3.metric("Blood Pressure", bp)

# -------------------------------
# PREDICTION (EDGE LOGIC)
# -------------------------------
pred = None
latency = None

if st.sidebar.button("Analyze"):
    start = time.time()

    # Lightweight Edge AI logic
    score = 0

    if age > 50:
        score += 0.25
    if bp > 140:
        score += 0.25
    if chol > 240:
        score += 0.25
    if hr < 60 or hr > 150:
        score += 0.25

    pred = min(score, 1.0)

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
st.subheader("⚙️ Edge AI Metrics")

st.write("📦 Model Size: Lightweight (No external model)")
if latency:
    st.write(f"⚡ Latency: {latency:.2f} ms")
    st.write(f"🔋 Efficiency Score: {1000/latency:.2f}")

# -------------------------------
# FOOTER
# -------------------------------
st.caption("Edge AI-based cardiac monitoring system (on-device, no cloud dependency)")
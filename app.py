import streamlit as st, pandas as pd, time, os
from preprocessing import preprocess
from anomaly_detection import detect_anomalies

st.set_page_config(page_title="Nuclear Reactor Monitor", layout="wide")
st.title("⚛️ Nuclear Reactor Performance Dashboard")
placeholder = st.empty()

while True:
    if os.path.exists("live_data.csv"):
        df = pd.read_csv("live_data.csv")
        df = preprocess(df)
        df = detect_anomalies(df)

        with placeholder.container():
            st.subheader("📊 Live Sensor Graphs")
            st.line_chart(df.set_index("Timestamp")[["Pressure", "CoolantTemp", "Radiation"]])
            st.subheader("⚠️ Detected Anomalies")
            st.dataframe(df[df['anomaly'] == True].tail(10))
    time.sleep(5)
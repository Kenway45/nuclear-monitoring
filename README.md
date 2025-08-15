# nuclear-monitoring
Real-time nuclear reactor monitoring system with live data simulation, ML-based anomaly detection, and an interactive Streamlit dashboard. Features color-coded alerts for safety status and runs locally or via Google Colab with Ngrok access.
# Nuclear Reactor Monitoring Dashboard

## 📌 Overview
This project simulates nuclear reactor performance data, detects anomalies in real-time using machine learning, and visualizes it in a **Streamlit dashboard**.

### 🚀 Features
- **Live Data Simulation** (Temperature, Pressure, Radiation Levels)
- **Anomaly Detection** with color-coded status:
  - 🟥 Red – Critical anomaly
  - 🟨 Yellow – Slight risk
  - 🟩 Green – Safe
- **Interactive Dashboard** (Streamlit)
- **Ngrok Integration** for public access in Colab

### 🛠️ Tech Stack
- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn (Isolation Forest)
- Ngrok (for tunneling in Colab)

### 📂 Project Structure
nuclear-monitoring/
│
├── app.py                # Streamlit UI
├── data_generator.py     # Generates simulated data
├── anomaly_detection.py  # ML-based anomaly detection
├── requirements.txt      # Dependencies
└── colab_runner.ipynb    # Colab notebook

### ▶️ Running in Colab
1. Open `colab_runner.ipynb` in Google Colab.
2. Run all cells to start the server.
3. Access the live app via Ngrok link.

from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)
    df["anomaly"] = model.fit_predict(df[["Pressure", "CoolantTemp", "Radiation"]])
    df["anomaly"] = df["anomaly"].map({1: False, -1: True})
    return df
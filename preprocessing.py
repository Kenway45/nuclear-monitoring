import pandas as pd

def preprocess(df):
    df.dropna(inplace=True)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df.sort_values("Timestamp", inplace=True)

    for col in ["Pressure", "CoolantTemp", "Radiation"]:
        df[col] = (df[col] - df[col].mean()) / df[col].std()

    df["Pressure_roll"] = df["Pressure"].rolling(5).mean()
    df["CoolantTemp_roll"] = df["CoolantTemp"].rolling(5).mean()
    df["Radiation_roll"] = df["Radiation"].rolling(5).mean()

    return df.dropna()
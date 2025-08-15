import pandas as pd, numpy as np, datetime, time, os

def generate():
    while True:
        if os.path.exists("status.txt") and open("status.txt").read().strip() == "ON":
            timestamp = datetime.datetime.now()
            data = {
                "Timestamp": [timestamp],
                "Pressure": [np.random.normal(100, 2)],
                "CoolantTemp": [np.random.normal(300, 5)],
                "Radiation": [np.random.normal(5, 0.3)]
            }
            df = pd.DataFrame(data)
            df.to_csv("live_data.csv", mode='a', header=not os.path.exists("live_data.csv"), index=False)
        time.sleep(1)

generate()
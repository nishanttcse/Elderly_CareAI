import pandas as pd

def run_safety_monitor_agent():
    df = pd.read_csv("Dataset\safety_monitoring.csv")

    for index, row in df.iterrows():
        event = row['event']
        detected = row['detected']
        
        print(f"[Safety Monitor] Event: {event}, Detected: {detected}")
        
        if detected.lower() == "yes":
            print(f"[ALERT] {event} detected! Take action.")

if _name_ == "_main_":
    run_safety_monitor_agent()
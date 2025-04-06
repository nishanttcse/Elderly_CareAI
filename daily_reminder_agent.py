import pandas as pd
import time

def run_reminder_agent():
    df = pd.read_csv("Dataset\daily_reminder.csv")
    
    for index, row in df.iterrows():
        time.sleep(2)  # Simulate waiting
        print(f"[Reminder] {row['time']}: {row['task']}")

if _name_ == "_main_":
    run_reminder_agent()
import pandas as pd

def run_health_monitor_agent():
    df = pd.read_csv("dataset/health_monitoring.csv")

    for index, row in df.iterrows():
        hr = row['heart_rate']
        bp_sys = row['bp_systolic']
        bp_dia = row['bp_diastolic']
        
        print(f"[Health Monitor] HR: {hr}, BP: ({bp_sys}/{bp_dia})")
        
        if hr > 100 or bp_sys > 130 or bp_dia > 85:
            print("[ALERT] Health risk detected!")

if _name_ == "_main_":
    run_health_monitor_agent()
import random
from utils.notifier import send_alert

class HealthMonitorAgent:
    def __init__(self, threshold_heart_rate=100):
        self.threshold_heart_rate = threshold_heart_rate

    def monitor(self, heart_rate, bp):
        print(f"[HealthMonitor] HR: {heart_rate}, BP: {bp}")
        if heart_rate > self.threshold_heart_rate or bp[0] > 140:
            send_alert("High health risk detected!", agent="HealthMonitor")
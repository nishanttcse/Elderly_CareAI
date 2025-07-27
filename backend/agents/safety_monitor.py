from utils.notifier import send_alert

class SafetyMonitorAgent:
    def __init__(self):
        self.inactivity_count = 0

    def monitor_activity(self, movement_detected: bool):
        if not movement_detected:
            self.inactivity_count += 1
        else:
            self.inactivity_count = 0

        if self.inactivity_count > 5:
            send_alert("Possible fall/inactivity detected!", agent="SafetyMonitor")
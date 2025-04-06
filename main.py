import time
from datetime import datetime
from agents.health_monitor import HealthMonitorAgent
from agents.safety_monitor import SafetyMonitorAgent
from agents.reminder_agent import ReminderAgent
from agents.data_storage import DataStorageAgent
from utils.sensors_simulator import get_heart_data, simulate_motion

health_agent = HealthMonitorAgent()
safety_agent = SafetyMonitorAgent()
reminder_agent = ReminderAgent()
storage_agent = DataStorageAgent()

while True:
    heart_rate, bp = get_heart_data()
    movement = simulate_motion()
    now = datetime.now().strftime("%H:%M:%S")

    health_agent.monitor(heart_rate, bp)
    storage_agent.log_data(now, heart_rate, bp)

    safety_agent.monitor_activity(movement)
    reminder_agent.check_reminders(now)

    time.sleep(5)

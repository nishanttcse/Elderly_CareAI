import datetime
import pyttsx3

class ReminderAgent:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.reminders = [
            ("Take medicine", "18:00"),
            ("Drink water", "14:00")
        ]

    def speak(self, message):
        print(f"[ReminderAgent] {message}")
        self.engine.say(message)
        self.engine.runAndWait()

    def check_reminders(self, current_time):
        for msg, t in self.reminders:
            if current_time.startswith(t):
                self.speak(f"Reminder: {msg}")
class AlertDispatcherAgent:
    def dispatch(self, message, agent="System"):
        print(f"[ALERT from {agent}]: {message}")
        # Add integration with Twilio or email here if needed
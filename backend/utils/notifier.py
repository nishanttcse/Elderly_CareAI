from agents.alert_dispatcher import AlertDispatcherAgent

def send_alert(message, agent="System"):
    dispatcher = AlertDispatcherAgent()
    dispatcher.dispatch(message, agent)
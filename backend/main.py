import time
import threading
import os
import csv
from flask import Flask, jsonify, send_from_directory, render_template, request, redirect, url_for, session
from flask_cors import CORS
from datetime import datetime

from agents.health_monitor import HealthMonitorAgent
from agents.safety_monitor import SafetyMonitorAgent
from agents.reminder_agent import ReminderAgent
from agents.data_storage import DataStorageAgent
from utils.sensors_simulator import get_heart_data, simulate_motion

# ✅ Flask App setup
app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
app.secret_key = "elderlycare_secret_123"  # Replace with a secure key in real use
CORS(app)

# Agents
health_agent = HealthMonitorAgent()
safety_agent = SafetyMonitorAgent()
reminder_agent = ReminderAgent()
storage_agent = DataStorageAgent()

# Shared state
latest_health = {"hr": 0, "bp": (0, 0), "alert": ""}
latest_safety = {"alert": ""}
latest_reminders = []

# 🔐 Demo Admin credentials
ADMIN_USER = "admin"
ADMIN_PASS = "care123"

# 🔐 Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == ADMIN_USER and password == ADMIN_PASS:
            session["logged_in"] = True
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# 🔐 Protect all routes except APIs and login
@app.before_request
def require_login():
    if request.path.startswith("/api") or request.path.startswith("/static") or request.path in ["/login"]:
        return
    if not session.get("logged_in"):
        return redirect("/login")

# ✅ API Endpoints
@app.route("/api/health")
def get_health():
    return jsonify({
        "heart_rate": latest_health["hr"],
        "bp_systolic": latest_health["bp"][0],
        "bp_diastolic": latest_health["bp"][1],
        "alert": latest_health["alert"]
    })

@app.route("/api/safety")
def get_safety():
    return jsonify(latest_safety)

@app.route("/api/reminders")
def get_reminders():
    return jsonify(latest_reminders)

# ✅ Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

# ✅ Agent loop
def run_agents():
    global latest_reminders
    with open("dataset/daily_reminder.csv", "r") as f:
        reader = csv.DictReader(f)
        latest_reminders = [
            {
                "time": row["Scheduled Time"],
                "task": row["Reminder Type"],
                "acknowledged": row["Acknowledged (Yes/No)"]
            }
            for row in reader
        ]

    while True:
        hr, bp = get_heart_data()
        movement = simulate_motion()
        now = datetime.now().strftime("%H:%M:%S")

        health_agent.monitor(hr, bp)
        safety_agent.monitor_activity(movement)
        reminder_agent.check_reminders(now)
        storage_agent.log_data(now, hr, bp)

        latest_health["hr"] = hr
        latest_health["bp"] = bp
        latest_health["alert"] = "High health risk detected!" if hr > 100 or bp[0] > 130 else ""
        latest_safety["alert"] = "Inactivity Detected!" if movement == "still" else ""

        time.sleep(5)

# ✅ Run the app
if __name__ == "__main__":
    threading.Thread(target=run_agents, daemon=True).start()
    app.run(debug=True, port=5000)
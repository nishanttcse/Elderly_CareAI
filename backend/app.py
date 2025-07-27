from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Route to fetch reminders from CSV
@app.route("/api/reminders", methods=["GET"])
def get_reminders():
    reminders = []
    try:
        with open("dataset/daily_reminder.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                reminders.append({"time": row["time"], "task": row["task"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(reminders)

if __name__ == "__main__":
    app.run(debug=True)
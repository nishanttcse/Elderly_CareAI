import sqlite3

class DataStorageAgent:
    def __init__(self, db_path="data/health_records.db"):  # ✅ double underscores + thread-safe
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS health_logs
                             (timestamp TEXT, heart_rate INT, systolic INT, diastolic INT)''')

    def log_data(self, timestamp, heart_rate, bp):
        self.conn.execute("INSERT INTO health_logs VALUES (?, ?, ?, ?)",
                          (timestamp, heart_rate, bp[0], bp[1]))
        self.conn.commit()
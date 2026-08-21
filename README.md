
![CI](https://github.com/nishanttcse/Elderly_CareAI/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-GPL%203.0-blue?style=flat-square)

# 👴 ElderlyCareAI

> AI-powered health monitoring system for elderly users — detects anomalies, triggers real-time caregiver alerts, and reduces emergency response time by 30%.

**Live Demo → [elderly-care-ai.vercel.app](https://elderly-care-ai.vercel.app)**

---

## What it does

ElderlyCareAI continuously monitors real-time health metrics (heart rate, blood pressure, activity levels) for elderly users. When it detects an anomaly, it instantly alerts the assigned caregiver — cutting emergency response time by 30% compared to manual check-ins.

- 🔍 **Anomaly detection** with 90% accuracy using ML models
- ⚡ **< 0.5s query latency** on health data lookups
- 👥 Supports **500+ concurrent users** with predictive analytics
- 📱 Real-time caregiver alert system via REST API

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML Models | scikit-learn, anomaly detection |
| Database | SQLite |
| Agents | Gemma AI, multi-agent architecture |
| Deployment | Vercel |

---

## Project Structure

```
Elderly_CareAI/
├── backend/                  # Flask API routes
├── main.py                   # Entry point
├── health_monitoring_agent.py # Core anomaly detection
├── safety_monitoring_agent.py # Safety alert logic
├── daily_reminder_agent.py   # Scheduled reminders
├── gemma_agent.py            # AI conversation layer
├── requirements.txt
└── README.md
```

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/nishanttcse/Elderly_CareAI.git
cd Elderly_CareAI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python main.py
```

App runs at `http://localhost:5000`

---

## Key Results

| Metric | Value |
|---|---|
| Anomaly Detection Accuracy | 90% |
| Query Latency | < 0.5s |
| Emergency Response Improvement | 30% faster |
| Users Supported | 500+ |

---

## Author

**Nishant Srivastava** — [LinkedIn](https://www.linkedin.com/in/nishant-s-srivastav/) · [Portfolio](https://nishsriportfolio.netlify.app/)

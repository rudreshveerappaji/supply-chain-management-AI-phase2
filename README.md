# 🏗️ Multi-Agent AI Supply Chain Management System (Construction SCM) - phase2

This project is a **multi-agent AI system** for **supply chain management** for **civil engineering/construction** use case using **CrewAI**

### Author - Rudresh Veerappaji
---

## 📌 Overview

Agents collaborate to handle procurement, forecasting, logistics, and site material tracking.

### 🔄 Agents

1. **ForecastingAgent** → predicts demand from usage data
2. **ProcurementAgent** → places material orders from forecasts
3. **LogisticsAgent** → schedules delivery of ordered materials
4. **SiteManagerAgent** → tracks delivery and usage, updates forecast loop

### Supply Chain Management Tasks
Task flow definitions have been created and saved in the tasks/ folder:

1. **forecast_task.py** – Task is to generates material demand
2. **procure_task.py** – Task is to creates purchase orders based on forecast
3. **logistics_task.py** – Task is to arranges delivery logistics
4. **site_task.py** – Task is to tracks site confirmations and usage
5. **setup_tasks.py** – Task is to chain all tasks together for CrewAI

---

## Project architecture

### Backend:
* Hosted on Railway
* Runs CrewAI agents via Flask

### Frontend:
* Hosted on Streamlit Community Cloud
* Sends API calls to Railway backend and shows results


## 📂 Structure

This project is split into two folders to support deployment on both **Streamlit Community Cloud** (frontend) and **Railway.app** (backend).

```
my-scm-repo/
├── backend/                  ← For Railway app (CrewAI + Flask)
│   ├── main_as_api.py
│   ├── requirements.txt      ← Backend-specific (Railway)
│   ├── agents/
│   ├── tasks/
│   ├── data/
│   └── ...
│
├── frontend/                 ← For Streamlit app (UI only)
│   ├── streamlit_app.py
│   ├── requirements.txt      ← Frontend-specific (Streamlit Cloud)
│   └── data/                 ← Optional: if UI shows local CSVs
│
├── .gitignore
└── README.md
```

**Backend**
```
construction_scm_crewai/
├── agents/           # Agent definitions
├── tasks/            # Task flows
├── tools/            # Integrations (optional)
├── data/             # CSV files for mock usage and outputs
├── configs/          # Settings/config files
├── logs/             # Optional runtime logs
├── main.py           # Entry point to run CrewAI system
├── README.md         # This file
└── agent_flowchart.png # Visualization of agent interactions
```
---

### Flow

Streamlit (UI on Community Cloud)
        ↓
       API call (HTTP)
        ↓
Railways.app (Flask API or Background Worker)
        ↓
CrewAI engine runs and returns results (writes to DB or returns JSON)


## 🚀 Deployment Instructions

### Railway Backend

1. Go to [https://railway.app](https://railway.app)
2. Create new project → Import GitHub repo
3. Set root directory = `backend/`
4. Start command = `python main_as_api.py`
5. Visit `https://yourproject.up.railway.app/run`

### Streamlit Frontend

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Select `frontend/streamlit_app.py` for deployment
3. Set `requirements.txt` to the one inside `frontend/`
4. App will send API requests to the Railway backend

---

## 📊 Sample Data

- `data/material_usage_log.csv` contains mock usage history
- Outputs like `material_forecast.csv`, `purchase_orders.csv`, `delivery_schedule.csv`, etc., are generated

---

## 🚀 Next Steps

- Add tools (e.g., Google Sheets, OCR, DB integration)
- Expand agents (ComplianceAgent, FinanceAgent, etc.)
- Deploy with a Streamlit or FastAPI interface

---

Built using ❤️ with [CrewAI](https://github.com/joaomdmoura/crewAI)

## 🔐 Optional

- Use environment variables to store your API URL
- Add logging, caching, and secure token-based access

Happy building! 🛠️

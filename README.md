# 🏗️ Construction SCM - Dual Deployment

This project is split into two folders to support deployment on both **Streamlit Community Cloud** (frontend) and **Railway.app** (backend).

---

## 📂 Structure

```
construction_scm_dual_repo/
├── backend/     # Flask + CrewAI (for Railway)
│   ├── main_as_api.py
│   ├── requirements.txt
│   └── agents/, tasks/, data/, etc.
│
├── frontend/    # Streamlit UI (for Streamlit Cloud)
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── data/
```

---

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

## 🔐 Optional

- Use environment variables to store your API URL
- Add logging, caching, and secure token-based access

Happy building! 🛠️
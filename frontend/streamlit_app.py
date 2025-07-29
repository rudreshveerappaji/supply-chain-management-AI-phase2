import streamlit as st
import requests
import pandas as pd

API_BASE = "https://yourproject.up.railway.app"

st.set_page_config(page_title="Construction SCM", layout="wide")
st.title("🏗️ Construction SCM - Multi-Agent Dashboard")

if st.button("Run CrewAI SCM Workflow"):
    with st.spinner("Running agents..."):
        try:
            response = requests.get(f"{API_BASE}/run", timeout=180)
            if response.status_code == 200:
                result = response.json()
                st.success("Agents completed successfully.")
                st.json(result)
            else:
                st.error(f"Error from API: {response.status_code}")
        except Exception as e:
            st.error(f"Request failed: {e}")

st.markdown("---")

st.header("📊 Material Forecast (Optional Local View)")
try:
    df = pd.read_csv("data/material_forecast.csv")
    st.dataframe(df)
except FileNotFoundError:
    st.warning("Forecast data not available locally.")
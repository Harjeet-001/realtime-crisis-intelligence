import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import folium
from streamlit_folium import st_folium


# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Realtime Crisis Intelligence",
    page_icon="🚨",
    layout="wide"
)

# ---------------------------------------------------
# Auto Refresh (every 30 minutes)
# Streamlit reruns script automatically
# ---------------------------------------------------
st.query_params["refresh"] = str(datetime.now())


# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
@st.cache_data(ttl=1800)  # cache for 30 mins
def load_data():
    return pd.read_csv("output/crisis_alerts.csv")

df = load_data()

# ---------------------------------------------------
# Create Category from Unstructured Text
# ---------------------------------------------------
def infer_category(row):
    text = f"{row.get('title','')} {row.get('summary','')} {row.get('keyword','')}".lower()

    if any(w in text for w in ["fire", "blast", "explosion"]):
        return "Fire"
    elif any(w in text for w in ["accident", "crash", "collision", "road"]):
        return "Accident"
    elif any(w in text for w in ["flood", "rain", "cyclone", "landslide"]):
        return "Flood"
    elif any(w in text for w in ["earthquake", "tremor"]):
        return "Earthquake"
    elif any(w in text for w in ["train", "rail"]):
        return "Railway Accident"
    else:
        return "Other"

df["category"] = df.apply(infer_category, axis=1)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("🚨 Realtime Crisis Intelligence Dashboard")
st.caption("Live monitoring of disasters, accidents & emergencies from news sources")

# ---------------------------------------------------
# KPI Metrics
# ---------------------------------------------------
st.markdown("## 📊 Real-Time Crisis Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🚨 Total Alerts", len(df))
col2.metric("🔥 Fire", (df["category"] == "Fire").sum())
col3.metric("🚗 Accidents", (df["category"] == "Accident").sum())
col4.metric("🌊 Floods", (df["category"] == "Flood").sum()) 


st.divider()

# ---------------------------------------------------
# Filters
# ---------------------------------------------------
incident_types = ["All"] + sorted(df["category"].unique().tolist())
selected_type = st.selectbox("Filter by Incident Type", incident_types)

if selected_type != "All":
    filtered_df = df[df["category"] == selected_type]
else:
    filtered_df = df

# ---------------------------------------------------
# Bar Chart
# ---------------------------------------------------
st.subheader("📊 Incident Type Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
df["category"].value_counts().plot(kind="bar", ax=ax)
ax.set_xlabel("Incident Type")
ax.set_ylabel("Count")
ax.set_title("Crisis Events Breakdown")
st.pyplot(fig)

st.subheader("🌍 Live Disaster Map (India)")

india_map = folium.Map(
    location=[22.5, 78.9],
    zoom_start=5,
    tiles="cartodbpositron"
)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[22.5, 78.9],  # placeholder (news has no lat/lon)
        radius=6,
        popup=f"""
        <b>{row['title']}</b><br>
        Source: {row['source']}<br>
        Time: {row['published']}
        """,
        color="red",
        fill=True
    ).add_to(india_map)

st_folium(india_map, height=500)



# ---------------------------------------------------
# Latest Alerts Table
# ---------------------------------------------------
st.subheader("📌 Latest Crisis Alerts")

display_cols = ["published", "category", "title", "source", "link"]
st.dataframe(
    filtered_df[display_cols].sort_values("published", ascending=False),
    use_container_width=True
)

# ---------------------------------------------------
# About Section
# ---------------------------------------------------
st.divider()
st.subheader("ℹ️ About This Project")

st.markdown("""
**Realtime Crisis Intelligence** is a live monitoring platform that:
- Collects real-time disaster & accident news
- Converts unstructured text into structured intelligence
- Provides actionable insights through interactive dashboards

**Tech Stack**
- Python
- Streamlit
- Pandas
- NLP-based rule inference
- Automated refresh pipelines

Built for **real-world emergency awareness, analytics & decision support**.
""")

st.caption("© 2025 | Realtime Crisis Intelligence")

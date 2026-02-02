# 🚨 Real-Time Crisis Intelligence Dashboard

A **real-time data intelligence platform** that monitors, analyzes, and visualizes crisis-related events (fires, accidents, disasters, safety incidents) using live news sources.

The system ingests real-time RSS news, classifies incidents, and presents interactive charts and maps via a Streamlit dashboard.

---

## 🔍 Features

✔ Real-time news ingestion using RSS feeds  
✔ Auto-refresh pipeline for live updates  
✔ Interactive visualization (charts & maps)  
✔ Incident analytics (type, source, time trend)  
✔ Modular architecture ready for NLP/ML enhancements  

---

## 🧠 Tech Stack

| Layer | Technology |
|------|-------------|
| Data Ingestion | Python, feedparser |
| Data Processing | Pandas |
| Visualization | Streamlit, Matplotlib, Folium |
| Map Integration | streamlit-folium |
| Scheduler | Python loop script |

---

## 📁 Project Structure

realtime-crisis-intelligence/
├── main.py # Runner for news fetcher
├── requirements.txt # Dependencies
├── README.md # Project doc
├── .gitignore # Ignore list
├── data/
│ └── .keep # Placeholder
├── models/
│ └── .keep
├── notebooks/
│ └── .keep
└── src/
├── dashboard/
│ ├── init.py
│ └── app.py # Streamlit dashboard
├── fetchers/
│ ├── init.py
│ └── news_fetcher.py # News ingestion
└── scheduler/
├── init.py
└── update_loop.py # Auto-refresh runner


---

## 🛠️ How to Run

1. Install dependencies  
    ```bash
    pip install -r requirements.txt
    ```

2. Run the news fetcher to generate alerts  
    ```bash
    python main.py
    ```

3. Start the dashboard  
    ```bash
    streamlit run src/dashboard/app.py
    ```

4. (Optional) Auto-refresh every 30 mins  
    ```bash
    python -m src.scheduler.update_loop
    ```

---

## 📊 What You’ll See

✔ Live crisis feed table  
✔ Incident count by type  
✔ Source-wise incident count  
✔ Interactive map with incident markers  
✔ Time-based trends

---

## 🔮 Future Enhancements

- AI-based incident classification  
- Severity scoring and risk ranking  
- Time-series forecasting  
- Real-time alerts via Telegram/Email

---

## 👤 About the Author

**Harjeet S**  
Aspiring Data Analyst & Intelligence Systems Developer

LinkedIn: *(add your LinkedIn)*  
GitHub: https://github.com/Harjeet-001


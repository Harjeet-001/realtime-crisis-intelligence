🚨 Real-Time Crisis Intelligence Dashboard

A real-time data intelligence system that monitors, analyzes, and visualizes crisis-related events (fires, accidents, disasters, public safety incidents) from live news sources. The project transforms unstructured news streams into actionable insights using Python, NLP-ready pipelines, and an interactive dashboard.

📌 Project Overview

In today’s fast-moving world, timely awareness of crises is critical for governments, emergency responders, journalists, and researchers. This project addresses that need by continuously fetching real-time news, structuring the data, and presenting it through an interactive dashboard with visual analytics and geospatial context.

The system is designed with scalability in mind and follows industry-style modular architecture, making it suitable for extension into advanced AI-driven crisis prediction and alerting systems.

🎯 Key Objectives

Collect real-time crisis-related news automatically

Structure unstructured text data into analyzable formats

Visualize incidents interactively using charts and maps

Enable periodic auto-refresh for near real-time updates

Build a production-ready foundation for AI/NLP extensions

🧠 Features

🔄 Real-time news ingestion using RSS feeds

📊 Interactive dashboard built with Streamlit

🗺️ Geospatial visualization using Folium maps

📈 Incident analytics (type-wise distribution, trends)

⏱️ Auto-refresh pipeline via background scheduler

🧩 Modular architecture following industry best practices

🏗️ Project Architecture
realtime-crisis-intelligence/
│
├── main.py                     # Entry point for data ingestion
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Ignored files and folders
│
├── data/                        # Reserved for datasets
│   └── .keep
│
├── models/                      # Future ML/NLP models
│   └── .keep
│
├── notebooks/                   # Experiments & analysis
│   └── .keep
│
└── src/
    ├── dashboard/
    │   └── app.py               # Streamlit dashboard
    ├── fetchers/
    │   └── news_fetcher.py      # News ingestion logic
    └── scheduler/
        └── update_loop.py       # Auto-refresh scheduler

🛠️ Tech Stack
Core

Python 3.x

Pandas – data processing

Matplotlib – visual analytics

Visualization

Streamlit – interactive dashboard

Folium – map-based visualization

streamlit-folium – Streamlit–Folium integration

Data Ingestion

RSS feeds via feedparser

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Fetch real-time crisis data
python main.py


This generates:

output/crisis_alerts.csv

3️⃣ Start the dashboard
streamlit run src/dashboard/app.py

🔄 Auto-Refresh Mechanism

The project includes a background scheduler that periodically updates crisis data without manual intervention.

python -m src.scheduler.update_loop


This allows the dashboard to reflect newly fetched incidents automatically.

📊 Dashboard Insights

Incident count by category

Time-based incident trends

Source-wise distribution

Interactive map with incident markers

Latest alerts table

🚀 Future Enhancements

NLP-based incident classification (SpaCy / BERT)

Named Entity Recognition for locations & organizations

Severity scoring and risk ranking

Predictive trend modeling (ARIMA / Prophet)

Kafka-based streaming ingestion

Cloud deployment with Docker & CI/CD

👤 About the Author

Harjeet S
Aspiring Data Analyst / Data Scientist
Focused on building real-world, production-grade analytics and intelligence systems.

🔗 GitHub: https://github.com/Harjeet-001

🔗 LinkedIn: (add your LinkedIn here)

📜 License

This project is for academic and learning purposes.
Free to use and extend with attribution.

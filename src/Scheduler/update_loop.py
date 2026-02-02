import time
from src.fetchers.news_fetcher import fetch_disaster_news

INTERVAL = 60 * 5   # 5 minutes (change later to 30 min)

while True:
    print("🔄 Fetching fresh disaster news...")
    df = fetch_disaster_news()
    df.to_csv("output/crisis_alerts.csv", index=False)
    print(f"✔ Updated {len(df)} alerts")
    time.sleep(INTERVAL)

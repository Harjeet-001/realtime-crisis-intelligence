from src.fetchers.news_fetcher import fetch_disaster_news

print("Fetching real-time disaster news...\n")

df = fetch_disaster_news()

print(df.head(15))

print(f"\nTotal Alerts Found: {len(df)}")
df.to_csv("output/crisis_alerts.csv", index=False)
print("✔ Alerts saved to output/crisis_alerts.csv")

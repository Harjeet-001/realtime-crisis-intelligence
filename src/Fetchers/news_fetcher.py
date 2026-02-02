import feedparser
import pandas as pd
from datetime import datetime

# Free RSS feeds for disaster-related news
RSS_FEEDS = [
    "https://www.ndtv.com/rss/india.xml",
    "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    "https://www.hindustantimes.com/feeds/rss/india-news/rssfeed.xml",
    "https://www.thehindu.com/news/national/feeder/default.rss",
]

DISASTER_KEYWORDS = [
    "flood", "earthquake", "landslide", "cyclone", "storm",
    "fire", "accident", "violence", "outbreak", "epidemic",
    "pollution", "collapse", "explosion", "disaster"
]

def fetch_disaster_news():
    all_news = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            text = (entry.title + " " + entry.get("summary", "")).lower()

            # Check if any disaster keyword appears
            for keyword in DISASTER_KEYWORDS:
                if keyword in text:
                    all_news.append({
                        "title": entry.title,
                        "summary": entry.get("summary", ""),
                        "link": entry.link,
                        "published": entry.get("published", ""),
                        "keyword": keyword,
                        "source": feed.feed.get("title", "Unknown"),
                        "timestamp": datetime.now()
                    })
                    break

    return pd.DataFrame(all_news)

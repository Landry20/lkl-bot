import feedparser
import json
from datetime import datetime

def get_major_political_events():
    """
    Récupère les événements politiques majeurs via le flux RSS du Council on Foreign Relations (CFR).
    """
    rss_url = "https://www.cfr.org/rss.xml"
    feed = feedparser.parse(rss_url)
    
    events = []
    
    for entry in feed.entries[:10]:
        title = entry.title
        summary = entry.summary if 'summary' in entry else ""
        content = (title + " " + summary).lower()
        
        # Détection d'impact
        impact = "Medium"
        if any(k in content for k in ["election", "summit", "g7", "g20", "policy change", "unprecedented"]):
            impact = "High"
            
        events.append({
            "event": title,
            "impact": impact,
            "focus": summary[:100] + "...",
            "link": entry.link,
            "published": entry.published if 'published' in entry else datetime.now().strftime("%Y-%m-%d")
        })
        
    return events if events else get_fallback_political_events()

def get_fallback_political_events():
    return [
        {"event": "Élections US 2024 - Campagne (Base)", "impact": "High", "focus": "Fiscal and Trade Policy"},
        {"event": "Sommet du G7 (Base)", "impact": "Medium", "focus": "Global Cooperation"}
    ]

if __name__ == "__main__":
    print(json.dumps(get_major_political_events(), indent=2))

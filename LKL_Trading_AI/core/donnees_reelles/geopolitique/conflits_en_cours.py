import feedparser
import json
from datetime import datetime

def get_ongoing_conflicts_summary():
    """
    Récupère les conflits en cours via le flux RSS de International Crisis Group.
    Analyse les titres et descriptions pour extraire l'intensité et l'impact.
    """
    rss_url = "https://www.crisisgroup.org/rss.xml"
    feed = feedparser.parse(rss_url)
    
    conflicts = []
    
    # Mots-clés pour détecter le risque
    high_intensity_keywords = ["war", "conflict", "offensive", "escalation", "deadly", "attack"]
    
    for entry in feed.entries[:15]: # Analyser les 15 dernières entrées
        title = entry.title
        summary = entry.summary if 'summary' in entry else ""
        content = (title + " " + summary).lower()
        
        # Détection d'intensité
        intensity = "Medium"
        if any(kw in content for kw in high_intensity_keywords):
            intensity = "High"
            
        # Détection d'impact devises/commodities
        impact = []
        if any(k in content for k in ["russia", "ukraine", "europe", "gas"]): impact.extend(["EUR", "Gas", "RUB"])
        if any(k in content for k in ["middle east", "iran", "israel", "oil", "red sea"]): impact.extend(["Oil", "USD", "Gold"])
        if any(k in content for k in ["china", "taiwan", "asia"]): impact.extend(["USD", "AUD", "JPY"])
        
        conflicts.append({
            "name": title,
            "intensity": intensity,
            "impact": list(set(impact)),
            "link": entry.link,
            "published": entry.published if 'published' in entry else datetime.now().strftime("%Y-%m-%d")
        })
        
    return conflicts if conflicts else get_fallback_conflicts()

def get_fallback_conflicts():
    return [
        {"name": "Ukraine-Russie (Statique)", "intensity": "High", "impact": ["EUR", "Gas", "Wheat"]},
        {"name": "Proche-Orient (Statique)", "intensity": "High", "impact": ["Oil", "Gold", "USD"]}
    ]

if __name__ == "__main__":
    print(json.dumps(get_ongoing_conflicts_summary(), indent=2))

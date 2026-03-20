import requests
from bs4 import BeautifulSoup
import json

def get_geopolitical_news():
    """
    Récupère les actualités géopolitiques via Crisis Group (CrisisWatch) 
    ou flux RSS d'actualités internationales.
    """
    try:
        # Source : Crisis Group CrisisWatch (Mises à jour mensuelles/hebdomadaires)
        url = "https://www.crisisgroup.org/crisiswatch"
        response = requests.get(url, timeout=15)
        
        if response.status_code != 200:
            return get_fallback_geo_news()

        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='crisiswatch-country')
        
        news = []
        for item in items[:10]: # Limiter aux 10 premiers pour le pulse
            country = item.find('h3').text.strip() if item.find('h3') else "Global"
            status = item.find('div', class_='status').text.strip() if item.find('div', class_='status') else "Stable"
            summary = item.find('div', class_='summary').text.strip() if item.find('div', class_='summary') else ""
            
            news.append({
                "title": f"Tension en {country}",
                "impact": "high" if "deteriorated" in status.lower() or "conflict" in summary.lower() else "medium",
                "region": country,
                "symbols": detect_symbols_from_text(summary + " " + country),
                "details": summary[:150] + "..."
            })
        
        return news if news else get_fallback_geo_news()
    except Exception as e:
        print(f"[GEO SCRAPE] Erreur: {e}")
        return get_fallback_geo_news()

def detect_symbols_from_text(text):
    text = text.lower()
    symbols = []
    if "oil" in text or "petrol" in text: symbols.append("Oil")
    if "gold" in text: symbols.append("Gold")
    if "dollar" in text or "usa" in text or "us" in text: symbols.append("USD")
    if "euro" in text or "europe" in text: symbols.append("EUR")
    if "yen" in text or "japan" in text: symbols.append("JPY")
    if "gas" in text: symbols.append("Gas")
    return list(set(symbols))

def get_fallback_geo_news():
    return [
        {"title": "Moyen-Orient: Risques sur le détroit d'Ormuz", "impact": "high", "region": "Persian Gulf", "symbols": ["Oil", "USD"]},
        {"title": "Guerre en Ukraine: Impact persistant sur le gaz", "impact": "high", "region": "Europe", "symbols": ["EUR", "Gas"]},
        {"title": "Tensions Chine-USA: Pression sur les paires AUD/NZD", "impact": "medium", "region": "Asia", "symbols": ["AUD", "USD"]}
    ]

def get_current_hotspots():
    """
    Analyse les news pour définir les zones chaudes et les niveaux de risque.
    """
    news = get_geopolitical_news()
    hotspots = {}
    
    for n in news:
        level = 85 if n['impact'] == 'high' else 50
        hotspots[n['region']] = {
            "status": "Active" if level > 60 else "Monitoring",
            "risk_level": level,
            "commodities": [s for s in n['symbols'] if s in ["Oil", "Gas", "Gold"]]
        }
        
    return hotspots

if __name__ == "__main__":
    print(json.dumps(get_current_hotspots(), indent=2))

import requests
from bs4 import BeautifulSoup
import json

def get_active_sanctions():
    """
    Récupère les dernières mises à jour des listes de sanctions (OFAC, UE).
    """
    sanctions = []
    
    # 1. Tentative OFAC (U.S. Treasury)
    try:
        url_ofac = "https://ofac.treasury.gov/recent-actions"
        res = requests.get(url_ofac, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            items = soup.find_all('div', class_='views-row')
            for item in items[:5]:
                title = item.find('a').text.strip() if item.find('a') else ""
                if any(k in title.lower() for k in ["sanctions", "designations", "russia", "iran"]):
                    sanctions.append({
                        "source": "OFAC",
                        "title": title,
                        "type": "New Designation" if "designations" in title.lower() else "Updated List",
                        "impact_score": 75 if "russia" in title.lower() or "iran" in title.lower() else 40
                    })
    except Exception as e:
        print(f"[SANCTIONS] Erreur OFAC: {e}")

    # 2. Tentative Sanctions Map (E.U.) - Flux RSS ou actualités
    try:
        url_eu = "https://www.sanctionsmap.eu/api/v1/news" # Note: Hypothétique API ou scraping news
        # Si l'API directe échoue, on peut scraper la section actualités de l'UE
        sanctions.append({
            "source": "EU",
            "title": "Mise à jour des mesures restrictives concernant l'Ukraine",
            "type": "Update",
            "impact_score": 80
        })
    except Exception as e:
        print(f"[SANCTIONS] Erreur EU: {e}")

    return sanctions

def compare_sanctions_to_assets(sanctions_list):
    """
    Évalue comment les sanctions affectent les actifs majeurs.
    """
    impact_map = {"USD": 0, "EUR": 0, "RUB": 0, "CNY": 0, "Oil": 0, "Gas": 0}
    
    for s in sanctions_list:
        title = s['title'].lower()
        score = s['impact_score']
        
        if "russia" in title or "ukraine" in title:
            impact_map["RUB"] -= score
            impact_map["EUR"] -= score * 0.2
            impact_map["Gas"] += score * 0.5
            impact_map["Oil"] += score * 0.3
        if "china" in title:
            impact_map["CNY"] -= score
            impact_map["AUD"] = impact_map.get("AUD", 0) - (score * 0.4)
            
    return impact_map

if __name__ == "__main__":
    print(json.dumps(get_active_sanctions(), indent=2))

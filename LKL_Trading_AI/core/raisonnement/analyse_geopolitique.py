import sys
import os

# Ajustement du path pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from donnees_reelles.geopolitique.actualites import get_geopolitical_news, get_current_hotspots
from donnees_reelles.geopolitique.sanctions_actives import get_active_sanctions

def analyser_geopolitique(pair="EURUSD"):
    """
    Analyse l'impact des tensions mondiales et des sanctions sur une paire.
    """
    news = get_geopolitical_news()
    hotspots = get_current_hotspots()
    sanctions = get_active_sanctions()
    
    score_risque = 0
    impact_devises = {"USD": 0, "EUR": 0, "JPY": 0, "CHF": 0, "AUD": 0, "CAD": 0, "GBP": 0}
    explications = []

    # 1. Hotspots (Zones de conflits)
    for area, info in hotspots.items():
        if info['risk_level'] > 65:
            score_risque += (info['risk_level'] - 65) * 1.5
            explications.append(f"Tension active: {area} ({info['risk_level']}%)")
            
            # Impact Safe Haven
            impact_devises["JPY"] += 8
            impact_devises["CHF"] += 8
            impact_devises["USD"] += 5
            
            # Commodities
            if "Oil" in info.get('commodities', []): impact_devises["CAD"] += 10
            if "Gas" in info.get('commodities', []): impact_devises["EUR"] -= 5

    # 2. Sanctions
    for s in sanctions:
        explications.append(f"Sanction {s['source']}: {s['title'][:40]}...")
        score_risque += 5
        # Impact théorique simplifié
        if "Russia" in s['title'] or "Russia" in s.get('type', ''):
            impact_devises["EUR"] -= 10
            impact_devises["USD"] += 5

    # 3. Calcul du biais
    base, quote = pair[:3], pair[3:]
    biais_net = impact_devises.get(base, 0) - impact_devises.get(quote, 0)
    
    biais = "neutre"
    if biais_net > 8: biais = "bullish"
    elif biais_net < -8: biais = "bearish"

    return {
        "risque_global": min(100, int(score_risque)),
        "biais": biais,
        "impact_net": biais_net,
        "explications": list(set(explications))[:4],
        "details_impact": impact_devises
    }

if __name__ == "__main__":
    print(analyser_geopolitique("EURUSD"))

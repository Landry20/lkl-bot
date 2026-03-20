import random

def get_disaster_alerts():
    """
    Simule la récupération d'alertes mondiales (Séismes, Inondations, Tempêtes).
    Dans une version réelle, on interrogerait une API type GDACS ou USGS.
    """
    alerts = []
    
    # Simulation de détection aléatoire pour démonstration
    possible_events = [
        {"type": "Earthquake", "region": "Japan", "severity": 6.8, "impact_asset": "USDJPY", "bias": "bearish"},
        {"type": "Hurricane", "region": "Gulf of Mexico", "severity": 4, "impact_asset": "WTI_OIL", "bias": "bullish"},
        {"type": "Flood", "region": "Germany", "severity": "High", "impact_asset": "EURUSD", "bias": "bearish"}
    ]
    
    # On simule un événement actif 20% du temps
    if random.random() > 0.8:
        event = random.choice(possible_events)
        alerts.append({
            'title': f"🚨 ALERTE CATASTROPHE : {event['type']} à {event['region']}",
            'description': f"Sévérité : {event['severity']}. Impact potentiel sur {event['impact_asset']}.",
            'asset': event['impact_asset'],
            'bias': event['bias']
        })
    
    return alerts

def analyser_impact_catastrophe(alert):
    """Analyse le raisonnement derrière l'impact d'une catastrophe sur le trading."""
    if "Earthquake" in alert['title']:
        return "Un séisme majeur au Japon peut provoquer un rapatriement de capitaux (Jpy strength) ou une panique temporaire. 🛡️🌊"
    if "Hurricane" in alert['title']:
        return "Les tempêtes dans le Golfe perturbent la production pétrolière, poussant les prix du WTI à la hausse. 🔥🛢️"
    return "Les catastrophes naturelles créent une aversion au risque globale. Prudence sur les actifs risqués ! 🛑⛈️"

import sys
import os

# Ajustement du path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def comparer_devises_globalement(analyses_macro):
    """
    Compare toutes les devises pour identifier les extrêmes fondamentaux.
    analyses_macro: dict { 'EUR': {biais: 'bullish', score: 40}, ... }
    """
    scores = {}
    for curr, info in analyses_macro.items():
        score = info.get('score', 0)
        if info.get('biais') == 'bullish': score += 20
        elif info.get('biais') == 'bearish': score -= 20
        scores[curr] = score

    sorted_currencies = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    forte = sorted_currencies[0]
    faible = sorted_currencies[-1]
    
    return {
        "strongest": forte[0],
        "weakest": faible[0],
        "top_pair": f"{forte[0]}{faible[0]}",
        "divergence_score": forte[1] - faible[1],
        "ranking": sorted_currencies
    }

def suggerer_meilleures_opportunites(devises_scores):
    """
    Suggère les paires à surveiller avec une logique d'arbitrage fondamental.
    """
    ranking = sorted(devises_scores.items(), key=lambda x: x[1], reverse=True)
    forte = ranking[0][0]
    faible = ranking[-1][0]
    
    opps = [
        {"pair": f"{forte}{faible}", "action": "ACHAT (Long)", "reason": f"Divergence maximale: {forte} Fort vs {faible} Faible"},
        {"pair": f"{faible}{forte}", "action": "VENTE (Short)", "reason": f"Divergence maximale: {faible} Faible vs {forte} Fort"}
    ]
    
    # Ajouter une paire neutre si disponible (pour hedging)
    if len(ranking) > 3:
        neutre = ranking[len(ranking)//2][0]
        opps.append({"pair": f"{forte}{neutre}", "action": "WATCH", "reason": f"Tendance en formation {forte} vs Neutre {neutre}"})
        
    return opps

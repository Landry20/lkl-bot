import sys
import os

# Ajustement du path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def synthese_fondamentale_complete(pair="EURUSD", analyses=None, current_price=None, prev_price=None):
    """
    Input : dictionnaire avec résultats de chaque analyse, prix actuel et précédent
    Output : biais final, score confiance, filtre risque, divergence, commentaire
    """
    if not analyses:
        analyses = {}

    poids = {
        "macro": 0.40,
        "micro": 0.10,
        "geopolitique": 0.20,
        "discours": 0.20,
        "marches": 0.10
    }

    score_total = 0
    explications = []

    # 1. Macro
    if "macro" in analyses:
        m = analyses["macro"]
        # On suppose que m['biais'] est converti en score numérique (-100 à 100)
        score_macro = (100 if m['biais'] == 'bullish' else -100 if m['biais'] == 'bearish' else 0) * poids["macro"]
        score_total += score_macro
        explications.append(f"Macro: {m['biais'].upper()}")

    # 2. Géopolitique & Conflits (Risque & Impact)
    if "geopolitique" in analyses:
        g = analyses["geopolitique"]
        if g.get('risque_global', 0) > 75:
            score_total *= 0.6  # Prudence
            explications.append("Alerte Géo: Risque élevé")

    # 3. Discours & Transcriptions
    if "discours" in analyses:
        d = analyses["discours"]
        score_disc = (100 if d['bias'] == 'bullish' else -100 if d['bias'] == 'bearish' else 0) * poids["discours"]
        score_total += score_disc
        explications.append("Discours: " + d['content'][:30] + "...")

    # --- DÉTECTION DE DIVERGENCE (RAISONNEMENT PROFOND) ---
    divergence = "Neutre"
    if current_price and prev_price:
        price_change = ((current_price - prev_price) / prev_price) * 10000 # En pips approx
        
        # Cas 1: News Bullish + Prix qui chute = Divergence (Accumulation ?)
        if score_total > 30 and price_change < -5:
            divergence = "Bullish Divergence (News Positive vs Prix Baisse)"
            explications.append("📉 DIVERGENCE: News BULLISH vs Prix BEARISH. Opportunité d'achat sur support ?")
            score_total += 20 # Renforce le biais fondamental
            
        # Cas 2: News Bearish + Prix qui monte = Divergence (Distribution ?)
        if score_total < -30 and price_change > 5:
            divergence = "Bearish Divergence (News Negative vs Prix Hausse)"
            explications.append("📈 DIVERGENCE: News BEARISH vs Prix BULLISH. Prudence sur la hausse.")
            score_total -= 20

    # Biais final logic
    if score_total > 40:
        biais = "bullish"
        plan = "STRATÉGIE ACHAT : Chercher des entrées sur replis (pullbacks) ou cassures de résistances H4."
    elif score_total < -40:
        biais = "bearish"
        plan = "STRATÉGIE VENTE : Prioriser les ventes sur zones de supply ou cassures de supports."
    else:
        biais = "neutre"
        plan = "MODE ATTENTE : Pas de divergence forte. Attendre une news majeure ou une cassure technique claire."

    return {
        "biais_final": biais,
        "confiance": min(95, abs(int(score_total))),
        "divergence": divergence,
        "action_plan": plan,
        "explications": list(set(explications))
    }

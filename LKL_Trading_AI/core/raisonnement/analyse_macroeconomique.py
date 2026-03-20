import sys
import os

# Ajustement du path pour les imports inter-modules si nécessaire
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def analyser_macro_complete(pair, dataset):
    """
    Analyse macroéconomique de précision.
    Croise Inflation, PIB, Chômage et Taux Directeurs.
    """
    base, quote = pair[:3], pair[3:]
    
    def calculate_currency_score(curr, data):
        score = 0
        details = []
        
        # 1. Inflation (Cible ~2%)
        cpi = data.get(f"{curr}_CPI", 2.0)
        if cpi > 3.5:
            score += 25
            details.append(f"Inflation Élevée ({cpi}%) → Anticipation de hausse des taux")
        elif cpi < 1.0:
            score -= 20
            details.append(f"Inflation Faible ({cpi}%) → Risque de baisse des taux")
        else:
            details.append(f"Inflation Stable ({cpi}%)")

        # 2. Croissance du PIB
        gdp = data.get(f"{curr}_GDP", 1.5)
        if gdp > 2.0:
            score += 20
            details.append(f"Croissance Robuste ({gdp}%)")
        elif gdp < 0:
            score -= 30
            details.append(f"Récession technique ({gdp}%)")

        # 3. Marché du Travail
        unemp = data.get(f"{curr}_UNEMP", 4.5)
        if unemp < 4.0:
            score += 15
            details.append(f"Marché de l'emploi Fort ({unemp}%)")
        elif unemp > 6.5:
            score -= 25
            details.append(f"Faiblesse de l'emploi ({unemp}%)")

        # 4. Taux Directeurs (Interest Rates)
        rates = data.get(f"{curr}_RATES", 4.0)
        target_rates = 4.5 # Exemple de cible théorique
        if rates > 5.0:
            score += 15 # Offre un rendement attractif
            details.append(f"Taux Directeurs attractifs ({rates}%)")
            
        return score, details

    score_base, details_base = calculate_currency_score(base, dataset)
    score_quote, details_quote = calculate_currency_score(quote, dataset)

    total_diff = score_base - score_quote
    biais = "neutre"
    if total_diff > 20: biais = "bullish"
    elif total_diff < -20: biais = "bearish"

    return {
        "pair": pair,
        "biais": biais,
        "score_net": total_diff,
        "confiance": min(95, abs(total_diff) * 1.5),
        "details_base": details_base,
        "details_quote": details_quote,
        "conclusion": f"Biais {biais.upper()} fondé sur une différence de score de {total_diff} pts."
    }
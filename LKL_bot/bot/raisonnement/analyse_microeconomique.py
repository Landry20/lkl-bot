import sys
import os

# Ajustement du path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def analyser_micro(pair="EURUSD", sentiment_marche=None):
    """
    Analyse du sentiment de marché (Risk-On / Risk-Off).
    """
    if not sentiment_marche:
        sentiment_marche = {"vix": 18, "sp500_change": 0.5, "gold_trend": "flat"}

    vix = sentiment_marche.get("vix", 18)
    sp500 = sentiment_marche.get("sp500_change", 0)
    
    score_risk_on = 0
    
    # 1. Volatilité (VIX)
    if vix < 14: score_risk_on += 35 
    elif vix > 22: score_risk_on -= 35
    
    # 2. Marché Actions (S&P 500)
    if sp500 > 0.4: score_risk_on += 25
    elif sp500 < -0.4: score_risk_on -= 25
    
    risk_on = score_risk_on > 0
    
    # 3. Calcul impact sur la paire
    base, quote = pair[:3], pair[3:]
    risk_assets = ["AUD", "NZD", "GBP", "CAD"] # Devises Beta
    safe_havens = ["JPY", "CHF", "USD"]       # Devises Safe Haven

    impact = 0
    if risk_on:
        if base in risk_assets: impact += 15
        if quote in safe_havens: impact += 15
    else:
        if base in safe_havens: impact += 20
        if quote in risk_assets: impact += 15

    return {
        "sentiment": "RISK-ON" if risk_on else "RISK-OFF",
        "score_risk_on": score_risk_on,
        "impact_net": impact,
        "biais": "bullish" if impact > 10 and risk_on else "bearish" if impact > 10 and not risk_on else "neutre",
        "explication": f"Marché en mode {'Appétit' if risk_on else 'Aversion'} au risque. VIX à {vix}."
    }

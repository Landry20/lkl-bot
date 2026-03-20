import requests

def get_market_sentiment():
    """
    Récupère le sentiment global du marché (VIX, S&P 500, Gold).
    """
    # Mock pour le raisonnement
    return {
        "vix": 16.5,
        "sp500_change": 0.8,
        "gold_trend": "bullish",
        "dxy_index": 104.2,
        "appetit": 65 # 0-100 score d'appétit au risque
    }

def get_commodity_prices():
    """
    Récupère les prix des matières premières clés.
    """
    return {
        "oil_wti": 78.5,
        "gold": 2035.0,
        "copper": 3.85
    }

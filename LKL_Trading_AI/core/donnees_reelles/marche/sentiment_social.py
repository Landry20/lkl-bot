import random

def get_social_sentiment(symbol):
    """
    Simule l'analyse de sentiment sur Twitter/X et Reddit.
    Utile pour identifier l'exubérance irrationnelle ou la panique.
    """
    vibe = random.choice(["Bullish Panic", "Greed", "Neutral", "Fear", "Extreme Fear"])
    score = random.randint(-50, 50) # Score entre -50 (Fear) et 50 (Greed)
    
    return {
        "symbol": symbol,
        "social_vibe": vibe,
        "social_score": score,
        "reddit_consensus": "Achat massif" if score > 30 else "Vente" if score < -30 else "Hésitant"
    }

def get_institutional_bias(symbol):
    """
    Simule l'extraction des données COT (Commitment of Traders).
    Permet de savoir ce que font les banques et gros fonds.
    """
    positions = random.choice(["Long Heavy", "Short Covering", "Neutral", "Short Heavy"])
    
    return {
        "symbol": symbol,
        "cot_status": positions,
        "smart_money_bias": "Bullish" if "Long" in positions else "Bearish" if "Short" in positions else "Neutre"
    }

def croiser_donnees_v3(symbol):
    """Croise le sentiment social (particuliers) et les données institutionnelles."""
    social = get_social_sentiment(symbol)
    inst = get_institutional_bias(symbol)
    
    resultat = f"Divergence détectée : Les particuliers sont en {social['social_vibe']}, mais les banques sont {inst['smart_money_bias']} ! 🛰️📉"
    
    if social['social_score'] > 40 and inst['smart_money_bias'] == "Bullish":
        resultat = "Convergence Forte : Tout le monde est à l'achat ! 🚀✅"
    
    return resultat

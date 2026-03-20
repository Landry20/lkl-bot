import sys
import os

# Ajustement du path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def analyser_discours(central_bank="FED", recent_speeches=None):
    """
    Analyse le ton des discours des banquiers centraux (Hawkish/Dovish).
    """
    if not recent_speeches:
        recent_speeches = ["Powell mentions persistent inflation risks", "ECB highlights economic uncertainty"]

    # Lexique étendu
    hawkish_lexicon = [
        "inflation", "tightening", "persistent", "raise", "restrictive", "overheating",
        "hike", "above target", "strength", "solid", "monitor carefully"
    ]
    dovish_lexicon = [
        "weakness", "support", "easing", "lower", "accommodation", "slowing",
        "cut", "downside risks", "fragile", "uncertainty", "patience"
    ]

    score = 0
    ton = "neutre"

    for speech in recent_speeches:
        content = speech.lower()
        for kw in hawkish_lexicon:
            if kw in content: score += 8
        for kw in dovish_lexicon:
            if kw in content: score -= 8

    # Calibration du ton
    if score > 20: ton = "hawkish"
    elif score < -20: ton = "dovish"
    elif score > 5: ton = "slightly hawkish"
    elif score < -5: ton = "slightly dovish"

    return {
        "bank": central_bank,
        "score_ton": score,
        "ton": ton,
        "sentiment": "Positif (Bullish)" if "hawkish" in ton else "Négatif (Bearish)" if "dovish" in ton else "Neutre",
        "summary": f"Le ton de la {central_bank} est jugé {ton.upper()} ({score} pts)."
    }

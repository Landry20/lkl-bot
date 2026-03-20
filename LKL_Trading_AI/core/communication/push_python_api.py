"""
Envoi des analyses techniques vers l'API Python (port 8001) pour affichage dans le menu Fonda / Analyses.
"""
import requests

PYTHON_API_BASE = "http://localhost:8001/api"


def push_analysis_to_dashboard(symbol: str, action: str, trend: str, fibo_zone: str, confirmation_count: int, chart_data=None, image_url: str = None, details: str = None):
    """
    Envoie une analyse technique à l'API Python pour qu'elle apparaisse dans le menu Analyses/Fonda.
    Appelé par le bot à chaque analyse (confirmée ou non) pour garder le dashboard à jour.
    """
    url = f"{PYTHON_API_BASE}/analyses"
    payload = {
        "symbol": symbol,
        "action": action or "none",
        "trend": trend or "neutral",
        "fibo_zone": fibo_zone or "",
        "confirmation_count": confirmation_count,
        "chart_data": chart_data or [],
        "image_url": image_url or "",
        "details": details or "",
        "timeframe": "H4"
    }
    try:
        r = requests.post(url, json=payload, timeout=3)
        if r.status_code in (200, 201):
            return True
        return False
    except Exception as e:
        print(f"[PUSH API] Analyse non envoyée au dashboard: {e}")
        return False

"""
RECEPTION BACKEND
Récupération de données depuis Laravel (GET).
"""
import requests
import json

API_BASE_URL = "http://localhost:8000/api"

def get_from_laravel(endpoint: str):
    """
    Récupère des données via GET.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code >= 400:
            print(f"[API GET ERROR] {url} -> {res.status_code} {res.text}")
            return None
        return res.json()
    except Exception as e:
        print(f"[API GET EXCEPTION] {url} -> {e}")
        return None

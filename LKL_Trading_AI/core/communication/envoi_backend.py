"""
ENVOI BACKEND
Envoi de données vers Laravel (POST).
"""
import requests
import json
from communication.reception_backend import API_BASE_URL

def send_to_laravel(endpoint: str, data: dict):
    """
    Envoie des données via POST.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        res = requests.post(url, json=data, headers=headers, timeout=5)
        if res.status_code >= 400:
            print(f"[API PUSH ERROR] {url} -> {res.status_code} {res.text}")
            return None
        return res.json()
    except Exception as e:
        print(f"[API PUSH EXCEPTION] {url} -> {e}")
        return None

import json
import os

CONFIG_FILE = "data/config.json"

class ConfigManager:
    def __init__(self):
        self.config = {
            "mt5_login": 0,
            "mt5_password": "",
            "mt5_server": "",
            "risk_percent": 1.0,
            "symbols": ["EURUSD", "XAUUSD", "GBPUSD", "US30", "BTCUSD"],
            "news_api_key": "",
            "openai_api_key": ""
        }
        self.load()

    def load(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    self.config.update(json.load(f))
            except Exception as e:
                print(f"[CONFIG] Erreur de chargement : {e}")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()

    def save(self):
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=4)

config = ConfigManager()

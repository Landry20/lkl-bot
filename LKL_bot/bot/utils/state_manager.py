import hashlib
import json
import os

class StateManager:
    """
    Gère l'état mémoire du bot pour éviter les répétitions.
    Stocke les hashes des dernières analyses et news envoyées.
    """
    def __init__(self, state_file="bot_state.json"):
        self.state_file = state_file
        self.state = self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=4)

    def get_hash(self, data):
        """Génère un hash unique pour un set de données."""
        data_str = json.dumps(data, sort_keys=True)
        return hashlib.md5(data_str.encode()).hexdigest()

    def has_changed(self, category, data):
        """
        Vérifie si la donnée a changé par rapport au dernier envoi.
        Retourne True si c'est nouveau ou modifié, False sinon.
        """
        new_hash = self.get_hash(data)
        old_hash = self.state.get(category)
        
        if new_hash != old_hash:
            self.state[category] = new_hash
            self.save_state()
            return True
        return False

    def clear(self, category=None):
        if category:
            if category in self.state:
                del self.state[category]
        else:
            self.state = {}
        self.save_state()

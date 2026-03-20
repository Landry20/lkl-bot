import json
import os

class MetaCerveau:
    """
    Le 'Méta-Cerveau' V3 du robot LKL.
    Responsable de l'auto-critique, du suivi de performance et de l'ajustement des poids.
    """
    def __init__(self, data_path="meta_data.json"):
        self.data_path = data_path
        self.stats = self._charger_stats()
        self.poids_actuels = {
            "fondamental": 1.0,
            "technique": 1.0,
            "sentiment": 1.0,
            "ia_externe": 1.0
        }

    def _charger_stats(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                return json.load(f)
        return {"analyses": [], "accuracy": 1.0}

    def enregistrer_analyse(self, symbol, type_analyse, biais, prix_entree):
        """Enregistre une analyse pour suivi ultérieur."""
        nouvelle = {
            "symbol": symbol,
            "type": type_analyse, # 'fondam', 'tech', 'ia'
            "biais": biais,
            "prix_entree": prix_entree,
            "status": "pending",
            "timestamp": "now"
        }
        self.stats["analyses"].append(nouvelle)
        self._sauvegarder()
        print(f"[META] Analyse enregistrée pour {symbol} ({type_analyse})")

    def evaluer_succes(self, symbol, cours_actuel):
        """
        Compare l'analyse au mouvement réel du marché.
        Si l'analyse était 'Bullish' et que le prix a monté, succès !
        """
        for a in self.stats["analyses"]:
            if a["symbol"] == symbol and a["status"] == "pending":
                succes = False
                if a["biais"] == "bullish" and cours_actuel > a["prix_entree"]:
                    succes = True
                elif a["biais"] == "bearish" and cours_actuel < a["prix_entree"]:
                    succes = True
                
                a["status"] = "success" if succes else "failed"
                self._ajuster_intelligence(a["type"], succes)
        
        self._sauvegarder()

    def _ajuster_intelligence(self, type_analyse, succes):
        """Ajuste les poids de décision de manière autonome."""
        cle = "fondamental" if type_analyse == "fondam" else "technique"
        delta = 0.05 if succes else -0.05
        self.poids_actuels[cle] += delta
        # Clamp entre 0.5 et 2.0
        self.poids_actuels[cle] = max(0.5, min(2.0, self.poids_actuels[cle]))
        print(f"[META] Ajustement {cle} : Nouveau poids = {self.poids_actuels[cle]:.2f}")

    def get_conseil_strategique(self):
        """Donne un conseil basé sur l'apprentissage."""
        if self.poids_actuels["technique"] > self.poids_actuels["fondamental"]:
            return "Le marché est actuellement plus technique que fondamental. Privilégiez les structures de prix ! 📈"
        return "Les fondamentaux dominent. Restez attentifs aux news économiques ! 🏛️"

    def _sauvegarder(self):
        with open(self.data_path, 'w') as f:
            json.dump(self.stats, f, indent=4)

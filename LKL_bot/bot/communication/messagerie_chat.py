import time
import MetaTrader5 as mt5
from communication.envoi_backend import send_to_laravel
from communication.reception_backend import get_from_laravel
from raisonnement.clarification_fondamentale import ClarificateurFondamental
from utils.personnalite import PersonnaliteBot
from utils.ia_externe import IntelligenceExterne
from apprentissage.meta_apprentissage import MetaCerveau

# Imports des nouveaux scrapers
from donnees_reelles.marche.cryptos import get_crypto_data
from donnees_reelles.marche.indices import get_index_data
from donnees_reelles.marche.actions import get_stock_data

class ChatProcessor:
    """
    Processeur de chat Expert V3 - Meta-Cerveau & Maîtrise Prédictive 🧠🚀
    """
    def __init__(self, user_id, user_name="Trader"):
        self.user_id = user_id
        self.user_name = user_name
        self.bot = PersonnaliteBot()
        self.ia_expert = IntelligenceExterne()
        self.meta_cerveau = MetaCerveau()
        self.memoire_positions = []

    def refresh_memory(self):
        """Récupère l'état actuel des trades et l'historique"""
        try:
            positions = mt5.positions_get()
            self.memoire_positions = [pos._asdict() for pos in positions] if positions else []
            self.derniere_analyse = get_from_laravel('bot/fundamental/latest')
        except:
            self.memoire_positions = []
            self.derniere_analyse = None

    def process_new_messages(self):
        """Boucle de réception des commandes utilisateur"""
        try:
            res = get_from_laravel('chats')
            if res and 'data' in res:
                chats = res.get('data', {}).get('data', [])
                if not chats: return

                last_msg = chats[0]
                if last_msg.get('sender') == 'user':
                    print(f"[CHAT] Commande reçue: {last_msg['message']}")
                    self.refresh_memory()
                    self.generate_response(last_msg['message'])
        except Exception as e:
            print(f"[CHAT ERROR] {str(e)}")

    def generate_response(self, user_text):
        """Analyse multi-actifs, redirection IA et personnalité"""
        text = user_text.lower()
        clarificateur = ClarificateurFondamental()
        response_text = ""
        
        # 1. Analyse d'actifs Spécifiques (Crypto, Index, Stocks, Forex)
        if "analyse" in text or "que penses-tu de" in text:
            symbol = text.replace("analyse", "").replace("que penses-tu de", "").replace("-moi", "").strip().upper()
            
            # Détection du type d'actif
            type_actif = "FOREX"
            if any(c in symbol for c in ["BTC", "ETH", "SOL", "BNB"]):
                data = get_crypto_data(symbol)
                type_actif = "CRYPTO"
            elif any(i in symbol for i in ["US30", "NAS100", "GER40", "FRA40"]):
                data = get_index_data(symbol)
                type_actif = "INDEX"
            elif len(symbol) <= 4 and not symbol.endswith("USD"): 
                data = get_stock_data(symbol)
                type_actif = "STOCK"
            else: 
                data = mt5.symbol_info_tick(symbol)
            
            if data:
                raison = clarificateur.analyser_actif_special(symbol, type_actif)
                response_text = f"🌟 **ANALYSE EXPERTE : {symbol}** 🌟\n\n"
                response_text += f"Le prix actuel est de {data.get('bid', data.get('price'))}. 📡\n\n"
                response_text += f"{raison}\n\n"
                response_text += f"✨ **Verdict** : {self.bot.donner_avis_tranche('bullish' if type_actif == 'CRYPTO' else 'neutre')}"
            else:
                response_text = f"Désolé, je ne trouve pas l'actif '{symbol}' dans mes radars actuels. 🛰️ Vérifiez l'orthographe ! 😊"

        # 2. Requête vers ChatGPT / Gemini (Savoir Approfondi)
        elif "chatgpt" in text or "gemini" in text or "approfondi" in text:
            question = text.replace("chatgpt", "").replace("gemini", "").strip()
            expertise = self.ia_expert.demander_expertise(question)
            impression = "Impressionnant, n'est-ce pas ?"
            response_text = f"🔍 **Ressources IA (Gemini/ChatGPT)** 🔍\n\n {expertise} \n\n {self.bot.humaniser(impression)}"

        # 3. Mémoire des trades
        elif "trade" in text or "position" in text:
            if not self.memoire_positions:
                response_text = "Aucune position ouverte. C'est le moment idéal pour une analyse à froid ! 🧘‍♂️✨"
            else:
                response_text = f"Vos {len(self.memoire_positions)} positions sont sous ma protection ! 🛡️💎"

        # 3. Conseil Stratégique (Meta-Cerveau V3)
        elif "conseil" in text or "stratégie" in text:
            conseil = self.meta_cerveau.get_conseil_strategique()
            response_text = f"🏹 **CONSEIL STRATÉGIQUE V3** 🏹\n\n {self.user_name}, {conseil} \n\n {self.bot.humaniser('Gardons ce cap ensemble !')}"

        # 4. Pensée Critique (Auto-Apprentissage)
        elif "critique" in text or "avis honnête" in text:
            response_text = f"🧐 **PENSÉE CRITIQUE DE {self.bot.bot_name}** 🧐\n\n"
            response_text += f"Honnêtement {self.user_name}, mon auto-apprentissage montre que nous devons être prudents. "
            response_text += "La volatilité actuelle piége pas mal d'analyses techniques. Restons sur les news ! 🏛️📉"

        # 5. Politesse et Débat
        elif "bonjour" in text or "hello" in text:
            response_text = self.bot.saluer(self.user_name)
        else:
            response_text = f"C'est passionnant, {self.user_name} ! {self.bot.debattre('multi-actifs')}"

        # Envoi
        payload = {"user_id": self.user_id, "message": response_text, "sender": "bot"}
        send_to_laravel('bot/response', payload)

def run_chat_worker():
    """Lancement du worker de chat en boucle"""
    print("=== LKL CHAT WORKER DÉMARRÉ (PERSONNALISÉ) ===")
    while True:
        # Simulation pour l'utilisateur 1 (Ex: Landry)
        processor = ChatProcessor(user_id=1, user_name="Landry")
        processor.process_new_messages()
        time.sleep(5)

if __name__ == "__main__":
    run_chat_worker()

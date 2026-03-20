from data.db import db
from core.utils.ia_externe import generar_resposta
import datetime

class ChatService:
    def send_message(self, user_id: int, message: str, msg_type: str = "text", media_url: str = None):
        # 1. Enregistrer message utilisateur
        db.execute("""
            INSERT INTO chat_history (user_id, sender, message, type, media_url, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, "user", message, msg_type, media_url, datetime.datetime.now()))

        # 2. Générer réponse IA
        try:
            bot_response = generar_resposta(message)
        except Exception as e:
            bot_response = f"Erreur IA: {str(e)}"

        # 3. Enregistrer réponse Bot
        db.execute("""
            INSERT INTO chat_history (user_id, sender, message, type, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, "bot", bot_response, "text", datetime.datetime.now()))

        return {
            "user_msg": message,
            "bot_msg": bot_response
        }

    def get_history(self, user_id: int, limit: int = 50):
        return db.fetch_all("""
            SELECT * FROM chat_history 
            WHERE user_id = ? 
            ORDER BY created_at DESC 
            LIMIT ?
        """, (user_id, limit))

chat_service = ChatService()

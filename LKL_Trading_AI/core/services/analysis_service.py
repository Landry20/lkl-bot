from data.db import db
from core.notification_manager import notification_manager
import datetime

class AnalysisService:
    def create_analysis(self, analysis_data: dict):
        """
        Enregistre une nouvelle analyse technique.
        """
        try:
            # Check doublons récents (optionnel)
            existing = db.fetch_one("SELECT id FROM analyses WHERE symbol=? AND created_at > datetime('now', '-1 hour')", (analysis_data['symbol'],))
            if existing:
                return existing

            # Insert
            row_id = db.execute("""
                INSERT INTO analyses (symbol, action, trend, confirmation_count, fibo_zone, price, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                analysis_data['symbol'],
                analysis_data['action'],
                analysis_data.get('trend', 'Unknown'),
                analysis_data.get('confirmation_count', 0),
                analysis_data.get('fibo_zone', ''),
                analysis_data.get('price', 0.0),
                datetime.datetime.now()
            ))
            
            # Notify UI
            notification_manager.send(
                "Nouvelle Analyse", 
                f"{analysis_data['symbol']} : {analysis_data['action']} ({analysis_data.get('fibo_zone')})", 
                "SUCCESS"
            )
            
            return {**analysis_data, "id": row_id}
            
        except Exception as e:
            print(f"[AnalysisService] Error: {e}")
            return None

    def get_recent_analyses(self, limit=20):
        return db.fetch_all("SELECT * FROM analyses ORDER BY created_at DESC LIMIT ?", (limit,))

analysis_service = AnalysisService()

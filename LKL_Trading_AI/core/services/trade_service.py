from data.db import db
from core.notification_manager import notification_manager
import datetime

class TradeService:
    def record_trade(self, trade_data: dict):
        """
        Enregistre un trade exécuté.
        """
        try:
            row_id = db.execute("""
                INSERT INTO trades (ticket, symbol, type, price, sl, tp, lot, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                trade_data.get('ticket', 0),
                trade_data['symbol'],
                trade_data['type'],
                trade_data.get('price', 0.0),
                trade_data.get('sl', 0.0),
                trade_data.get('tp', 0.0),
                trade_data.get('lot', 0.01),
                trade_data.get('status', 'OPEN'),
                datetime.datetime.now()
            ))
            
            notification_manager.send(
                "Trade Enregistré", 
                f"{trade_data['symbol']} {trade_data['type']} @ {trade_data.get('price')}", 
                "TRADE"
            )
            return row_id
        except Exception as e:
            print(f"[TradeService] Error: {e}")
            return None

    def update_trade_status(self, ticket: int, status: str, profit: float = None):
        if profit is not None:
            db.execute("UPDATE trades SET status=?, profit=? WHERE ticket=?", (status, profit, ticket))
        else:
            db.execute("UPDATE trades SET status=? WHERE ticket=?", (status, ticket))

    def get_trades(self, limit=50):
        return db.fetch_all("SELECT * FROM trades ORDER BY created_at DESC LIMIT ?", (limit,))

trade_service = TradeService()

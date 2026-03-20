from datetime import datetime

class NotificationManager:
    def __init__(self):
        self.history = []

    def send(self, title: str, message: str, level: str = "INFO"):
        """
        Enregistre une notification et l'affiche.
        Levels: INFO, SUCCESS, WARNING, ERROR, TRADE
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted = f"[{timestamp}] [{level}] {title}: {message}"
        
        # 1. Console Output
        print(formatted)
        
        # 2. Store in history (for UI)
        self.history.append({
            "time": timestamp,
            "level": level,
            "title": title,
            "message": message
        })
        
        # 3. TODO: Emit signal to UI (Tauri)
        # emit_to_frontend("notification", payload)

notification_manager = NotificationManager()

def send_notification(user_id, level, message, is_silent=False):
    """Compatibility wrapper for old code"""
    notification_manager.send("Bot Notification", message, level.upper())

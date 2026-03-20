from enum import Enum
import threading
import time

class AppState(Enum):
    OFF = "OFF"       # Application arrêtée
    IDLE = "IDLE"     # Application lancée, bot en pause
    ACTIVE = "ACTIVE" # Bot en cours d'analyse/trading
    ERROR = "ERROR"   # État d'erreur critique

class StateManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(StateManager, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.current_state = AppState.IDLE
        self.last_update = time.time()
        self.status_message = "Système prêt."
        self._initialized = True

    def set_state(self, new_state: AppState, message: str = ""):
        """Change l'état de l'application."""
        with self._lock:
            old_state = self.current_state
            self.current_state = new_state
            self.last_update = time.time()
            if message:
                self.status_message = message
            print(f"[STATE] Changement d'état : {old_state.value} -> {new_state.value} ({self.status_message})")

    def get_state(self):
        """Retourne l'état actuel et le message."""
        return {
            "state": self.current_state.value,
            "message": self.status_message,
            "timestamp": self.last_update
        }

    def is_active(self):
        return self.current_state == AppState.ACTIVE

# Instance globale
state_manager = StateManager()

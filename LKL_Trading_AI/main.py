import time
import sys
import os
import threading
from runtime.state_manager import state_manager, AppState

# Simulation du moteur de trading pour l'instant
from core.bot_engine import BotEngine

from core.ipc_server import run_ipc_background

# Initialisation du moteur réel
trading_engine = BotEngine()

def main_loop():
    """Boucle principale qui maintient le processus en vie et exécute le bot."""
    print(">>> Démarrage du moteur LKL Trading AI (Desktop Mode)")
    
    # Démarrage du serveur de commande pour l'UI
    run_ipc_background()
    
    # Au démarrage, on est en IDLE
    state_manager.set_state(AppState.IDLE, "En attente d'activation")

    try:
        while state_manager.current_state != AppState.OFF:
            
            if state_manager.is_active():
                # Le bot travaille
                try:
                    trading_engine.run_cycle()
                except Exception as e:
                    state_manager.set_state(AppState.ERROR, f"Erreur critique bot : {str(e)}")
            else:
                # Mode veille, on économise le CPU
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        print("\nArrêt manuel détecté.")
        state_manager.set_state(AppState.OFF)

    print("<<< Arrêt du système.")

if __name__ == "__main__":
    # Dans une vraie app GUI, ceci tournerait dans un thread séparé
    # Pour le test, on lance directement
    main_loop()

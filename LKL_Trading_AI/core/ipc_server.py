import socket
import threading
import json
from runtime.state_manager import state_manager, AppState

HOST = '127.0.0.1'
PORT = 5555

def handle_client(conn):
    try:
        data = conn.recv(1024).decode('utf-8')
        if not data: return
        
        parts = data.split('|')
        cmd = parts[0]
        payload = parts[1] if len(parts) > 1 else ""
        
        response = "OK"
        
        print(f"[IPC] Commande reçue : {cmd} ({payload})")

        if cmd == "GET_STATE":
            state = state_manager.get_state()
            response = f"{state['state']}|{state['message']}"
            
        elif cmd == "SET_STATE":
            if payload == "START":
                state_manager.set_state(AppState.ACTIVE, "Démarrage demandé par UI")
                response = "STARTED"
            elif payload == "STOP":
                state_manager.set_state(AppState.IDLE, "Arrêt demandé par UI")
                response = "STOPPED"
                
        elif cmd == "PING":
            response = "PONG"

        conn.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"[IPC ERROR] {e}")
    finally:
        conn.close()

def start_ipc_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[IPC] Serveur de commande écoute sur {HOST}:{PORT}")
        
        while True:
            conn, addr = server.accept()
            # Pour éviter de bloquer, on gère chaque commande dans un thread (ou vite fait)
            # Ici c'est très rapide donc on le fait en direct ou thread
            threading.Thread(target=handle_client, args=(conn,)).start()
            
    except Exception as e:
        print(f"[IPC CRITICAL] Impossible de démarrer le serveur : {e}")

def run_ipc_background():
    threading.Thread(target=start_ipc_server, daemon=True).start()

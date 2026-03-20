# LKL Bot - Backend Python FastAPI
# Serveur API principal pour gérer toutes les données dynamiques

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
import asyncio
import json
from datetime import datetime

# Import des routes
from routes import chat, analyses, trades, dashboard

app = FastAPI(title="LKL Bot API", version="1.0.0")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir les fichiers uploadés
from fastapi.staticfiles import StaticFiles
import os
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ============================================
# ÉTAT GLOBAL DU ROBOT
# ============================================
robot_state = {
    "active": False,
    "mt5_connected": False,
    "mode": "STANDBY",  # STANDBY, ACTIVE, ERROR
    "last_activation": None,
    "message": "Robot en veille - Démarrez le robot pour commencer"
}

# Gestionnaire de connexions WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        print(f"✅ User {user_id} connected via WebSocket")

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
            print(f"❌ User {user_id} disconnected")

    async def send_personal_message(self, message: dict, user_id: str):
        if user_id in self.active_connections:
            try:
                await self.active_connections[user_id].send_json(message)
            except Exception as e:
                print(f"Error sending message to {user_id}: {e}")

    async def broadcast(self, message: dict):
        """Envoie un message à tous les clients connectés"""
        for user_id, connection in self.active_connections.items():
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error broadcasting to {user_id}: {e}")

manager = ConnectionManager()

# Routes
app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(analyses.router, prefix="/api", tags=["Analyses"])
app.include_router(trades.router, prefix="/api", tags=["Trades"])
app.include_router(dashboard.router, prefix="/api", tags=["Dashboard"])

@app.get("/")
async def root():
    return {
        "message": "LKL Bot Python API",
        "version": "1.0.0",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    """WebSocket pour communication temps réel avec le frontend"""
    await manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            # Le client peut envoyer des messages ici si nécessaire
            print(f"Received from {user_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(user_id)

# Fonction utilitaire pour broadcaster des événements
async def broadcast_event(event_type: str, data: dict, user_id: str = None):
    """
    Envoie un événement via WebSocket
    - Si user_id est spécifié, envoie uniquement à cet utilisateur
    - Sinon, broadcast à tous
    """
    message = {
        "event": event_type,
        "data": data,
        "timestamp": datetime.now().isoformat()
    }
    
    if user_id:
        await manager.send_personal_message(message, user_id)
    else:
        await manager.broadcast(message)

# Rendre le manager, broadcast_event et robot_state disponibles pour les routes
app.state.manager = manager
app.state.broadcast_event = broadcast_event
app.state.robot_state = robot_state

# ============================================
# ENDPOINTS DE GESTION DU ROBOT
# ============================================
@app.get("/api/robot/status")
async def get_robot_status():
    """Récupère l'état actuel du robot"""
    return {
        "status": "success",
        "data": robot_state
    }

@app.post("/api/robot/activate")
async def activate_robot(data: dict):
    """Appelé par Laravel quand l'utilisateur démarre le robot"""
    robot_state["active"] = True
    robot_state["mode"] = "ACTIVE"
    robot_state["last_activation"] = datetime.now().isoformat()
    robot_state["message"] = "Robot actif - Toutes les fonctionnalités sont disponibles"
    
    # Broadcaster à tous les clients
    await broadcast_event("RobotActivated", robot_state)
    
    print("🤖 Robot activé !")
    return {
        "status": "success",
        "data": robot_state
    }

@app.post("/api/robot/deactivate")
async def deactivate_robot():
    """Appelé par Laravel quand l'utilisateur arrête le robot"""
    robot_state["active"] = False
    robot_state["mode"] = "STANDBY"
    robot_state["message"] = "Robot en veille - Démarrez le robot pour commencer"
    
    # Broadcaster à tous les clients
    await broadcast_event("RobotDeactivated", robot_state)
    
    print("🛑 Robot désactivé - Mode veille")
    return {
        "status": "success",
        "data": robot_state
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting LKL Bot Python API on http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)

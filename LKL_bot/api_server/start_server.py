# Script de démarrage du serveur Python FastAPI
# Exécutez ce fichier pour lancer le backend Python

import sys
import os

# Ajouter le chemin du bot au PYTHONPATH
sys.path.append(os.path.dirname(__file__))

if __name__ == "__main__":
    import uvicorn
    from main import app
    
    print("=" * 60)
    print("🚀 LKL Bot - Backend Python FastAPI")
    print("=" * 60)
    print("📡 API disponible sur: http://localhost:8001")
    print("📚 Documentation: http://localhost:8001/docs")
    print("🔌 WebSocket: ws://localhost:8001/ws/{user_id}")
    print("=" * 60)
    print("\n✅ Serveur démarré avec succès!\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )

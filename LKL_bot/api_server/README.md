# LKL Bot - Backend Python FastAPI

## 🚀 Démarrage Rapide

### 1. Installer les dépendances
```bash
cd c:\Users\lou_kou\bot_projet\LKL_bot
.\venv\Scripts\activate
pip install -r api_server\requirements.txt
```

### 2. Démarrer le serveur
```bash
cd api_server
python start_server.py
```

Le serveur sera disponible sur **http://localhost:8001**

## 📡 Endpoints Disponibles

### Chat IA
- `POST /api/chats` - Envoyer un message au chat IA
- `GET /api/chats?user_id={id}` - Récupérer l'historique du chat

### Analyses Techniques
- `GET /api/analyses` - Récupérer les analyses récentes
- `POST /api/analyses` - Créer une nouvelle analyse (appelé par le bot)

### Trades
- `GET /api/trades` - Récupérer les trades récents
- `POST /api/trades` - Créer un nouveau trade (appelé par le bot)

### Dashboard
- `GET /api/dashboard/stats` - Récupérer les statistiques du dashboard
- `POST /api/dashboard/stats` - Mettre à jour les stats (appelé par le bot)

### WebSocket
- `ws://localhost:8001/ws/{user_id}` - Connexion WebSocket pour le temps réel

## 🔧 Architecture

```
Frontend React (localhost:3000)
    ↓
    ├─→ Laravel (localhost:8000) - Auth & Config
    │   ├─ Login/Register
    │   ├─ Toggle Robot
    │   ├─ Comptes MT5
    │   └─ Paramètres
    │
    └─→ Python FastAPI (localhost:8001) - Données Dynamiques
        ├─ Chat IA
        ├─ Analyses Techniques
        ├─ Trades
        └─ Dashboard Stats
```

## 📝 Utilisation depuis le Bot Python

```python
import requests

# Envoyer un trade
requests.post('http://localhost:8001/api/trades', json={
    'symbol': 'XAUUSD',
    'action': 'buy',
    'price': 2050.50,
    'profit': 125.00,
    'status': 'ACTIF'
})

# Envoyer une analyse
requests.post('http://localhost:8001/api/analyses', json={
    'symbol': 'EURUSD',
    'action': 'buy',
    'trend': 'Haussière',
    'fibo_zone': '0.618',
    'confirmation_count': 2,
    'chart_data': []
})
```

## 🌐 Documentation Interactive

Une fois le serveur démarré, accédez à :
- **Swagger UI** : http://localhost:8001/docs
- **ReDoc** : http://localhost:8001/redoc

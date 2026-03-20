# Routes pour les Trades
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class Trade(BaseModel):
    symbol: str
    action: str
    price: float
    profit: Optional[float] = 0.0
    status: str = "ACTIF"

# Stockage temporaire des trades (en mémoire)
trades_storage: List[dict] = []

@router.get("/trades")
async def get_trades(limit: int = 20):
    """
    Récupère les trades récents
    """
    return {
        "status": "success",
        "data": trades_storage[-limit:] if trades_storage else []
    }

@router.post("/trades")
async def create_trade(trade: Trade, request: Request):
    """
    Crée un nouveau trade
    Appelé par le bot Python quand un trade est exécuté
    """
    try:
        trade_data = {
            "id": len(trades_storage) + 1,
            "symbol": trade.symbol,
            "action": trade.action,
            "price": trade.price,
            "profit": trade.profit,
            "status": trade.status,
            "time": datetime.now().strftime('%H:%M:%S'),
            "created_at": datetime.now().isoformat()
        }
        
        trades_storage.append(trade_data)
        
        # Broadcaster via WebSocket
        await request.app.state.broadcast_event(
            "TradeUpdated",
            {"trade": trade_data}
        )
        
        return {
            "status": "success",
            "data": trade_data
        }
    
    except Exception as e:
        print(f"Error creating trade: {e}")
        raise HTTPException(status_code=500, detail=str(e))

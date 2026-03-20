# Routes pour le Dashboard
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime

router = APIRouter()

# Statistiques du dashboard (en mémoire)
dashboard_stats = {
    "total_profit": 0.0,
    "total_trades": 0,
    "win_rate": 0.0,
    "mt5_connected": False,
    "bot_running": False,
    "last_update": datetime.now().isoformat()
}

@router.get("/dashboard/stats")
async def get_dashboard_stats():
    """
    Récupère les statistiques du dashboard
    """
    return {
        "status": "success",
        "data": dashboard_stats
    }

@router.post("/dashboard/stats")
async def update_dashboard_stats(stats: Dict[str, Any]):
    """
    Met à jour les statistiques du dashboard
    Appelé par le bot Python pour synchroniser les stats
    """
    try:
        dashboard_stats.update(stats)
        dashboard_stats["last_update"] = datetime.now().isoformat()
        
        return {
            "status": "success",
            "data": dashboard_stats
        }
    
    except Exception as e:
        print(f"Error updating dashboard stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Routes pour les Analyses Techniques
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class Analysis(BaseModel):
    symbol: str
    action: str
    trend: str
    fibo_zone: str
    confirmation_count: int
    chart_data: Optional[List] = []
    image_url: Optional[str] = ""
    details: Optional[str] = ""
    timeframe: Optional[str] = "H4"

# Stockage temporaire des analyses (en mémoire)
# TODO: Remplacer par une vraie base de données si nécessaire
analyses_storage: List[dict] = []

@router.get("/analyses")
async def get_analyses(limit: int = 20):
    """
    Récupère les analyses techniques récentes
    """
    return {
        "status": "success",
        "data": analyses_storage[-limit:] if analyses_storage else []
    }

@router.post("/analyses")
async def create_analysis(analysis: Analysis, request: Request):
    """
    Crée une nouvelle analyse technique
    Appelé par le bot Python quand une nouvelle opportunité est détectée
    """
    try:
        analysis_data = {
            "id": len(analyses_storage) + 1,
            "symbol": analysis.symbol,
            "action": analysis.action,
            "trend": analysis.trend,
            "fibo_zone": analysis.fibo_zone,
            "confirmation_count": analysis.confirmation_count,
            "chart_data": analysis.chart_data or [],
            "image_url": getattr(analysis, "image_url", "") or "",
            "details": getattr(analysis, "details", "") or "",
            "timeframe": getattr(analysis, "timeframe", "H4") or "H4",
            "created_at": datetime.now().isoformat()
        }
        
        analyses_storage.append(analysis_data)
        
        # Broadcaster via WebSocket
        await request.app.state.broadcast_event(
            "AnalysisCreated",
            {"analysis": analysis_data}
        )
        
        return {
            "status": "success",
            "data": analysis_data
        }
    
    except Exception as e:
        print(f"Error creating analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyses/check")
async def check_analysis(data: dict):
    """
    Vérifie si une analyse existe déjà
    """
    symbol = data.get("symbol")
    existing = [a for a in analyses_storage if a["symbol"] == symbol]
    
    return {
        "status": "success",
        "exists": len(existing) > 0,
        "data": existing[0] if existing else None
    }

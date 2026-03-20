# Routes pour le Chat IA
from fastapi import APIRouter, HTTPException, Request, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import shutil
from datetime import datetime
import sys
import os

# Ajouter le chemin du bot pour importer ia_externe
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'bot'))
from utils.ia_externe import generar_resposta

router = APIRouter()

class ChatMessage(BaseModel):
    message: str
    user_id: int

class ChatResponse(BaseModel):
    id: str
    user_id: int
    message: str
    sender: str
    type: str
    created_at: str

@router.post("/chats/upload")
async def upload_file(
    file: UploadFile = File(...),
    message: str = Form(...),
    user_id: int = Form(...),
    request: Request = None  # Inject request dependency
):
    """
    Upload une image ou vidéo et analyse son contenu
    """
    try:
        # Créer le dossier uploads s'il n'existe pas
        upload_dir = os.path.join(os.path.dirname(__file__), '..', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Sauvegarder le fichier
        timestamp = int(datetime.now().timestamp())
        filename = f"{user_id}_{timestamp}_{file.filename}"
        file_path = os.path.join(upload_dir, filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        file_url = f"http://localhost:8001/uploads/{filename}"
        file_type = "video" if file.content_type.startswith("video/") else "image"
        
        # Analyser le contenu (Simulation)
        analysis_response = f"J'ai bien reçu votre fichier {file.filename}. C'est un superbe graphique ! Je vais l'analyser..."
        if file_type == "image":
             analysis_response += " Je détecte une tendance haussière potentielle sur ce graphique."
        
        # Créer la réponse du bot
        bot_response_data = {
            "id": f"bot_{timestamp}",
            "user_id": user_id,
            "message": analysis_response,
            "sender": "bot",
            "type": "text",
            "created_at": datetime.now().isoformat()
        }
        
        # Créer le message utilisateur (pour l'affichage en temps réel)
        user_message_data = {
            "id": f"user_{timestamp}",
            "user_id": user_id,
            "message": message,
            "sender": "user",
            "type": file_type,
            "media_url": file_url,
            "created_at": datetime.now().isoformat()
        }

        # Broadcaster le message utilisateur
        await request.app.state.broadcast_event(
            "MessageSent",
            {"chat": user_message_data},
            str(user_id)
        )
        
        # Broadcaster la réponse du bot après un court délai
        import asyncio
        async def send_bot_response():
            await asyncio.sleep(1)
            await request.app.state.broadcast_event(
                "MessageSent",
                {"chat": bot_response_data},
                str(user_id)
            )
            
        asyncio.create_task(send_bot_response())
        
        return {
            "status": "success",
            "data": user_message_data
        }

    except Exception as e:
        print(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chats")
async def send_chat_message(
    body: ChatMessage,
    request: Request = None
):
    """
    Envoie un message texte et déclenche une réponse IA.
    """
    try:
        user_id = body.user_id
        message_text = body.message.strip()
        if not message_text:
            raise HTTPException(status_code=400, detail="Message vide")

        timestamp = int(datetime.now().timestamp())
        user_message_data = {
            "id": f"user_{timestamp}",
            "user_id": user_id,
            "message": message_text,
            "sender": "user",
            "type": "text",
            "created_at": datetime.now().isoformat()
        }

        if request and hasattr(request.app.state, "broadcast_event"):
            await request.app.state.broadcast_event(
                "MessageSent",
                {"chat": user_message_data},
                str(user_id)
            )

        # Réponse IA (simplifiée ou via ia_externe)
        try:
            bot_text = generar_resposta(message_text)
        except Exception:
            bot_text = f"Message reçu : « {message_text[:100]} ». (Réponse IA en cours de configuration.)"

        bot_message_data = {
            "id": f"bot_{timestamp}",
            "user_id": user_id,
            "message": bot_text,
            "sender": "bot",
            "type": "text",
            "created_at": datetime.now().isoformat()
        }

        if request and hasattr(request.app.state, "broadcast_event"):
            import asyncio
            async def send_bot():
                await asyncio.sleep(0.3)
                await request.app.state.broadcast_event(
                    "MessageSent",
                    {"chat": bot_message_data},
                    str(user_id)
                )
            asyncio.create_task(send_bot())

        return {
            "status": "success",
            "data": user_message_data
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error send_chat_message: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/chats")
async def get_chat_history(user_id: int, limit: int = 50):
    """
    Récupère l'historique du chat (pour l'instant retourne un tableau vide,
    vous pouvez implémenter la sauvegarde en base de données si nécessaire)
    """
    # TODO: Implémenter la récupération depuis la base de données si nécessaire
    return {
        "status": "success",
        "data": {
            "data": [],
            "total": 0
        }
    }

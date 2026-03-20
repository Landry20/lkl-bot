from communication.envoi_backend import send_to_laravel

def send_notification(user_id, msg_type, message, token=None, url=None, is_silent=False):
    """
    Envoie une notification à la base de données via la couche de communication centrale.
    """
    if not user_id:
        print("[NOTIFY] Erreur: user_id manquant")
        return False
            
    # Si silencieux, on modifie le type pour que le frontend puisse filtrer
    final_type = f"silent_{msg_type}" if is_silent else msg_type
        
    data = {
        "user_id": user_id,
        "type": final_type,
        "message": message,
        "url": url
    }
    
    res = send_to_laravel('notifications', data)
    if res:
        print(f"[NOTIFY] Notification envoyée pour User {user_id}: {message[:30]}...")
        return True
    return False

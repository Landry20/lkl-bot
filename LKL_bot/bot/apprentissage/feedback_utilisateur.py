def enregistrer_feedback_utilisateur(user_id, message_id, feedback_type):
    """
    Enregistre si l'utilisateur a trouvé une réponse utile (👍/👎).
    """
    print(f"[FEEDBACK] User {user_id} feedback on {message_id}: {feedback_type}")
    # TODO: Stocker en DB pour ajuster les poids via apprentissage/ajustement_scores.py

def extraire_preferences(chat_history):
    """
    Analyse l'historique de chat pour ajuster les préférences de réponse.
    Ex: Si l'utilisateur demande toujours 'macro', augmenter le poids macro.
    """
    # Analyse de texte simplifiée
    preferences = {"macro": 0, "geo": 0, "micro": 0}
    for msg in chat_history:
        text = msg.lower()
        if "macro" in text: preferences["macro"] += 1
        if "geo" in text: preferences["geo"] += 1
        
    return preferences

def generer_briefing_quotidien(user_name, meta_data, sentiment_data):
    """
    Génère un briefing textuel conçu pour être lu (voix) ou affiché.
    V3 - Utilise les données du Méta-Cerveau et du Sentiment Social.
    """
    ton_marche = "favorable" if meta_data['technique'] > 1.0 else "complexe"
    
    briefing = (
        f"Ligne de départ, {user_name}. 🏁 Voici votre briefing stratégique L_K_L. \n\n"
        f"Aujourd'hui, mon Méta-Cerveau indique un environnement {ton_marche}. "
        f"Les banques sont principalement positionnées en {sentiment_data['smart_money_bias']}, "
        f"tandis que les particuliers sur reddit sont plutôt {sentiment_data['reddit_consensus']}. ⚖️ \n\n"
        "Mon conseil : Surveillez la cassure des 1.0850 sur l'Euro. "
        "Soyez discipliné, soyez chic, et la rentabilité sera au rendez-vous. 🥂✨"
    )
    return briefing

def calculer_probabilite_v3(type_setup, scores):
    """
    Calcule une probabilité de succès basée sur la convergence des couches.
    (Fondamental + Technique + Social + COT).
    """
    base_prob = 50
    # Simulation d'un calcul complexe
    if scores.get('fondam') > 2 and scores.get('tech') > 2:
        base_prob = 75
    
    # Bonus de convergence V3
    if scores.get('social_align'): base_prob += 10
    
    return min(95, base_prob)

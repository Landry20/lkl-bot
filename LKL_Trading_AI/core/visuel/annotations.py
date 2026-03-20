def generate_annotations(symbol, ta_data, fundamental_data):
    """
    Génère les textes explicatifs à superposer sur les visuels.
    """
    annotations = []
    
    # Technique
    if ta_data.get('action') == 'buy':
        annotations.append(f"Zône d'achat détectée sur {symbol}")
    elif ta_data.get('action') == 'sell':
        annotations.append(f"Signal de vente sur {symbol}")

    # Fondamental
    bias = fundamental_data.get('bias', 'neutre')
    if bias != 'neutre':
        annotations.append(f"Biais Fondamental: {bias.upper()}")
        
    return annotations

def format_impact_text(importance):
    """
    Formate le texte d'impact pour le visuel.
    """
    return f"IMPACT {importance.upper()}"

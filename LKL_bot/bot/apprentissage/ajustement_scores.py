import json
import os

WEIGHTS_FILE = "poids_raisonnement.json"

def charger_poids():
    if os.path.exists(WEIGHTS_FILE):
        with open(WEIGHTS_FILE, 'r') as f:
            return json.load(f)
    return {
        "macro": 0.45,
        "micro": 0.15,
        "geopolitique": 0.15,
        "discours": 0.15,
        "marches": 0.10
    }

def ajuster_poids_selon_performance(category, succes: bool):
    """
    Ajuste les poids si une catégorie a été particulièrement prédictive ou non.
    """
    poids = charger_poids()
    
    ajustement = 0.02 if succes else -0.02
    poids[category] = max(0.05, min(0.60, poids[category] + ajustement))
    
    # Normalisation pour que la somme soit 1.0
    total = sum(poids.values())
    for k in poids:
        poids[k] /= total
        
    with open(WEIGHTS_FILE, 'w') as f:
        json.dump(poids, f, indent=4)
    
    return poids

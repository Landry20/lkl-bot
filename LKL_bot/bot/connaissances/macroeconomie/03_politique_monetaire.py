
"""
Politique Monétaire - Banques centrales, taux, QE
Version : 2.0 - Cours détaillé
"""

POLITIQUE_MONETAIRE = """
La politique monétaire est contrôlée par les banques centrales pour influencer croissance, inflation, emploi.

Outils :
- Taux directeurs : Haut → ralentit économie
- QE : Achats actifs → liquidités ↑ → inflation ↑
- Forward guidance : Discours sur futur

Impact Forex : Hawkish → devise ↑ | Dovish → devise ↓
"""

EXEMPLES = """
- Fed 2022 hikes : USD +20 %
- BCE QE 2015 : EUR ↓
- BoJ YCC : JPY faible
"""

def get_monetaire_summary():
    return """
Politique monétaire : Taux haut → devise ↑. QE → devise ↓.
"""

def get_full_monetaire():
    return POLITIQUE_MONETAIRE + "\n\n" + EXEMPLES
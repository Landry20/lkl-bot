
"""
Impact Macro sur Marché Forex - Volatilité, Annonces
Version : 2.0 - Cours détaillé
"""

IMPACT_FOREX = """
Annonces macro → volatilité (NFP 300 pips)
Surprise vs consensus clé
Calendrier : Forex Factory, Investing.com

Gestion : Filtre news, pause trading 15min avant/après
"""

EXEMPLES = """
NFP surprise +50k → USD ↑ 100 pips
CPI bas → USD ↓
"""

def get_impact_summary():
    return """
Macro impact Forex : Annonces → volatilité haute. Surprise vs consensus = mouvement.
"""

def get_full_impact():
    return IMPACT_FOREX + "\n\n" + EXEMPLES
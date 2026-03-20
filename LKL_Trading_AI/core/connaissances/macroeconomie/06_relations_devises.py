
"""
Relations entre Devises et Macroéconomie
Version : 2.0 - Cours détaillé
"""

RELATIONS_DEVICES = """
- Différentiel croissance : US > EU → USD ↑
- Différentiel taux : Haut → devise ↑
- Inflation relative : Haute → devise ↓ long terme
- Balance paiements : Surplus → devise ↑
- Dette : Haute → devise ↓

Exemples : US croissance > EU 2023 → EURUSD ↓
"""

def get_relations_summary():
    return """
Macro sur devises : Croissance/taux haut → ↑ | Dette/inflation haute → ↓.
"""

def get_full_relations():
    return RELATIONS_DEVICES
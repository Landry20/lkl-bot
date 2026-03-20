
"""
Cycles Économiques - Expansion, Récession, Boom, Bust
Version : 2.0 - Cours détaillé
"""

CYCLES_ECONOMIQUES = """
Cycle : Expansion (croissance) → Pic → Contraction (récession) → Trough → Recovery

Expansion : Devise ↑
Récession : Devise ↓ sauf refuges
Boom : Inflation → hawkish → devise ↑
Bust : Crise → refuges ↑

Durée moyenne : 5–7 ans
"""

EXEMPLES = """
- Boom 2010-2019 : USD fort fin cycle
- Récession 2020 COVID : USD ↑ refuge
"""

def get_cycles_summary():
    return """
Cycles : Expansion → devise ↑ | Récession → refuges ↑.
"""

def get_full_cycles():
    return CYCLES_ECONOMIQUES + "\n\n" + EXEMPLES
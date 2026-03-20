
"""
Dé-dollarisation - Tendances, acteurs, impact Forex long terme
Version : 2.0 - Cours détaillé
"""

DEDOLLARISATION_INTRO = """
La dé-dollarisation est la réduction progressive de la dépendance mondiale au dollar américain comme monnaie de réserve, de paiement et de facturation.

Contexte 2025–2030 :
- Sanctions massives Russie 2022 → accélération
- BRICS expansion + initiatives CNY/RUB
- Dette US élevée + inflation persistante → perte confiance ?

Devises alternatives : CNY, EUR, or, crypto, paniers BRICS
"""

ACTEURS_ET_ACTIONS = """
- **Russie** : Paiements CNY/RUB, gaz facturé RUB
- **Chine** : CNY dans Belt & Road, paiements pétrole Arabie
- **Inde** : Rupee pour commerce Russie
- **BRICS** : Discussions panier monnaies + gold-backed
- **Arabie Saoudite** : Vente pétrole en CNY possible
- **Banques centrales** : Achats or records (Chine, Inde, Turquie, Pologne)

Impact actuel (2026) :
- Dollar reste ~58 % réserves mondiales (baisse lente)
- Or ↑ long terme (alternative neutre)
- CNY ↑ dans commerce international (encore faible)
"""

IMPACTS_FOREX_LONG_TERME = """
- USD ↓ progressif si dé-dollarisation accélère
- Or ↑ structurel (hedge dé-dollarisation)
- CNY ↑ potentiel (mais contrôlé)
- EUR stable ou ↑ léger (alternative occidentale)
- AUD/NZD/CAD sensibles (Chine demande ↑)

Scénarios :
- Scénario lent (2030+) : USD perd 5–10 % part → or ↑, CNY ↑ modéré
- Scénario rapide (crise dette US) : USD crash, or +50 %, CNY +30 %

Règles LKL Bot :
- Or long si news BRICS + achats or ↑
- USD short prudent si dette US >140 % PIB + BRICS news
- Suivre % réserves CNY/or dans rapports FMI
"""

def get_dedollarisation_summary():
    return """
Dé-dollarisation : BRICS + sanctions → USD ↓ lent, or ↑, CNY ↑ potentiel.
Impact long terme : or long, USD hedge prudence.
"""

def get_full_dedollarisation():
    return (
        DEDOLLARISATION_INTRO + "\n\n" +
        ACTEURS_ET_ACTIONS + "\n\n" +
        IMPACTS_FOREX_LONG_TERME
    )
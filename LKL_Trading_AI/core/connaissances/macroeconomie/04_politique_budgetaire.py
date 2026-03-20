
"""
Politique Budgétaire - Dépenses état, dette, taxes
Version : 2.0 - Cours détaillé
"""

POLITIQUE_BUDGETAIRE = """
Politique budgétaire = décisions gouvernement sur dépenses, taxes, dette.

Expansionniste : Dépenses ↑ → croissance ↑ mais dette ↑ → devise ↓ long terme
Restrictive : Taxes ↑ → croissance ↓ → devise stable

Impact Forex : Déficit haut → devise ↓ (risque souverain)
"""

EXEMPLES = """
- US stimulus 2021 : USD ↓ initial
- Grèce dette 2010 : EUR ↓ massif
"""

def get_budgetaire_summary():
    return """
Budgétaire : Dépenses ↑ → croissance ↑ mais dette → devise ↓ long terme.
"""

def get_full_budgetaire():
    return POLITIQUE_BUDGETAIRE + "\n\n" + EXEMPLES
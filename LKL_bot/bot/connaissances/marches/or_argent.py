
"""
Cours Complet sur Or et Argent - Impacts, Facteurs de Mouvement, Géopolitique
Version : 2.0 - Étendu pour LKL Bot (XAUUSD, XAGUSD)
"""

OR_ARGENT_INTRODUCTION = """
Or (Gold - XAUUSD) et Argent (Silver - XAGUSD) sont des métaux précieux tradés comme commodities et devises (or = 'anti-USD').
- Marché : 24h/5j, volume 500B$/jour or, 100B$ argent
- Rôles : or refuge/inflation hedge, argent industriel (70%) + refuge
- Corrélations : or -0.8 USD, argent +0.6 cuivre (industriel)
- Volatilité : or 10-30$/jour, argent 0.5-2$/jour (plus volatile %)
- LKL Bot : 4% allocation or (hedge), 1% argent (opportuniste)
"""

OR_IMPACTS = {
    "caracteristiques": "Safe haven #1, non-yielding asset, stock-to-flow haut (rare)",
    "facteurs_mouvement": [
        "Inflation haute → or ↑ (hedge pouvoir d'achat)",
        "Real rates bas (taux - inflation <0) → or ↑ (coût opportunité bas)",
        "USD faible → or ↑ (prix en USD inverse)",
        "Géopolitique : Guerres (Ukraine 2022) → or +20% (risk-off)",
        "Crises financières : 2008 Lehman → or +100% (anti-banques)",
        "Banques centrales : Achats or Russie/Chine → or ↑ (dé-dollarisation)",
        "Mines/supply : Grèves Afrique du Sud → or ↑ temporaire",
        "Exemple 2020 COVID : Or 2200$ ATH (QE Fed + fear)",
        "Exemple 2023 Guerre Israël-Hamas : Or +15% (Moyen-Orient tensions)",
        "Exemple 2024 Fed pivot dovish → Or >2500$ (real rates négatifs)"
    ]
}

ARGENT_IMPACTS = {
    "caracteristiques": "70% industriel (solaire, électronique, batteries), 30% refuge/investissement",
    "facteurs_mouvement": [
        "Croissance industrielle : Demande Chine EV/solaire → argent ↑",
        "Gold ratio : Argent suit or en bull market (ratio 80:1 → 50:1)",
        "Inflation : Moins hedge que or, plus sensible commodities",
        "Géopolitique : Guerres → argent + (munitions, électronique militaire)",
        "Supply chain disruptions : Mines Mexique/Peru (70% production mondiale) → argent ↑",
        "Crypto corrélation : BTC bull → argent ↑ (comme 'digital silver')",
        "Exemple 2021 Reddit squeeze : Argent 30$ → 50$ spike (WallStreetBets)",
        "Exemple 2022 Guerre Ukraine : Argent +25% (industriel + refuge)"
    ]
}

STRATEGIE_OR_ARGENT_LKL = """
**Règles LKL Bot** :
- Long or si risk-off (guerre, récession) ou inflation >3%
- Short or si Fed hawkish + real rates >1%
- Argent : Follow or trend, mais scale in industriel (PMI >50)
- Hedge : 1% position or inverse USD longs
- News filter : Guerre alert Telegram + auto-long or si spike VIX >30
- Backend : Analyse impact géopolitique avant exécution
"""

def get_or_argent_summary() -> str:
    return """
Or : Guerre/inflation/rates bas → ↑ (safe hedge). Argent : Industriel + follow or → plus volatile.
Exemples : Ukraine 2022 or +20%, EV boom argent +30%.
LKL : Long or risk-off, hedge USD.
"""

def get_full_or_argent_explanation() -> str:
    lines = [OR_ARGENT_INTRODUCTION, "\n\nOr (XAUUSD) Impacts :\n"]
    lines.append(f"   Caractéristiques : {OR_IMPACTS['caracteristiques']}")
    lines.append("   Facteurs Mouvement :")
    for item in OR_IMPACTS['facteurs_mouvement']:
        lines.append(f"     - {item}")
    lines.append("\n\nArgent (XAGUSD) Impacts :\n")
    lines.append(f"   Caractéristiques : {ARGENT_IMPACTS['caracteristiques']}")
    lines.append("   Facteurs Mouvement :")
    for item in ARGENT_IMPACTS['facteurs_mouvement']:
        lines.append(f"     - {item}")
    lines.append("\n\nStratégie LKL Bot :\n" + STRATEGIE_OR_ARGENT_LKL)
    return "\n".join(lines)
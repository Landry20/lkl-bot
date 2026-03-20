
"""
Connaissances de base intégrées sur l'ANALYSE FONDAMENTALE
Version : 1.0
Utilisation : import dans c3_macro_analysis.py, strategy.py, prompts pour IA, notifications, etc.
"""

FUNDAMENTAL_ANALYSIS_INTRODUCTION = """
L'analyse fondamentale est une méthode d'évaluation des actifs financiers qui se concentre sur les 
facteurs économiques, financiers et autres facteurs qualitatifs et quantitatifs pouvant influencer 
la valeur d'un actif.

Cette approche vise à déterminer la **valeur intrinsèque** (juste valeur) d'un actif en examinant :
• Les données financières (entreprises, États, devises)
• Les conditions économiques générales
• Les tendances sectorielles / macroéconomiques
• Les facteurs qualitatifs (politique, géopolitique, gestion, etc.)

Objectif principal :
Identifier les actifs **sous-évalués** ou **surévalués** par le marché actuel 
afin de prendre des décisions d'investissement / trading basées sur la réalité économique 
plutôt que sur le seul comportement des prix.

Contrairement à l'analyse technique (qui étudie l'historique des prix et volumes),
l'analyse fondamentale cherche à comprendre **pourquoi** un prix devrait bouger à moyen/long terme.
"""

FUNDAMENTAL_ANALYSIS_KEY_CONCEPTS = {
    "juste_valeur": """
L'analyse fondamentale repose sur l'idée que chaque actif possède une **juste valeur** (intrinsic value).
Même si le marché peut temporairement :
• surévaluer un actif (bulles)
• sous-évaluer un actif (opportunités)

À long terme, le prix a tendance à converger vers cette juste valeur.
Les traders fondamentaux achètent quand Prix < Juste valeur et vendent quand Prix > Juste valeur.
    """,
    "marche_forex": """
Sur le marché des changes (Forex), on évalue la juste valeur relative entre deux devises.
Exemples de facteurs analysés :
• Différentiels de taux d'intérêt
• Croissance économique (PIB)
• Inflation (CPI, core inflation)
• Balance commerciale
• Politique monétaire des banques centrales
• Stabilité politique / géopolitique
• Prix des matières premières (pour devises commodity : AUD, CAD, NZD, etc.)
    """,
}

FUNDAMENTAL_ANALYSIS_LIMITATIONS = """
Inconvénients et limites importantes :

1. Pas de garantie de convergence rapide vers la juste valeur
   → le marché peut rester "irrationnel" très longtemps ("les marchés peuvent rester irrationnels
      plus longtemps que vous ne pouvez rester solvable" — Keynes)

2. Événements imprévisibles
   → catastrophes naturelles, guerres, scandales, décisions politiques soudaines

3. Volume énorme de données
   → difficile de savoir quelles informations sont vraiment déterminantes à court/moyen terme

4. Plus adaptée au moyen/long terme
   → moins efficace pour le scalping ou le trading très court terme
"""

FUNDAMENTAL_ANALYSIS_IMPORTANT_FACTORS = {
    "banques_centrales": [
        "Décisions sur les taux d'intérêt (hausse = généralement positif pour la devise)",
        "Forward guidance (ton hawkish / dovish)",
        "Politique monétaire (QE, QT, achat/vente d'actifs)",
        "Minutes / discours des gouverneurs",
        "Changements de gouvernance / succession"
    ],
    "donnees_economiques": [
        "Produit Intérieur Brut (PIB)",
        "Emploi (NFP, taux de chômage, JOLTS, etc.)",
        "PMI manufacturier et services",
        "Ventes au détail (Retail Sales)",
        "Production industrielle",
        "Balance commerciale"
    ],
    "inflation": [
        "CPI (headline et core)",
        "PCE (préféré par la Fed)",
        "PPI (prix à la production)",
        "Inflation sous-jacente vs inflation énergétique/alimentaire"
    ],
    "politique_et_geopolitique": [
        "Élections, changements de gouvernement",
        "Sanctions internationales",
        "Conflits armés",
        "Accords commerciaux",
        "Crises migratoires / politiques"
    ],
    "autres": [
        "Prix des matières premières (pétrole → CAD, gaz → EUR/NOK, métaux → AUD, etc.)",
        "Catastrophes naturelles",
        "Saisonnalité (agriculture, tourisme, énergie)",
        "Sentiment global de risque (risk-on / risk-off)"
    ]
}

# Version courte – utile pour les notifications ou les logs
FUNDAMENTAL_SUMMARY_SHORT = """
L'analyse fondamentale évalue la **juste valeur** d'une devise via :
• Taux d'intérêt & politique monétaire
• Croissance (PIB, PMI, emploi)
• Inflation
• Balance commerciale & matières premières
• Événements politiques & géopolitiques

Objectif : détecter si une paire est sous-évaluée ou surévaluée par rapport à sa réalité économique.
"""

def get_fundamental_introduction(full: bool = True) -> str:
    """Retourne l'introduction complète ou courte selon le besoin"""
    if full:
        return (
            FUNDAMENTAL_ANALYSIS_INTRODUCTION +
            "\n\n" +
            FUNDAMENTAL_ANALYSIS_KEY_CONCEPTS["juste_valeur"] +
            "\n\n" +
            FUNDAMENTAL_ANALYSIS_KEY_CONCEPTS["marche_forex"]
        )
    return FUNDAMENTAL_SUMMARY_SHORT


def get_important_factors_as_text() -> str:
    """Retourne une version texte formatée des facteurs les plus importants"""
    lines = ["Facteurs les plus importants en analyse fondamentale (Forex) :\n"]
    for category, items in FUNDAMENTAL_ANALYSIS_IMPORTANT_FACTORS.items():
        lines.append(f"• {category.replace('_', ' ').title()}:")
        for item in items:
            lines.append(f"  - {item}")
        lines.append("")
    return "\n".join(lines)


# Exemple d'utilisation simple
if __name__ == "__main__":
    print(get_fundamental_introduction(full=True))
    print("\n" + "="*60 + "\n")
    print(get_important_factors_as_text())
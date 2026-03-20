
"""
Indice des Directeurs d'Achat (PMI - Purchasing Managers' Index)
Version : 1.0
Connaissances clés pour traders Forex sur le PMI
"""

PMI_INTRODUCTION = """
L'Indice des Directeurs d'Achat (PMI) est l'un des indicateurs économiques les plus rapides et les plus suivis.

Il fournit une évaluation **précoce** de la santé économique d'un secteur (manufacturier, services ou composite) 
grâce à une enquête mensuelle auprès des responsables des achats des entreprises.

Le PMI est considéré comme un **indicateur avancé** (leading indicator) : il anticipe souvent les tendances 
de croissance, d'emploi et d'inflation avant que les données officielles (PIB, emploi, etc.) ne les confirment.
"""

QU_EST_CE_QUE_LE_PMI = """
**Méthodologie** :
- Enquête mensuelle réalisée par des organismes comme S&P Global (ex IHS Markit), ISM (USA), etc.
- Questions posées aux directeurs d'achat sur :
  - Nouveaux commandes
  - Production / activité
  - Emploi
  - Délais de livraison (supply chain)
  - Stocks / inventaires
  - Prix payés (matières premières)

**Interprétation simple** :
- PMI > 50 → **expansion** du secteur (croissance par rapport au mois précédent)
- PMI = 50 → **stagnation** (pas de changement significatif)
- PMI < 50 → **contraction** du secteur (recul par rapport au mois précédent)

**Types principaux** :
- PMI Manufacturier (Manufacturing PMI)
- PMI des Services (Services PMI)
- PMI Composite (combinaison des deux – le plus représentatif de l'économie globale)
"""

PUBLICATION_DU_PMI = """
**Dates typiques** :
- **Flash PMI** (estimation préliminaire) : publié vers le 23–24 du mois en cours (très rapide et impactant)
- **PMI final** : publié début du mois suivant (vers le 1er–3)

**Principaux pays suivis en Forex** :
- États-Unis : ISM Manufacturing PMI + S&P Global PMI
- Zone Euro : S&P Global PMI (flash + final), Allemagne très scrutée
- Royaume-Uni : S&P Global PMI
- Chine : Caixin PMI (privé) + Official NBS PMI
- Japon : au-japan PMI
- Australie, Canada, etc.

Le **PMI flash US et Eurozone** provoque souvent une volatilité notable sur les paires majeures.
"""

INTERPRETATION_ET_IMPACT_SUR_LE_FOREX = """
**Règles générales d'impact** :

- PMI > 50 et en hausse → croissance attendue → devise positive
- PMI > 50 mais en baisse → ralentissement → neutre à négatif
- PMI < 50 → contraction → devise sous pression
- Surprise importante (écart vs consensus) → réaction forte

**Exemples classiques** :
- PMI Manufacturier US > 52 + surprise → USD ↑ (EURUSD ↓)
- PMI Services Eurozone < 50 → EUR ↓ (surtout si Allemagne faible)
- Chine Caixin PMI < 50 → risque aversion → AUD, NZD, commodities sous pression

**Pourquoi c'est important** :
- Sort très tôt dans le mois (avant NFP, CPI, etc.)
- Donne une première indication sur la direction du PIB trimestriel
- Influence les attentes sur la politique monétaire (Fed, BCE, BoE…)
"""

STRATEGIE_TRADING_AUTOUR_DU_PMI = """
**Approches courantes** :

1. **Trading de la surprise** :
   - Attendre la publication du flash PMI
   - Comparer flash vs consensus vs précédent
   - Réaction immédiate souvent alignée avec la surprise

2. **Approche post-publication** :
   - Laisser passer les 5–15 premières minutes (volatilité)
   - Observer retracement vers niveaux techniques
   - Entrer sur continuation ou reversal avec confirmation

3. **Approche anticipative** (plus risquée) :
   - Analyser tendances récentes + données préalables (commandes industrielles, enquêtes confiance)
   - Positionner avant si biais très clair

**Conseils de gestion du risque** :
- Réduire la taille de position (volatilité modérée à forte)
- Éviter d’être en position juste avant le flash PMI
- Utiliser stops larges ou attendre confirmation technique
- Combiner avec d’autres données (PMI composite, ISM, NFP, etc.)
"""

PRINCIPAUX_ENSEIGNEMENTS_PMI = [
    "Le PMI est un indicateur avancé très rapide (flash ~ fin de mois)",
    "PMI > 50 = expansion / croissance ; PMI < 50 = contraction",
    "Le PMI Composite est le plus représentatif de l’économie globale",
    "Surprise vs consensus = principale source de volatilité",
    "Impact fort sur les devises, surtout sur flash PMI US et Eurozone",
    "Anticipe souvent les tendances du PIB, emploi et inflation",
    "Utilisé pour ajuster les attentes sur les décisions de banques centrales",
    "Allemagne PMI très scruté (leader économique de la zone euro)",
    "Chine PMI (Caixin) influence les devises commodity (AUD, NZD, CAD)"
]

def get_pmi_summary() -> str:
    """Résumé court pour notifications, logs ou dashboard rapide"""
    return """
Le PMI mesure l’activité économique via les directeurs d’achat.
> 50 = expansion → devise généralement positive
< 50 = contraction → devise sous pression
Flash PMI = très rapide et impactant (fin de mois)
Surprise vs attentes = source principale de mouvement sur Forex.
"""

def get_full_pmi_explanation() -> str:
    """Explication complète pour documentation ou formation"""
    parts = [
        PMI_INTRODUCTION,
        "\n\n" + QU_EST_CE_QUE_LE_PMI,
        "\n\nPublication :\n" + PUBLICATION_DU_PMI,
        "\n\nInterprétation et impact Forex :\n" + INTERPRETATION_ET_IMPACT_SUR_LE_FOREX,
        "\n\nStratégie trading :\n" + STRATEGIE_TRADING_AUTOUR_DU_PMI,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_PMI)
    ]
    return "".join(parts)


# Pour tester rapidement
if __name__ == "__main__":
    print(get_pmi_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_pmi_explanation())
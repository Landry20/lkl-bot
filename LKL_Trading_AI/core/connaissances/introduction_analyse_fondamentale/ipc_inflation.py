
"""
Indice des Prix à la Consommation (IPC / CPI)
Version : 1.0
Connaissances clés pour traders Forex sur l'inflation via l'IPC
"""

IPC_INTRODUCTION = """
L'Indice des Prix à la Consommation (IPC ou CPI en anglais) est l'indicateur le plus suivi 
pour mesurer l'inflation dans une économie.

Il calcule l'évolution du coût d'un panier fixe de biens et services représentatifs 
de la consommation des ménages (alimentation, logement, transport, santé, loisirs, etc.).

Objectif principal :
- Identifier si l'économie connaît de l'**inflation** (hausse des prix) 
  ou de la **déflation** (baisse des prix)
- Servir de référence principale pour les banques centrales dans leur politique monétaire
"""

IPC_DEFINITION_DETAILLEE = """
Calcul :
- Un panier de produits et services est défini (pondéré selon les habitudes de consommation)
- On mesure l'évolution moyenne des prix de ce panier d'un mois à l'autre et d'une année sur l'autre

Deux versions principales :
1. **IPC headline** (global) : inclut TOUS les postes, notamment alimentation et énergie
   → très volatil à cause des prix du pétrole, des produits agricoles, etc.

2. **IPC core** (sous-jacent) : exclut alimentation et énergie
   → plus stable, reflète mieux les pressions inflationnistes structurelles
   → souvent plus surveillé par les banques centrales (Fed, BCE, etc.)

Autres variantes importantes :
- PCE Price Index (Personal Consumption Expenditures) → préféré par la Fed
- HICP (Harmonized Index of Consumer Prices) → version européenne harmonisée
"""

IPC_PUBLICATION = """
Publication :
- **États-Unis** : mensuelle, par le Bureau of Labor Statistics (BLS)
  - Généralement le 2ᵉ ou 3ᵉ semaine du mois suivant (vers 14h30 GMT)
  - Exemple : IPC de mars publié mi-avril
- **Zone Euro** : mensuel (flash + final), par Eurostat
- **Royaume-Uni** : mensuel, par l'ONS
- **Australie** : trimestriel
- **Japon, Canada, etc.** : mensuel ou trimestriel selon le pays

La publication US est la plus impactante pour le Forex en raison du poids du dollar.
"""

IPC_IMPACT_SUR_LE_FOREX = """
Impact principal sur les devises :

Règle générale :
- **IPC plus élevé que prévu** → anticipation de resserrement monétaire (hausse des taux) → devise ↑
- **IPC plus faible que prévu** → anticipation d'assouplissement (baisse ou maintien des taux) → devise ↓

Nuances importantes :
- Si l'inflation est déjà très élevée → un IPC encore plus haut peut effrayer (crainte de récession) → parfois négatif
- Si l'économie est en déflation ou très faible inflation → un IPC plus haut est souvent bien accueilli
- Core CPI souvent plus déterminant que headline pour les décisions de banques centrales
- Surprise + écart important par rapport au consensus → très forte volatilité (50–200+ pips possibles en quelques minutes)
"""

STRATEGIE_TRADING_IPC = """
Stratégies autour de l'IPC :

1. Trading de la surprise (le plus courant) :
   - Attendre la publication
   - Comparer actual vs forecast vs previous
   - Direction immédiate : souvent alignée avec la surprise (IPC > forecast → devise ↑)

2. Approche pré-annonce :
   - Analyser le consensus (prévisions Bloomberg, Reuters, etc.)
   - Positionner en avance si biais très fort (risqué → spreads très larges)

3. Approche post-annonce :
   - Laisser passer les premières 1–5 minutes de folie
   - Observer la réaction réelle + niveaux techniques (supports/résistances, VWAP, etc.)
   - Entrer sur retracement ou continuation avec confirmation technique

Conseils de gestion du risque :
- Ne pas être en position juste avant la publication (spreads explosent)
- Utiliser des ordres stop / limit plutôt que du market
- Réduire fortement la taille de position (volatilité extrême)
- Combiner avec d'autres données (NFP, PMI, discours banquiers centraux)
"""

EXEMPLE_IPC_HISTORIQUE = """
Exemple concret – Mars 2021 (États-Unis) :
- Prévision : ~2.5 %
- Réel : 2.6 % (légère surprise à la hausse)
- Réaction immédiate : USD fort (hausse de l'USDX de ~0.4–0.6 % en quelques minutes)
- Ensuite : marché a digéré que la Fed resterait dovish en 2021 → USD a reperdu ses gains + faiblesse des rendements obligataires → USDX a chuté

Autre exemple classique :
- CPI US très fort (ex. +0.9 % m/m en 2022) → USD très fort, EURUSD sous 1.05, USDJPY vers 135+
"""

PRINCIPAUX_ENSEIGNEMENTS_IPC = [
    "L'IPC est l'indicateur numéro 1 de l'inflation grand public",
    "Core CPI est souvent plus important que headline pour les banques centrales",
    "Une surprise significative provoque une forte volatilité sur les paires majeures",
    "Éviter d'être positionné juste avant la publication (spreads et slippage)",
    "Regarder la réaction réelle du marché + niveaux techniques après les premières minutes",
    "L'impact dépend du contexte : inflation déjà haute ou basse, position de la banque centrale",
    "Utiliser en combinaison avec NFP, taux d'intérêt, PMI, discours de banquiers centraux"
    
]

def get_ipc_summary() -> str:
    """Résumé court pour notifications ou logs rapides"""
    return """
L'IPC (CPI) mesure l'inflation via un panier de biens et services.
- Headline : inclut tout (volatil)
- Core : hors alimentation & énergie (plus suivi)
→ IPC > attentes → hausse probable des taux → devise plus forte
→ IPC < attentes → politique plus souple → devise plus faible
Très forte volatilité attendue lors des publications US.
"""

def get_full_ipc_explanation() -> str:
    """Explication complète pour dashboard ou formation"""
    parts = [
        IPC_INTRODUCTION,
        "\n\n" + IPC_DEFINITION_DETAILLEE,
        "\n\nPublication : " + IPC_PUBLICATION,
        "\n\nImpact Forex :\n" + IPC_IMPACT_SUR_LE_FOREX,
        "\n\nStratégie :\n" + STRATEGIE_TRADING_IPC,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_IPC)
    ]
    return "".join(parts)

# Pour test rapide
if __name__ == "__main__":
    print(get_ipc_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_ipc_explanation())
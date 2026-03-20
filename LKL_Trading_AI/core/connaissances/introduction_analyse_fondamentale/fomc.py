
"""
FOMC - Federal Open Market Committee
Version : 1.0
Connaissances clés pour traders Forex sur le FOMC (Fed)
"""

FOMC_INTRODUCTION = """
Le **FOMC** (Federal Open Market Committee) est le principal organe décisionnel de la **Réserve fédérale américaine (Fed)** en matière de politique monétaire.

Il est considéré comme **l'événement le plus important du calendrier économique** pour les marchés financiers mondiaux, en particulier pour le dollar américain (USD) et toutes les paires impliquant l'USD.
"""

QU_EST_CE_QUE_LE_FOMC = """
**Composition** :
- 12 membres votants :
  - 7 membres du Board of Governors de la Fed (dont le Président et le Vice-Président)
  - Le Président de la Federal Reserve Bank de New York (vote permanent)
  - 4 Présidents des autres 11 Federal Reserve Banks (rotation annuelle)

**Mandat double** de la Fed (depuis 1977) :
- Maximum employment (plein emploi)
- Stabilité des prix (inflation autour de 2 % à long terme)

**Outils principaux** :
- Taux des fonds fédéraux (Fed Funds Rate)
- Forward guidance (communication sur les futures décisions)
- Quantitative Easing (QE) ou Quantitative Tightening (QT)
- Opérations d'open market
"""

CALENDRIER_ET_PUBLICATIONS_FOMC = """
**Réunions** :
- Généralement **8 réunions par an** (environ toutes les 6–7 semaines)
- Durée : 1 à 2 jours
- Annonce des décisions : **dernier jour à 14h00 ET** (19h00 GMT / 20h00 Paris)

**Éléments publiés à chaque réunion** :
1. **Décision sur les taux** (hausse, baisse, statu quo)
2. **Communiqué de politique monétaire** (Statement)
3. **Projections économiques** (Summary of Economic Projections – SEP) :
   - Dot Plot : graphique des prévisions individuelles des membres sur les taux futurs
   - Prévisions de PIB, chômage, inflation (PCE)
4. **Conférence de presse** du Président de la Fed (30 min après l’annonce) – souvent la partie la plus impactante

**Documents complémentaires** (3 semaines après) :
- Minutes de la réunion (détails des débats, divergences)

**Réunions sans conférence de presse** (souvent les réunions intermédiaires) → impact généralement moindre
"""

INTERPRETATION_DU_TON_FOMC = """
**Ton hawkish** (faucon) :
- Hausse des taux ou signal clair de hausses futures
- Inflation trop élevée → priorité à la lutte contre l’inflation
- Dot Plot montre des taux plus élevés que prévu
→ USD généralement **fort** (appréciation)

**Ton dovish** (colombe) :
- Maintien ou baisse des taux
- Forward guidance accommodante (« patient », « data-dependent » sans urgence)
- Dot Plot montre moins de hausses ou des baisses anticipées
→ USD généralement **faible** (dépréciation)

**Réactions marché** :
- Souvent plus fortes sur le **forward guidance** et le **dot plot** que sur le changement de taux lui-même
- La conférence de presse peut inverser ou amplifier la réaction initiale
"""

IMPACT_SUR_LE_FOREX = """
**Règles générales** :

- Décision hawkish + dot plot agressif + ton ferme → USD très fort (mouvements de 100–300 pips possibles sur EURUSD, USDJPY…)
- Décision dovish + dot plot doux → USD faible
- Statu quo mais guidance surprise → volatilité très élevée
- Pas de surprise → réaction limitée

**Paires les plus sensibles** :
- EURUSD, GBPUSD, USDJPY, USDCAD, AUDUSD, NZDUSD
- Gold (XAUUSD) souvent inverse au dollar
- Indices actions (S&P 500, Nasdaq) sensibles au ton

**Volatilité** :
- Spreads très élargis juste avant/après l’annonce
- Mouvements rapides dans les 5–30 premières minutes
- Souvent suivi d’un retracement ou d’un V-shape
"""

STRATEGIE_TRADING_FOMC = """
**Approches courantes** :

1. **Ne rien faire avant** (le plus sûr) :
   - Clôturer positions ou réduire exposition
   - Attendre 15–60 min après l’annonce + conférence

2. **Trading post-annonce** :
   - Attendre la première impulsion
   - Chercher retracement vers niveaux techniques (Fibonacci, pivots, support/résistance)
   - Entrer dans la direction dominante si confirmation

3. **Anticipation** (risquée) :
   - Analyser consensus + discours récents + dot plot précédent
   - Positionner sur straddle (options) ou ordres pendants

**Conseils de risque** :
- Pas de positions juste avant 14h00 ET
- Stops larges ou trailing stops
- Taille de position fortement réduite
- Attention aux fakeouts et à la conférence de presse
"""

PRINCIPAUX_ENSEIGNEMENTS_FOMC = [
    "Le FOMC est l'événement le plus important pour l'USD",
    "8 réunions par an + conférence de presse du Président",
    "Décision + communiqué + dot plot + projections + conférence = sources de volatilité",
    "Ton hawkish → USD ↑ ; ton dovish → USD ↓",
    "Le forward guidance et le dot plot souvent plus impactants que le taux lui-même",
    "Très forte volatilité → prudence extrême (spreads, gaps, fakeouts)",
    "Meilleure approche : attendre confirmation technique après l’annonce",
    "La conférence de presse peut tout changer",
    "Surveiller toujours le calendrier FOMC à l'avance"
]

def get_fomc_summary() -> str:
    """Résumé court pour notifications ou dashboard"""
    return """
FOMC = comité de politique monétaire de la Fed (8 réunions/an).
Décide des taux + forward guidance + dot plot.
→ Hawkish (anti-inflation) → USD fort
→ Dovish (pro-croissance) → USD faible
Annonce à 19h GMT + conférence de presse → volatilité massive.
"""

def get_full_fomc_explanation() -> str:
    """Explication complète pour documentation ou formation"""
    parts = [
        FOMC_INTRODUCTION,
        "\n\n" + QU_EST_CE_QUE_LE_FOMC,
        "\n\nCalendrier et publications :\n" + CALENDRIER_ET_PUBLICATIONS_FOMC,
        "\n\nInterprétation du ton :\n" + INTERPRETATION_DU_TON_FOMC,
        "\n\nImpact Forex :\n" + IMPACT_SUR_LE_FOREX,
        "\n\nStratégie trading :\n" + STRATEGIE_TRADING_FOMC,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_FOMC)
    ]
    return "".join(parts)


# Pour tester
if __name__ == "__main__":
    print(get_fomc_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_fomc_explanation())
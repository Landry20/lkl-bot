
"""
Introduction à la Macroéconomie - Rôle fondamental dans le trading Forex
Version : 2.0 - Cours détaillé et complet
"""

MACRO_INTRODUCTION = """
La macroéconomie est l'étude des phénomènes économiques à grande échelle : nations, régions, monde entier.
Elle analyse les agrégats comme le PIB, l’inflation, le chômage, la croissance, les taux d’intérêt, et les politiques publiques.

Pourquoi est-elle essentielle en trading Forex ?
- Les devises sont le reflet de la santé économique d’un pays : une économie forte attire les capitaux → devise apprécie
- Les annonces macro (NFP, CPI, PIB) provoquent 80 % de la volatilité journalière sur les paires majeures
- La macro donne le biais long terme : carry trade, safe havens, commodities currencies
- Sans macro, le trading technique seul est aveugle aux inversions soudaines (ex. guerre, récession)

Structure du cours macroéconomique :
1. Comprendre les bases et leur lien avec Forex
2. Indicateurs clés et comment ils bougent les marchés
3. Politiques monétaire et budgétaire
4. Cycles et crises
5. Application directe aux devises et stratégies
"""

ROLE_MACRO_TRADING = """
**Rôle pratique dans le trading** :
- Prévoir les réactions : CPI haut → anticipation de hausse de taux → USD fort
- Identifier les thèmes dominants : inflation 2022 → hawkish Fed → USD rally
- Hedger les risques : récession → long JPY/CHF, short AUD/NZD
- Combiner avec micro : macro donne direction, micro explique flux

Exemple concret :
Inflation US 8 % 2022 → Fed hawkish → USD index +20 %, EURUSD <0.95
Croissance Chine faible 2023 → AUD/NZD ↓ 10–15 %
"""

ERREURS_COMMUNES_MACRO = """
- Ignorer le consensus : c’est la surprise qui compte, pas le chiffre absolu
- Overtrading news : attendre confirmation technique après annonce
- Bias personnel : suivre les données, pas les opinions politiques
- Oublier interconnexions : PIB US fort → USD ↑, mais aussi pétrole ↑ → CAD ↑
"""

def get_macro_intro_summary():
    return """
Macroéconomie = étude agrégats (PIB, inflation, chômage). Essentielle Forex : annonces provoquent volatilité, donne biais long terme (carry, safe havens).
Exemple : CPI haut → USD ↑
"""

def get_full_macro_intro():
    return (
        MACRO_INTRODUCTION + "\n\n" +
        ROLE_MACRO_TRADING + "\n\n" +
        ERREURS_COMMUNES_MACRO
    )
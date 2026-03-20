
"""
Structure des Marchés - Liquidité, carnet d'ordres, HFT, stop hunting
Version : 2.0 - Cours détaillé pour trading Forex
"""

STRUCTURE_MARCHES_INTRO = """
La structure du marché explique comment les prix se forment réellement (pas seulement macro ou technique).

Concepts clés :
- Liquidité (profondeur du marché)
- Carnet d’ordres (order book)
- Acteurs (retail vs institutionnels)
- Manipulation (stop hunting, liquidity grab)
- Sessions et overlaps

Pour le bot LKL : comprendre la structure aide à éviter les pièges et à entrer aux bons endroits.
"""

LIQUIDITE_ET_PROFONDEUR = """
**Liquidité** : quantité d’ordres disponibles à chaque niveau de prix.
- Haute liquidité (EURUSD, USDJPY) → spreads serrés, exécution rapide
- Faible liquidité (exotics, week-end, news) → spreads larges, slippage, gaps

**Sessions liquidité** :
- Asia : faible (sauf AUD/NZD/JPY)
- London open (8h GMT) : liquidité ↑
- NY overlap (13h30–17h GMT) : max liquidité/volatilité
- NY close : baisse rapide

Règle LKL : éviter trades hors overlap sauf news majeure
"""

CARNET_D_ORDRES_ET_ACTEURS = """
**Carnet d’ordres** (order book) :
- Bids (achats) vs Asks (ventes)
- Zones d’accumulation : gros ordres institutionnels
- Iceberg orders : cachés par HFT/banques

**Acteurs dominants** :
- HFT / algos : 50–70 % volume Forex → chasse liquidité
- Banques : flux clients + proprietary
- Hedge funds : momentum, macro bets
- Retail : faible volume, mais clusters stops

Stop hunting : gros joueurs poussent prix vers zones retail stops (sous support, au-dessus résistance) → exécution puis reversal
"""

PIEGES_ET_LIQUIDITY_GRAB = """
**Liquidity grab** : prix va chercher stops / ordres pendants puis reversal
- Exemple : EURUSD descend sous 1.1000 (chasse stops) → remonte 100 pips

**Fakeout / false breakout** :
- Cassure niveau psychologique → piège → retour
- Très fréquent avant NFP/FOMC

**Wick hunting** : longues mèches pour liquider positions

Règle LKL :
- Ne jamais mettre stop sur niveau rond évident
- Attendre retest après cassure
- Entrer après liquidity grab (prix revient dans range)
"""

REGLES_TRADING_STRUCTURE_LKL = """
Règles bot :
- Trade seulement overlap London/NY (haute liquidité)
- Éviter exotics sauf news forte
- Stop jamais sur niveau rond → +10–15 pips au-delà
- Après fakeout → chercher entrée dans direction opposée
- Alert Telegram : "Liquidity grab détecté sur EURUSD 1.1000"
- Intégration : `analyse_technique/confirmation_technique.py` → valider après grab
"""

def get_structure_marches_summary():
    return """
Structure marchés : Haute liquidité = London/NY overlap.  
Stop hunting, liquidity grab, fakeouts = pièges classiques.
Règle : éviter stops ronds, entrer après grab.
"""

def get_full_structure_marches():
    return (
        STRUCTURE_MARCHES_INTRO + "\n\n" +
        LIQUIDITE_ET_PROFONDEUR + "\n\n" +
        CARNET_D_ORDRES_ET_ACTEURS + "\n\n" +
        PIEGES_ET_LIQUIDITY_GRAB + "\n\n" +
        REGLES_TRADING_STRUCTURE_LKL
    )
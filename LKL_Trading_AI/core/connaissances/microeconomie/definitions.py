
"""
Microéconomie - Concepts fondamentaux appliqués au trading Forex
Version : 2.0 - Version très détaillée pour compréhension profonde
"""

MICRO_INTRODUCTION = """
La microéconomie étudie les décisions individuelles et les interactions entre agents économiques (ménages, entreprises, investisseurs, spéculateurs, institutions).

Contrairement à la macroéconomie (PIB, inflation, chômage), la microéconomie regarde :
- Comment les prix se forment
- Comment l’offre et la demande interagissent
- Comment les agents réagissent aux incitations (prix, taux, risques, informations)

En trading Forex, la microéconomie explique :
- Pourquoi une paire monte ou descend à court/moyen terme
- Les flux réels de capitaux (pas seulement les annonces macro)
- Les comportements des gros joueurs (banques, hedge funds, algos)
- Les inefficiences et opportunités que l’on peut exploiter
"""

OFFRE_ET_DEMANDE_DEVISES = """
**Offre de devises** (ce qui fait baisser le prix d’une devise) :
- Exportations du pays → entrée de devises étrangères
- Vente d’actifs par des non-résidents (sortie de capitaux)
- Tourisme sortant (demande de devises étrangères)
- Remboursement de dette en devises étrangères
- Intervention banque centrale (vente de sa propre devise)
- Spéculation baissière (short massifs par hedge funds)

**Demande de devises** (ce qui fait monter le prix d’une devise) :
- Importations → besoin de payer en devises étrangères
- Investissements entrants (carry trade, achat d’actions/obligations)
- Tourisme entrant
- Remboursement de dette par des étrangers (entrée de devises)
- Intervention banque centrale (achat de sa propre devise)
- Spéculation haussière (longs massifs)

Exemple concret :
AUDUSD monte quand la Chine achète beaucoup de minerai australien → demande AUD ↑
USDJPY monte quand les fonds japonais achètent des Treasuries US → demande USD ↑
"""

ELASTICITE_DANS_LE_FOREX = """
**Élasticité-prix** : réaction de la quantité demandée ou offerte à un changement de prix.

En Forex :
- Carry trade très élastique : +0.5% différentiel taux → flux massifs vers devise haute rendement
- Safe havens peu élastiques : même si taux bas, USD/JPY/CHF montent en panique (demande inélastique)
- Commodities currencies (AUD, CAD, NZD) élastiques aux prix matières premières : +10% pétrole → CAD très fort

**Élasticité-revenu** :
- Croissance forte Chine → demande AUD ↑ (élasticité élevée)
- Récession US → demande USD ↓ pour imports (élasticité positive)

**Élasticité croisée** :
- Pétrole ↑ → CAD ↑ → USDCAD ↓
- Or ↑ → AUD ↑ (Australie gros producteur) → AUDUSD ↑
"""

AGENTS_ECONOMIQUES_ET_LEUR_IMPACT = """
1. Banques centrales → interviennent directement (achat/vente devises)
2. Banques commerciales → flux clients (import/export), hedging, carry
3. Hedge funds & CTAs → momentum, trend following, macro bets
4. Entreprises multinationales → hedging naturel (paiements fournisseurs)
5. Tourisme & migrants → flux faibles mais constants
6. Retail traders → faible volume individuel, mais amplification via brokers

Exemple :
Hedge funds vendent massivement EUR en 2022 (guerre + énergie) → EURUSD < 0.95
Tourisme US vers Europe → demande EUR ↑ (mais effet faible)
"""

PSYCHOLOGIE_MICRO = """
- Anchoring : traders fixés sur niveaux ronds (1.2000, 150.00)
- Availability bias : sur-réaction aux news récentes (NFP fort → USD fort même si macro faible)
- Herding : tout le monde suit la même direction → overshoot puis reversal
- Loss aversion : stops chassés avant vrai mouvement
"""

def get_micro_definitions_summary():
    return """
Microéconomie Forex : Offre/Demande devises, élasticité (carry, safe havens, commodities), agents (banques, hedge funds, entreprises), psychologie (herding, anchoring).
"""

def get_full_micro_definitions():
    return (
        MICRO_INTRODUCTION + "\n\n" +
        OFFRE_ET_DEMANDE_DEVISES + "\n\n" +
        ELASTICITE_DANS_LE_FOREX + "\n\n" +
        AGENTS_ECONOMIQUES_ET_LEUR_IMPACT + "\n\n" +
        PSYCHOLOGIE_MICRO
    )
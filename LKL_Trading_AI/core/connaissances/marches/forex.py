
"""
Cours Complet sur le Marché Forex - Caractéristiques, Définitions, Impacts et Facteurs de Mouvement
Version : 2.0 - Étendu pour LKL Bot (Détails sur paires, volatilité, news, géopolitique, macro)
Adapté Landry Abidjan GMT - Focus EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD
"""

FOREX_INTRODUCTION = """
Le marché Forex (Foreign Exchange) est le plus grand marché financier mondial : 
- Volume quotidien : ~7.5 trillions USD (2026)
- 24h/5j (Sydney open lundi 21h GMT → NY close vendredi 21h GMT)
- Acteurs : banques centrales (20%), hedge funds (30%), corporates (15%), retail (10%), algos/HFT (25%)
- Avantages : liquidité extrême, leverage haut (1:500+), coûts bas (spreads 0.1-1 pip majors)
- Risques : leverage tue, news spikes, slippage NFP/FOMC

Définitions clés :
- Pip : unité mouvement (4e décimale majors, 2e yen) ex. EURUSD 1.1000 → 1.1001 = +1 pip
- Lot : 100k unités base (standard), 10k (mini), 1k (micro)
- Marge : dépôt requis (ex. 1% pour 1:100 leverage)
- Swap : intérêt carry trade (positif long AUDUSD, négatif short USDJPY)
- Majors : USD pairs (70% volume) - EURUSD, GBPUSD, USDJPY, USDCAD, AUDUSD, NZDUSD, USDCHF
- Crosses : non-USD (EURGBP, GBPJPY)
- Exotics : emerging (USDTRY, USDMXN) - volatilité haute, spreads larges
"""

PAIRES_FOREX_IMPACTS = {
    "EURUSD": {
        "caracteristiques": "Plus liquide (28% volume global), faible volatilité moyenne (50-80 pips/jour), corrélée inverse à USD strength",
        "facteurs_mouvement": [
            "Macro US/EU : NFP fort → EURUSD ↓ (USD ↑), PMI Euro faible → EURUSD ↓",
            "Géopolitique : Guerre Ukraine/Russie → EUR ↓ (gaz, instabilité)",
            "Politique monétaire : FOMC hawkish → EURUSD ↓, BCE dovish → EURUSD ↓",
            "Saisonnalité : Fin année fiscale → repatriation USD ↑ → EURUSD ↓",
            "Exemple 2022 : Guerre Ukraine → EURUSD < 0.95 (parité brisée)",
            "Exemple 2024 : Fed cuts → EURUSD > 1.12"
        ]
    },
    "GBPUSD": {
        "caracteristiques": "Haute volatilité (80-150 pips/jour), 'Cable', sensible UK news",
        "facteurs_mouvement": [
            "Brexit legacy : GBP faible long terme vs pré-2016",
            "Macro UK : Retail Sales faible → GBPUSD ↓, BoE hawkish → GBPUSD ↑",
            "Géopolitique : Tensions EU/UK (Irlande) → GBP ↓",
            "Énergie : GBP corrélé pétrole (North Sea) → Brent ↑ → GBPUSD ↑",
            "Exemple 2022 : Truss budget crisis → GBPUSD 1.03 (all-time low)"
        ]
    },
    "USDJPY": {
        "caracteristiques": "Carry trade favori, volatilité moyenne (60-120 pips), safe haven JPY",
        "facteurs_mouvement": [
            "Différentiel taux : Fed haut vs BoJ 0% → USDJPY ↑",
            "Risk-off : Crises globales → JPY ↑ (USDJPY ↓)",
            "Géopolitique : Tensions Corée/Asie → JPY ↑",
            "Interventions BoJ : Si USDJPY > 160 → vente USD massive",
            "Exemple 2022 : Guerre Ukraine → USDJPY 150+ (carry + risk-on USD)"
        ]
    },
    "AUDUSD": {
        "caracteristiques": "Commodity currency, volatile (70-120 pips), corrélé Chine/Aussie exports",
        "facteurs_mouvement": [
            "Matières : Fer/cuivre/or ↑ → AUD ↑ (Chine 40% exports)",
            "Macro Chine : PMI Caixin faible → AUDUSD ↓",
            "Géopolitique : Tensions US-Chine → AUD ↓",
            "RBA vs Fed : Différentiel haut → carry trade AUDUSD long",
            "Exemple 2020 : COVID China lockdown → AUDUSD 0.55 low"
        ]
    },
    "USDCAD": {
        "caracteristiques": "Commodity (pétrole), faible volatilité (50-90 pips), 'Loonie'",
        "facteurs_mouvement": [
            "Pétrole : WTI ↑ → CAD ↑ (USDCAD ↓)",
            "Macro Canada : Employment faible → USDCAD ↑",
            "Géopolitique : Tensions OPEC → pétrole ↑ → USDCAD ↓",
            "BoC vs Fed : Sync souvent (NAFTA) mais Fed lead",
            "Exemple 2022 : Guerre Ukraine pétrole spike → USDCAD 1.25 low"
        ]
    }
}

STRATEGIE_FOREX_LKL = """
**Règles LKL Bot Forex** :
- Scalping 5-15min : London open 8h GMT Abidjan
- News trading : Pause 15min avant NFP/FOMC, filtre volatilité >100 pips
- Carry : Long AUDJPY/NZDUSD si risk-on + différentiel >2%
- Géopolitique filter : Guerre → flat AUD/CAD, long USD/JPY
- Backend auth : Envoyer analyse macro + impact pair avant exécution
- Dashboard Telegram : Alert 'EURUSD Impact: NFP surprise +50k → Target 1.1050'
"""

def get_forex_summary() -> str:
    return """
Forex : 7.5T$/jour, 24/5. Majors USD-centriques. Impacts : macro/news (NFP ↓ → USD ↓), géopolitique (guerre → USD/JPY ↑), matières (pétrole ↑ → CAD ↑).
Paires LKL : EURUSD liquide, GBPUSD volatile, USDJPY carry.
"""

def get_full_forex_explanation() -> str:
    lines = [FOREX_INTRODUCTION, "\n\nPaires et Impacts :\n"]
    for pair, data in PAIRES_FOREX_IMPACTS.items():
        lines.append(f"► {pair}")
        lines.append(f"   Caractéristiques : {data['caracteristiques']}")
        lines.append("   Facteurs Mouvement :")
        for item in data['facteurs_mouvement']:
            lines.append(f"     - {item}")
        lines.append("")
    lines.append("\nStratégie LKL Bot :\n" + STRATEGIE_FOREX_LKL)
    return "\n".join(lines)
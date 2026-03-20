
"""
Indices US (US30, NAS100, SPX500) - Caractéristiques, impacts Forex et règles LKL Bot
Version : 2.0 - Cours détaillé
"""

INDICES_US_INTRODUCTION = """
Les indices US (Dow Jones US30, Nasdaq NAS100, S&P 500 SPX500) sont des baromètres mondiaux du risque et de la croissance.

Ils ont une corrélation forte avec le sentiment macro et influencent indirectement le Forex :
- Risk-on (indices ↑) → devises high-beta ↑ (AUD, NZD, CAD)
- Risk-off (indices ↓) → refuges ↑ (USD, JPY, CHF, or)
- Volatilité indices → volatilité Forex amplifiée

LKL Bot : 10 % allocation possible (US30 le plus utilisé)
"""

CARACTERISTIQUES_PRINCIPALES = """
1. **US30 (Dow Jones Industrial Average)**  
   - 30 grandes entreprises industrielles et financières  
   - Moins tech, plus cyclique → sensible à l’économie réelle  
   - Volatilité moyenne : 200–600 points/jour  

2. **NAS100 (Nasdaq 100)**  
   - Tech-heavy (Apple, Microsoft, Nvidia, Tesla, Amazon)  
   - Très sensible aux taux d’intérêt (tech = croissance future)  
   - Volatilité haute : 300–1000 points/jour  

3. **SPX500 (S&P 500)**  
   - 500 entreprises → mix équilibré  
   - Le plus représentatif de l’économie US  
   - Volatilité moyenne : 30–80 points/jour
"""

FACTEURS_DE_MOUVEMENT = """
1. **Macro US** : NFP fort → indices ↑ (Goldilocks), CPI haut → indices ↓ (crainte hikes)  
2. **Taux d’intérêt** : Real yields ↑ → tech ↓ (NAS100 sensible)  
3. **Sentiment risque** : VIX ↑ → indices ↓ → USD/JPY/CHF ↑  
4. **Géopolitique** : Guerre → indices ↓ initial → USD ↑ refuge  
5. **Earnings season** : Résultats tech → NAS100 ±5–10 % en semaine  
6. **FOMC** : Hawkish → indices ↓ (taux hauts), Dovish → indices ↑  
7. **Carry trade unwind** : Risk-off → indices crash → JPY ↑ fort
"""

CORRELATIONS_FOREX_CLES = """
- Indices ↑ (risk-on) → AUDUSD, NZDUSD, CADUSD ↑ | USDJPY ↓  
- Indices ↓ (risk-off) → USDJPY ↑, EURCHF ↓, AUDUSD ↓  
- NAS100 sensible aux taux : Fed hawkish → NAS100 ↓ → USD ↑  
- US30 corrélé pétrole : Pétrole ↑ → US30 ↑ → CAD ↑ (USDCAD ↓)  

Exemples historiques :
- Mars 2020 COVID crash : SPX -34 %, NAS100 -30 % → USD/JPY ↑, AUDUSD 0.55  
- 2022 bear market : Fed hikes → NAS100 -35 % → USD rally  
- 2024 AI boom : NAS100 +50 % → risk-on → AUD/NZD ↑
"""

REGLES_TRADING_LKL = """
Règles bot :
- US30 > 40000 + VIX <18 → risk-on → long AUDUSD/NZDUSD  
- NAS100 breakout ATH + Fed dovish → augmenter exposition carry  
- VIX >35 + indices -3 % jour → flat high-beta, long USD/JPY/CHF  
- Alert Telegram : "US30 -500 pts + VIX spike → RISK-OFF"  
- Corrélation inverse or : US30 ↓ → XAUUSD ↑ → hedge long or  
- Allocation : max 10 % sur US30, éviter NAS100 sauf trend clair
"""

def get_indices_us_summary():
    return """
Indices US : Risk-on → AUD/NZD/CAD ↑ | Risk-off → USD/JPY/CHF ↑  
US30 cyclique, NAS100 tech, SPX500 équilibré.
VIX >35 → refuges, VIX <15 → carry trade.
"""

def get_full_indices_us():
    return (
        INDICES_US_INTRODUCTION + "\n\n" +
        CARACTERISTIQUES_PRINCIPALES + "\n\n" +
        FACTEURS_DE_MOUVEMENT + "\n\n" +
        CORRELATIONS_FOREX_CLES + "\n\n" +
        REGLES_TRADING_LKL
    )
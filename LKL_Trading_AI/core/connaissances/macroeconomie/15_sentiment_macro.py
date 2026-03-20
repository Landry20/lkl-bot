
"""
Sentiment Macro Global - VIX, Spreads de crédit, Fear & Greed, etc.
Version : 2.0 - Cours détaillé pour le bot LKL
"""

SENTIMENT_MACRO_INTRODUCTION = """
Le sentiment macro mesure la peur / l’appétit au risque sur les marchés financiers mondiaux.

Il complète la macro pure (PIB, inflation) en donnant des signaux avancés :
- Quand la peur monte → risk-off → devises refuge (USD, JPY, CHF) ↑
- Quand l’appétit domine → risk-on → devises high-beta (AUD, NZD, CAD) ↑

Principaux indicateurs de sentiment macro :
- VIX (indice de peur)
- Spreads de crédit
- Indices Fear & Greed
- TED Spread
- MOVE Index (volatilité obligataire)
"""

VIX_INDICE_DE_PEUR = """
**VIX** (CBOE Volatility Index) : volatilité implicite S&P 500 sur 30 jours
- < 15 : très faible peur → risk-on extrême
- 15–20 : normal
- 20–30 : anxiété croissante
- > 30 : peur élevée → risk-off
- > 40 : panique (crise)

Impact Forex :
- VIX ↑ → USD/JPY/CHF ↑, AUD/NZD/CAD ↓
- VIX > 35 → pause trading ou long refuges seulement
- Exemple : Mars 2020 COVID → VIX 82 → USDJPY crash puis rebond, AUDUSD 0.55

Règle LKL :
- VIX > 30 + news géopolitique → alerte Telegram "RISK-OFF DÉTECTÉ"
- VIX < 15 + carry trade → augmenter taille AUDJPY/NZDUSD
"""

SPREADS_DE_CREDIT = """
**Spreads de crédit** : écart rendement obligations corporate vs Treasuries US
- Spreads élargis → peur de défaut → risk-off
- Spreads serrés → confiance → risk-on

Indicateurs clés :
- High Yield Spread (junk bonds vs Treasuries)
- Investment Grade Spread
- TED Spread (LIBOR vs T-Bills) → stress bancaire

Impact Forex :
- Spreads ↑ → USD ↑ (refuge), AUD/NZD ↓
- TED Spread > 50 bps → risque systémique → JPY/CHF ↑ fort

Exemple :
2008 crise subprime → spreads explosent → USD/JPY ↑ massif (carry unwind)
2023 SVB faillite → TED ↑ → USD ↑ temporaire
"""

FEAR_AND_GREED_INDEX = """
**CNN Fear & Greed Index** (actions US) :
- Extreme Fear (<20) → capitulation → bottom potentiel
- Extreme Greed (>80) → euphorie → top potentiel

Impact Forex :
- Extreme Fear → USD/JPY/CHF ↑
- Extreme Greed → AUD/NZD/CAD ↑

Règle LKL :
- Fear & Greed < 25 → préparer longs refuges
- > 75 → préparer shorts high-beta
"""

MOVE_INDEX = """
**MOVE Index** : volatilité obligataire US (équivalent VIX pour Treasuries)
- MOVE ↑ → stress taux → USD ↑, or ↑
- Utile quand VIX est bas mais obligations stressées
"""

REGLES_TRADING_SENTIMENT_LKL = """
Règles automatiques bot :
- VIX > 35 → flat AUD/NZD/CAD, long USD/JPY/CHF/or
- VIX < 15 + carry différentiel > 3 % → long AUDJPY/NZDUSD
- Spreads crédit +100 bps en 1 semaine → alerte risk-off
- Fear & Greed + VIX + TED combinés → score risque macro (0–100)
- Backend : envoie score risque au Laravel pour validation trade
"""

def get_sentiment_macro_summary():
    return """
Sentiment macro : VIX ↑ → risk-off → USD/JPY/CHF ↑  
Spreads crédit ↑ → USD ↑  
Fear & Greed extrême → capitulation/euphorie → opportunités contraires
"""

def get_full_sentiment_macro():
    return (
        SENTIMENT_MACRO_INTRODUCTION + "\n\n" +
        VIX_INDICE_DE_PEUR + "\n\n" +
        SPREADS_DE_CREDIT + "\n\n" +
        FEAR_AND_GREED_INDEX + "\n\n" +
        MOVE_INDEX + "\n\n" +
        REGLES_TRADING_SENTIMENT_LKL
    )

"""
Flux de capitaux - Risk-On / Risk-Off / Carry Trade
Version : 2.0 - Très détaillé avec exemples concrets et impacts paires
"""

FLUX_CAPITAUX_INTRODUCTION = """
Les flux de capitaux sont les mouvements réels d’argent entre pays et entre actifs.
Ils expliquent 70–80 % des mouvements de devises à moyen terme (pas seulement les annonces macro).

Trois grands types de flux dominants en Forex :
1. Flux risk-on / risk-off (appétit / aversion au risque)
2. Flux carry trade (chasse au rendement)
3. Flux safe-haven (fuite vers la sécurité)
"""

RISK_ON_RISK_OFF_DETAILLE = """
**Risk-On** (appétit pour le risque) :
- Caractéristiques : marchés haussiers, VIX bas (<20), spreads crédit serrés
- Gagnants : devises high-beta (AUD, NZD, CAD), emerging markets (TRY, ZAR, MXN), actions, crypto
- Perdants : safe havens (USD, JPY, CHF, or en phase initiale)
- Paires qui montent fort :
  - AUDUSD, NZDUSD, CADUSD
  - EURJPY, GBPJPY, AUDJPY (carry + risk-on)
  - USDMXN, USDZAR (carry emerging)

**Risk-Off** (aversion au risque) :
- Caractéristiques : VIX >30, spreads crédit larges, ventes panique actions
- Gagnants : USD (devise de réserve), JPY (carry unwinding), CHF, or, Treasuries US
- Perdants : tout ce qui est risqué (AUD, NZD, CAD, emerging currencies)
- Paires qui bougent :
  - USDJPY ↑ (carry unwind + JPY refuge)
  - EURCHF ↓ (CHF refuge)
  - AUDUSD, NZDUSD ↓ très fort
  - USDCAD ↑ (CAD commodity + risk-off)

Exemples historiques :
- Mars 2020 COVID crash → Risk-Off extrême : USDJPY 102 → 102 (puis rebound), AUDUSD 0.55 low
- 2022 Guerre Ukraine + inflation → Risk-On initial (USD fort carry), puis Risk-Off (JPY + CHF ↑)
"""

CARRY_TRADE_EXPLIQUE = """
**Carry Trade** = emprunter devise à faible taux → investir dans devise à haut taux

Exemples classiques :
- Emprunter JPY (0–0.25%) → acheter AUD (3–4.5%) → AUDJPY long
- Emprunter CHF/EUR → acheter NZD ou MXN

Conditions favorables :
- Différentiel taux > 2–3 %
- Volatilité faible (pas de gros risk-off)
- Sentiment risk-on dominant

Risques majeurs :
- Sudden stop : risk-off → unwind massif (carry unwind)
- Hausse taux pays financement (JPY ↑ → carry coûteux)
- Intervention banque centrale (BoJ vend USDJPY)

Exemple 2008 : Carry unwind massif → JPY +30% en quelques mois
Exemple 2022–2023 : Carry USDJPY très rentable (Fed 5.5% vs BoJ 0%)
"""

SAFE_HAVEN_FLOWS = """
Devises / actifs refuge quand panique :
1. USD (devise de réserve mondiale)
2. JPY (carry unwind + rapatriement Japon)
3. CHF (neutralité suisse)
4. Or (anti-fiat, anti-banques)

Quand ça arrive :
- Guerres (Ukraine 2022 → USD + JPY + or)
- Crises financières (2008 → USD + JPY)
- Crises dette souveraine (2011 → CHF fort → SNB plancher 1.20)

Exemple : Crise SVB 2023 → USD + JPY + CHF ↑ rapide
"""

def get_flux_capitaux_summary():
    return """
Flux capitaux : 
Risk-On → AUD/NZD/CAD ↑, USD/JPY ↓ 
Risk-Off → USD/JPY/CHF ↑, AUD/NZD ↓ 
Carry → AUDJPY/NZDUSD long si différentiel taux + faible vol
Safe-haven → USD/JPY/CHF/or en panique
"""

def get_full_flux_capitaux():
    return (
        FLUX_CAPITAUX_INTRODUCTION + "\n\n" +
        RISK_ON_RISK_OFF_DETAILLE + "\n\n" +
        CARRY_TRADE_EXPLIQUE + "\n\n" +
        SAFE_HAVEN_FLOWS
    )
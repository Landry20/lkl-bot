
"""
Matières Premières Macro - Pétrole, Gaz, Cuivre, Fer – Impact devises
Version : 2.0 - Cours détaillé
"""

COMMODITIES_INTRO = """
Les matières premières influencent fortement les devises commodity (AUD, CAD, NOK, NZD, RUB, CLP, ZAR).

Règle générale :
Prix commodity ↑ → exportateur ↑ → devise ↑
Prix commodity ↓ → exportateur ↓ → devise ↓
"""

PRINCIPALES_COMMODITIES_ET_DEVISES = """
1. **Pétrole (WTI/Brent)** :
   - Devises : CAD (Canada), NOK (Norvège), RUB (Russie)
   - Impact : +10 $ → CAD ↑ 0.5–1 %, USDCAD ↓
   - Exemple : 2022 guerre → pétrole 130 $ → USDCAD <1.25

2. **Gaz naturel** :
   - Devises : EUR (import), NOK (export), RUB
   - Impact : Prix gaz ↑ → NOK ↑, EUR ↓ (crise énergie)

3. **Cuivre** (Dr Copper – indicateur croissance) :
   - Devises : AUD (Australie), CLP (Chili), CNY
   - Impact : Cuivre ↑ → AUDUSD ↑ (Chine demande)

4. **Minerai de fer** :
   - Devises : AUD (Australie gros export)
   - Impact : Fer ↑ → AUDUSD ↑

5. **Or** :
   - Pas commodity classique → refuge + inflation hedge
   - Lien macro : real rates bas → or ↑

6. **Blé, soja** :
   - Devises : CAD, UAH (Ukraine), RUB
   - Impact limité sauf guerre (2022 blé ↑ → CAD ↑ léger)
"""

FACTEURS_MACRO_INFLUENCANT_COMMODITIES = """
- Croissance Chine : 60–70 % demande cuivre/fer → AUD sensible
- Dollar index : USD ↑ → commodities ↓ (prix en USD)
- Inflation : Commodities ↑ → inflation coûts
- Géopolitique : Guerres Moyen-Orient → pétrole ↑ → CAD ↑
- OPEP+ : Coupes production → pétrole ↑ → CAD/NOK ↑
"""

REGLES_TRADING_LKL = """
- Pétrole +5 % jour → long USDCAD, short EURUSD
- Cuivre breakout ATH → long AUDUSD
- Chine PMI >52 + fer ↑ → AUD/NZD call
- Filtre bot : Brent >90 $ → alerte CAD strength
"""

def get_commodities_summary():
    return """
Commodities macro : Pétrole ↑ → CAD/NOK ↑ | Cuivre/Fer ↑ → AUD ↑ | Gaz ↑ → NOK ↑, EUR ↓
Chine croissance + OPEP+ = clés.
"""

def get_full_commodities():
    return (
        COMMODITIES_INTRO + "\n\n" +
        PRINCIPALES_COMMODITIES_ET_DEVISES + "\n\n" +
        FACTEURS_MACRO_INFLUENCANT_COMMODITIES + "\n\n" +
        REGLES_TRADING_LKL
    )

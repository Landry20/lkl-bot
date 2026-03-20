
"""
Pétrole (WTI / Brent) - Caractéristiques, facteurs de mouvement, impact Forex
Version : 2.0 - Cours détaillé
"""

PETROLE_INTRODUCTION = """
Le pétrole (WTI, Brent) est la commodity la plus influente sur le Forex après l’or.

Il impacte directement :
- CAD (Canada exportateur)
- NOK (Norvège)
- RUB (Russie)
- Indirectement : USD (inflation), EUR (importateur net), GBP (North Sea)

LKL Bot : surveiller pétrole comme proxy macro + risque géopolitique
"""

CARACTERISTIQUES_PETROLE = """
- WTI : pétrole US (Texas) – plus volatil, stockage Cushing
- Brent : pétrole international (Mer du Nord) – référence mondiale
- Volatilité : 1–5 $/jour normal, 10–30 $ en crise
- Unités : baril (bbl), contrats futures NYMEX/ICE
- Marché 24h : Asia → London → NY
"""

FACTEURS_DE_MOUVEMENT = """
1. **OPEP+** : Coupes production → pétrole ↑ | Quotas ↑ → ↓  
2. **Géopolitique** : Guerres Moyen-Orient (Ormuz, Yémen) → spike ↑  
3. **Demande** : Croissance Chine/US → ↑ | Récession → ↓  
4. **Dollar** : USD ↑ → pétrole ↓ (prix en USD)  
5. **Stocks US** (EIA weekly) : Drawdowns → ↑ | Builds → ↓  
6. **Saisonnalité** : Été US → demande ↑ | Hiver → gaz concurrence  
7. **Transition énergétique** : Long terme ↓ pression (EV, renouvelables)

Exemples :
- 2022 guerre Ukraine → Brent 130 $ → CAD ↑ massif, USDCAD <1.25  
- 2020 COVID → pétrole négatif → CAD crash  
- 2024–2025 OPEP+ coupes → Brent 80–90 $ → CAD stable fort
"""

IMPACTS_FOREX = """
- Pétrole +10 $ → CAD ↑ 0.5–1.5 % (USDCAD ↓)  
- Pétrole ↑ + inflation → Fed hawkish → USD ↑ (contrebalancé)  
- Pétrole spike géopolitique → NOK ↑, EUR ↓ (importateur)  
- Pétrole bas prolongé → CAD faible, inflation basse → dovish BoC  
- Corrélation inverse USD : pétrole ↑ → USD ↓ léger (demande globale)

Paires sensibles :
- USDCAD : corrélation -0.7 à -0.9 avec WTI
- EURUSD : pétrole ↑ → EUR ↓ (énergie)
- NOK (EURNOK, USDNOK) : pétrole ↑ → NOK ↑
"""

REGLES_TRADING_LKL = """
Règles bot :
- Brent +5 % jour → long USDCAD, short EURUSD  
- Pétrole >90 $ + géopolitique → alerte CAD strength  
- EIA stocks drawdown surprise → USD/CAD call  
- Pétrole <60 $ prolongé → short CAD pairs  
- Filtre : OPEC+ news → pause trading 1h si spike >8 %
- Corrélation : Vérifier USDCAD vs WTI avant trade CAD
"""

def get_petrole_summary():
    return """
Pétrole : OPEP+/géopolitique/demande → ↑ ou ↓  
Impact : CAD/NOK ↑ fort, EUR ↓, USD mixte (inflation).
Brent >90 $ → CAD call, <60 $ → CAD short.
"""

def get_full_petrole():
    return (
        PETROLE_INTRODUCTION + "\n\n" +
        CARACTERISTIQUES_PETROLE + "\n\n" +
        FACTEURS_DE_MOUVEMENT + "\n\n" +
        IMPACTS_FOREX + "\n\n" +
        REGLES_TRADING_LKL
    )
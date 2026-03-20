
"""
Calendrier Économique - Événements majeurs, horaires, volatilité attendue
Version : 2.0 - Cours détaillé pour le bot LKL
"""

CALENDRIER_INTRODUCTION = """
Le calendrier économique est la **carte de navigation** du trader fondamental.
Il liste toutes les annonces macro importantes avec :
- Date et heure (fuseau GMT ou Abidjan GMT)
- Pays / devise impactée
- Indicateur concerné
- Consensus (attentes des économistes)
- Importance (low / medium / high)

Pour le bot LKL :
- Les événements "high impact" = pause trading ou réduction risque
- Surprise vs consensus = principal déclencheur de mouvement
"""

PRINCIPAUX_EVENEMENTS_ET_VOLATILITE = """
Événements high impact (volatilité potentielle 100–400 pips) :
1. NFP (Non-Farm Payrolls) – US – 1er vendredi 13h30 GMT
2. CPI / Core CPI – US – mensuel 13h30 GMT
3. FOMC Decision + Dot Plot + Conférence Powell – 8×/an 19h00 GMT
4. PIB US (Advance) – trimestriel 13h30 GMT
5. BCE Rate Decision + Lagarde Press – 8×/an 13h45–14h30 GMT
6. BoE Rate Decision + Conférence – 8×/an
7. RBA / BoC / RBNZ Rate Decisions – impact AUD/CAD/NZD

Événements medium impact (50–150 pips) :
- PMI Flash (US, Eurozone, UK, Chine)
- Retail Sales US/EU
- Employment Change AU/CA
- ZEW / IFO Allemagne

Règles de volatilité pour LKL Bot :
- High impact US → pause 15–30 min avant/après
- High impact non-US → réduction taille position 50 %
- Plusieurs high impact le même jour → flat ou micro-lots
- Consensus très aligné → volatilité faible même sur high impact
"""

FUSEAU_ABIDJAN_ET_HORAIRES_OPTIMAUX = """
Abidjan = GMT (pas de changement heure d’été)
Horaires clés pour trading :
- London open : 8h GMT → EUR/GBP volatilité
- NY open : 13h30 GMT → US news + overlap max volatilité
- Asia session : 00h–08h GMT → faible sauf AUD/NZD/JPY news

Exemple planning LKL :
- 13h–17h GMT : zone rouge (NFP, CPI, FOMC possible)
- 8h–12h GMT : zone orange (Europe PMI, UK data)
"""

REGLES_AUTOMATIQUES_BOT = """
- 30 min avant high impact → bloquer nouveaux trades
- Après annonce → attendre 5–15 min confirmation technique
- Si écart > 20 % vs consensus → alerte Telegram + analyse impact pair
- Calendrier chargé (FOMC + NFP même semaine) → risque max 0.5 %/trade
"""

def get_calendrier_summary():
    return """
Calendrier économique : high impact = NFP, CPI, FOMC, PIB, BCE → 100–400 pips possibles.
Abidjan GMT : pause 30 min avant US high impact.
"""

def get_full_calendrier():
    return (
        CALENDRIER_INTRODUCTION + "\n\n" +
        PRINCIPAUX_EVENEMENTS_ET_VOLATILITE + "\n\n" +
        FUSEAU_ABIDJAN_ET_HORAIRES_OPTIMAUX + "\n\n" +
        REGLES_AUTOMATIQUES_BOT
    )
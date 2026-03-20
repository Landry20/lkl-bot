# knowledge/savoir/geopolitique/evenements_historiques.py
"""
Événements géopolitiques historiques majeurs - Leçons Forex
Version : 2.0
"""

EVENEMENTS_HISTORIQUES = """
1. Crise des missiles Cuba 1962 → USD/JPY/CHF ↑, gold ↑
2. Guerre du Kippour + embargo OPEP 1973 → pétrole ×4 → CAD/NOK ↑ futur, inflation ↑
3. Crise Iran otages 1979-1981 → or 850$ ATH, USD fort
4. Guerre Golfe 1990 → pétrole spike → USD ↑, CAD ↑
5. 11 septembre 2001 → USD ↑ refuge, or ↑
6. Guerre Irak 2003 → pétrole ↑, USD ↑ initial puis ↓ (coût guerre)
7. Crise dette grecque 2010-2012 → EUR ↓ massif, CHF ↑ (SNB plancher 1.20)
8. Brexit 2016 → GBP -15% en jours, USD ↑
9. Guerre commerciale US-Chine 2018-2020 → CNY ↓, AUD ↓, USD ↑
10. Invasion Ukraine 2022 → EUR <0.95, RUB crash, pétrole 130$, or 2070$, JPY ↑ carry unwind
11. Conflit Israël-Hamas 2023-2025 → pétrole ↑, or ↑, USD ↑ refuge
"""

LECONS_TRADING = """
Leçons pour LKL Bot :
- Guerres Moyen-Orient → pétrole ↑ → CAD long, EUR short
- Conflits Europe/Asie → JPY/CHF long, EUR/AUD short
- Sanctions massives → devise ciblée short extrême + or long
- Toujours hedge or/USD/JPY quand VIX >35 + news géopolitique
"""

def get_evenements_summary():
    return """
Guerre → USD/JPY/CHF/or ↑, pétrole ↑ → CAD ↑  
Sanctions → devise ciblée crash  
Brexit/Ukraine → EUR/GBP/RUB ↓ massif
"""

def get_full_evenements():
    return (
        "Événements majeurs :\n" + "\n".join([f"{i+1}. {evt}" for i, evt in enumerate(EVENEMENTS_HISTORIQUES.strip().split('\n'))]) +
        "\n\nLeçons trading LKL Bot :\n" + LECONS_TRADING
    )
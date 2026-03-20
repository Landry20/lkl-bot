
"""
Types de conflits géopolitiques et impacts Forex immédiats / moyens termes
Version : 2.0
"""

TYPES_CONFLITS = {
    "Guerre chaude / invasion directe": {
        "exemples": "Russie-Ukraine 2022, Israël-Hamas 2023-2025",
        "impact_immédiat": "USD/JPY/CHF/or ↑ très fort | EUR ↓ (énergie) | RUB ↓ massif",
        "impact_moyen_terme": "Pétrole ↑ → CAD ↑, NOK ↑ | inflation ↑ → hawkish Fed/BCE → USD ↑",
        "paires les plus touchées": "EURUSD ↓, USDJPY ↑, USDCAD ↑, XAUUSD ↑",
        "exemple_2022": "Invasion Ukraine → EURUSD < 0.95, pétrole >120$, or >2000$"
    },
    "Conflit régional / proxy war": {
        "exemples": "Yémen Houthis vs Arabie 2024-2025, Syrie, Mer Rouge",
        "impact_immédiat": "Pétrole ↑ modéré → CAD ↑, NOK ↑ | USD ↑ léger (refuge)",
        "impact_moyen_terme": "Perturbation Suez/Malacca → fret ↑ → inflation → hawkish",
        "paires": "USDCAD ↑, EURUSD ↓ léger, XAUUSD ↑ modéré"
    },
    "Tensions diplomatiques / cyberattaques": {
        "exemples": "US-Chine Taïwan, cyberattaques Russie/Occident",
        "impact_immédiat": "USD ↑ (refuge), JPY ↑, CNY ↓ contrôlé",
        "impact_moyen_terme": "Sanctions → RUB ↓, CNY sous pression, or ↑ (dé-dollarisation)"
    },
    "Crise migratoire / instabilité politique interne": {
        "exemples": "Europe 2015-2016, Venezuela 2018-2024",
        "impact": "Devise concernée ↓ (EUR ↓ en 2015, VEF/RUB ↓), CHF ↑ (proximité)"
    },
    "Blocus naval / chokepoint bloqué": {
        "exemples": "Détroit d’Ormuz menacé, Suez bloqué 2021 Ever Given",
        "impact": "Pétrole ↑ très fort → CAD ↑ massif, inflation ↑ → USD ↑ hawkish"
    }
}

REGLES_TRADING_GEOPOLITIQUE = """
Règles LKL Bot face aux conflits :
- Guerre chaude → flat AUD/NZD/CAD initialement, long USD/JPY/CHF/or
- Pétrole spike >10% → long USDCAD, short EURUSD
- Houthis/Mer Rouge → surveiller Brent >90$ → CAD call options
- Taïwan tension → long USD/CNH, short AUDUSD
- Backend : alerte Telegram "GEOPO ALERT" + pause trading 1-2h sur news majeure
"""

def get_types_conflits_summary():
    return """
Guerre chaude → USD/JPY/CHF/or ↑ massif  
Proxy/régional → pétrole ↑ → CAD/NOK ↑  
Tensions diplomatiques → USD/JPY ↑ léger  
Chokepoint bloqué → inflation + CAD ↑
"""

def get_full_types_conflits():
    lines = []
    for typ, data in TYPES_CONFLITS.items():
        lines.append(f"► {typ}")
        lines.append(f"   Exemples : {data['exemples']}")
        lines.append(f"   Impact immédiat : {data['impact_immédiat']}")
        lines.append(f"   Impact moyen terme : {data['impact_moyen_terme']}")
        lines.append(f"   Paires touchées : {data['paires les plus touchées']}")
        lines.append("")
    lines.append("\nRègles trading LKL :\n" + REGLES_TRADING_GEOPOLITIQUE)
    return "\n".join(lines)
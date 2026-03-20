
"""
Alliances mondiales et blocs - Impact Forex
Version : 2.0
"""

BLOCS_ACTUELS = """
- OTAN (USA + Europe + Canada) : Renforce USD/EUR en crise
- BRICS (Brésil, Russie, Inde, Chine, Afrique du Sud + nouveaux 2024-2025) : Pousse dé-dollarisation, or/CNY ↑ long terme
- OPEP+ (Arabie + Russie + autres) : Contrôle pétrole → CAD/NOK/RUB impactés
- AUKUS (Australie, UK, USA) : Anti-Chine → AUD/USD/JPY sensible
- QUAD (USA, Japon, Inde, Australie) : Anti-Chine → AUD/JPY impact
"""

IMPACTS_BLOCS = """
- BRICS expansion 2024-2025 → or ↑, CNY ↑ potentiel, USD ↓ long terme (si paiements BRICS augmentent)
- OPEP+ coupes production → pétrole ↑ → CAD ↑, USD ↑ modéré (inflation)
- OTAN élargissement (Finlande/Suède 2023) → EUR/NOK ↑ léger (stabilité nordique)
"""

def get_alliances_summary():
    return """
BRICS → dé-dollarisation → or/CNY ↑ long terme  
OPEP+ → pétrole ↑ → CAD/NOK ↑  
OTAN → USD/EUR stabilité en crise
"""

def get_full_alliances():
    return BLOCS_ACTUELS + "\n\n" + IMPACTS_BLOCS
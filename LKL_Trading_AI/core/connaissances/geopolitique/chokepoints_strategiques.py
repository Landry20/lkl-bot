
"""
Chokepoints stratégiques - Points de passage critiques et impact Forex
Version : 2.0 - Cours détaillé
"""

CHOKepoints_INTRO = """
Les chokepoints sont des passages maritimes étroits par lesquels transite une grande partie du commerce mondial (pétrole, gaz, biens).

Un blocage ou une menace fait exploser les prix énergie → inflation → impact devises
"""

PRINCIPAUX_CHOKEPOINTS = """
1. **Détroit d’Ormuz**  
   - Localisation : Iran/Oman – 20 % pétrole mondial  
   - Menace : Iran, Houthis, tensions US-Iran  
   - Impact : Pétrole ↑ massif → CAD/NOK ↑, EUR ↓, USD ↑ (inflation)  
   - Exemple : 2019 drones → Brent +10 % en jours

2. **Détroit de Bab el-Mandeb** (Mer Rouge)  
   - Localisation : Yémen/Djibouti – Suez route  
   - Menace : Houthis attaques 2024–2025  
   - Impact : Fret ↑ → inflation → CAD ↑ (énergie), EUR ↓  
   - Exemple : 2024 blocage → reroutage Cap → coûts +30 %

3. **Canal de Suez**  
   - Égypte – 12 % commerce mondial  
   - Menace : Égypte instabilité, Ever Given 2021  
   - Impact : Pétrole/gaz ↑ → CAD/NOK ↑

4. **Détroit de Malacca**  
   - Indonésie/Malaisie/Singapour – 25 % pétrole, 40 % gaz  
   - Menace : Piraterie, tensions Chine  
   - Impact : Pétrole ↑ → AUD/NZD/CAD ↑ (Asie demande)

5. **Canal de Panama**  
   - Impact : Plus faible sur énergie, mais fret US-Asie  
   - Sécheresse 2023–2024 → délais → inflation légère

6. **Détroit de Taïwan**  
   - Menace : Chine invasion → semi-conducteurs crash → NAS100 ↓ → USD ↑
"""

IMPACTS_FOREX = """
- Ormuz/Bab el-Mandeb menacés → Brent +10–30 $ → CAD/NOK ↑ fort, USDCAD ↓, EURUSD ↓  
- Suez bloqué → inflation → hawkish banques → USD ↑  
- Malacca → pétrole ↑ → AUD ↑ (Chine demande alternative)  
- Taïwan risque → tech crash → risk-off → USD/JPY ↑
"""

REGLES_TRADING_LKL = """
Règles bot :
- News Ormuz/Bab el-Mandeb → alerte "ENERGY SPIKE" → long USDCAD/NOK  
- Brent >90 $ géopolitique → short EURUSD  
- Vérifier flux fret Suez/Malacca → anticiper inflation  
- Taïwan tension → flat NAS100, long USD/JPY
"""

def get_chokepoints_summary():
    return """
Chokepoints : Ormuz/Bab el-Mandeb/Suez → pétrole ↑ → CAD/NOK ↑, EUR ↓  
Malacca → énergie Asie → AUD ↑ potentiel  
Taïwan → risk-off → USD/JPY ↑
"""

def get_full_chokepoints():
    return (
        CHOKEPOINTS_INTRO + "\n\n" +
        PRINCIPAUX_CHOKEPOINTS + "\n\n" +
        IMPACTS_FOREX + "\n\n" +
        REGLES_TRADING_LKL
    )
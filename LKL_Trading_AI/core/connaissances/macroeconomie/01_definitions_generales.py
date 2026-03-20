
"""
Définitions Générales en Macroéconomie - Croissance, Inflation, Chômage, etc.
Version : 2.0 - Cours détaillé avec liens Forex
"""

DEFINITIONS_GENERALES = """
1. **Croissance économique** : Augmentation du PIB réel sur une période (trimestre/année).
   - Mesure : % variation annualisée
   - Idéal : 2–3 % pour économies développées
   - Impact Forex : Croissance forte → devise ↑ (attire capitaux)

2. **Inflation** : Hausse générale et soutenue des prix.
   - Types : Demande (croissance trop rapide), coûts (pétrole ↑), monétaire (QE excessif)
   - Cible : ~2 %
   - Impact Forex : Inflation haute → anticipation resserrement → devise ↑

3. **Déflation** : Baisse des prix → spirale dangereuse (consommation reportée)
   - Impact : Devise faible, banque centrale dovish → taux bas

4. **Chômage** : % population active sans emploi.
   - Types : Frictionnel, structurel, cyclique
   - Taux naturel : 4–5 %
   - Impact Forex : Chômage bas → inflation salariale → devise ↑

5. **Balance des paiements** : Export - Import + flux capitaux
   - Déficit → devise ↓ long terme
   - Surplus → devise ↑

6. **Dette publique** : Emprunts État / PIB
   - Haut ratio (>100 %) → risque souverain → devise ↓ (ex. EUR Grèce 2010)
"""

EXEMPLES_LIENS_FOREX = """
- Croissance US 3 % → USD ↑, EURUSD ↓
- Inflation UK 10 % 2022 → GBP ↓ initial (dovish BoE), puis ↑ (hawkish pivot)
- Chômage bas Japon → JPY stable faible (BoJ YCC)
- Déficit US chronique → USD long terme pression, mais refuge status compense
"""

def get_definitions_summary():
    return """
Définitions macro : Croissance (PIB ↑ → devise ↑), Inflation (2 % cible → resserrement → devise ↑), Chômage bas → inflation → devise ↑, Dette haute → devise ↓.
"""

def get_full_definitions():
    return DEFINITIONS_GENERALES + "\n\n" + EXEMPLES_LIENS_FOREX
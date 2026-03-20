
"""
Indicateurs Macroéconomiques - PIB, Taux, Chômage, CPI, PMI, etc.
Version : 2.0 - Cours détaillé avec impacts Forex
"""

INDICATEURS_DETAILLES = """
1. **PIB (Produit Intérieur Brut)** : Valeur biens/services produits.
   - Fréquence : Trimestriel (avance, révision, final)
   - Impact : PIB > attentes → devise ↑ | Exemple : PIB US fort 2024 → USD ↑

2. **Taux d’intérêt directeurs** : Coût emprunt Fed/BCE/etc.
   - Impact : Hausse → devise ↑ (carry attractif) | Exemple : Fed hikes 2022 → USD rally

3. **Chômage / NFP** : Emplois créés, taux chômage.
   - Fréquence : Mensuel
   - Impact : NFP haut → USD ↑ | Exemple : NFP 200k+ → EURUSD ↓ 50 pips

4. **CPI / Inflation** : Variation panier biens/services.
   - Headline vs Core
   - Impact : CPI > attentes → devise ↑ (hawkish anticipation)

5. **PMI** : Enquête activité ( >50 expansion)
   - Impact : PMI faible → devise ↓ | Exemple : PMI Euro <50 → EUR ↓

Autres : Retail Sales (consommation ↑ → devise ↑), Balance commerciale (surplus → devise ↑)
"""

VOLATILITE_INDICATEURS = """
Niveau volatilité Forex :
- NFP / CPI / FOMC : Haute (100–300 pips)
- PIB / PMI : Moyenne (50–150 pips)
- Autres : Basse (20–80 pips)
"""

def get_indicateurs_summary():
    return """
Indicateurs macro : PIB/NFP/CPI haut → devise ↑. Volatilité haute sur NFP/CPI.
"""

def get_full_indicateurs():
    return INDICATEURS_DETAILLES + "\n\n" + VOLATILITE_INDICATEURS
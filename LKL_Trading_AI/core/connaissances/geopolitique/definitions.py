
"""
Géopolitique - Définitions et concepts clés pour le trading Forex
Version : 2.0 - Très détaillé
"""

GEOPOLITIQUE_INTRODUCTION = """
La géopolitique étudie l’influence de la géographie, des ressources, des frontières, des populations et du pouvoir politique sur les relations internationales.

En trading Forex, la géopolitique est un **multiplicateur de volatilité** :
- Elle peut créer des mouvements de 200–500+ pips en quelques heures/jours
- Elle inverse souvent les tendances macro classiques (carry trade, inflation)
- Elle renforce ou détruit les devises refuge (USD, JPY, CHF)
- Elle impacte fortement les commodities currencies (pétrole → CAD, gaz → EUR/NOK/RUB)
"""

CONCEPTS_CLES_GEOPOLITIQUE = """
- **Hard power** : Force militaire directe (invasions, frappes, blocus navals)
- **Soft power** : Influence culturelle, économique, diplomatique (sanctions, aide, médias)
- **Proxy war** : Conflit indirect via alliés ou groupes armés (Ukraine 2022–2025, Syrie, Yémen)
- **Energy weaponization** : Utilisation du pétrole/gaz comme arme (Russie 2022 gaz → Europe, OPEP+ quotas)
- **Currency war** : Dévaluation compétitive volontaire (JPY 2022–2024, CNY contrôlé)
- **De-dollarisation** : Tentative de réduire dépendance au dollar (BRICS, Chine-Russie paiements CNY/RUB)
- **Chokepoints** : Points stratégiques (détroit d’Ormuz, canal de Suez, détroit de Malacca, Panama)
- **Sphère d’influence** : Zone où un pays domine (USA Amérique latine, Russie ex-URSS, Chine Mer de Chine méridionale)
"""

IMPACT_GENERIQUE_SUR_LE_FOREX = """
Règle générale géopolitique :
- Risque géopolitique ↑ → **USD, JPY, CHF, or** ↑ (refuges)
- Conflit localisé (non-Occident) → USD ↑ modéré
- Conflit impliquant USA/Europe → volatilité extrême, USD peut baisser si faiblesse perçue
- Énergie perturbée → CAD ↑ (pétrole), NOK ↑ (gaz), RUB ↓ très fort, EUR ↓ (importateur)
- De-dollarisation accélérée → or ↑, CNY long terme potentiel ↑
"""

def get_geopolitique_definitions_summary():
    return """
Géopolitique = hard/soft power, proxy wars, energy weaponization, currency wars, de-dollarisation.
Impact Forex : risque ↑ → USD/JPY/CHF/or ↑ | énergie perturbée → CAD/NOK ↑, EUR ↓
"""

def get_full_geopolitique_definitions():
    return (
        GEOPOLITIQUE_INTRODUCTION + "\n\n" +
        CONCEPTS_CLES_GEOPOLITIQUE + "\n\n" +
        IMPACT_GENERIQUE_SUR_LE_FOREX
    )
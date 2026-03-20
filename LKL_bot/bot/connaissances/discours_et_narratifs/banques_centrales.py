
"""
Discours et narratifs des Banques Centrales
Version : 2.0 - Très détaillé - Hawkish / Dovish / Neutre + exemples récents
"""

BANQUES_CENTRALESS_DISCOURS_INTRO = """
Les discours des banques centrales (Fed, BCE, BoE, BoJ, RBA, etc.) sont souvent **plus importants** que les décisions elles-mêmes.

Pourquoi ?
- Le **forward guidance** (ce qu’ils disent sur l’avenir) influence les anticipations de taux sur 6–24 mois
- Le **ton** (hawkish / dovish) peut provoquer des mouvements de 100–400 pips en quelques heures
- Une phrase mal interprétée ou une surprise dans le dot plot / projections peut inverser complètement le marché
"""

DEFINITIONS_TONS = """
**Hawkish** (faucon) = combat l’inflation, prêt à resserrer la politique monétaire
Mots / phrases typiques :
- "inflation persistante / plus élevée que prévu"
- "nécessité d’agir de manière décisive / ferme"
- "risques inflationnistes à la hausse"
- "taux plus élevés pour plus longtemps"
- "pas de pivot imminent"
- "réduction du bilan va se poursuivre" (QT)

**Dovish** (colombe) = priorité à la croissance / emploi, prêt à assouplir ou à rester patient
Mots / phrases typiques :
- "data dependent / dépend des données"
- "patient / pas d’urgence"
- "inflation transitoire / temporaire"
- "risques à la baisse pour la croissance"
- "flexibilité pour soutenir l’économie"
- "réduction du bilan ralentira" ou "pause QT"

**Neutre** / équilibré :
- "risques équilibrés"
- "nous restons vigilants des deux côtés"
- "pas de pré-engagement"
- "nous suivrons les données entrantes"
"""

IMPACTS_TON_SUR_LE_FOREX = """
Hawkish surprise → USD ↑ très fort (EURUSD, GBPUSD, AUDUSD ↓ | USDJPY ↑)
Dovish surprise → USD ↓ (EURUSD, GBPUSD, AUDUSD ↑ | USDJPY ↓)
Neutre → réaction faible sauf si dot plot / projections surprenantes

Exemples concrets récents :
- Powell Jackson Hole 2022 : "pain is coming" → hawkish → USD +10 % en 3 mois
- Powell 2023 (plusieurs fois) : "higher for longer" → USDJPY 151–161
- Lagarde 2022 : "we will do whatever it takes" (anti-inflation) → EUR rebond temporaire
- BoJ Kuroda 2022–2023 : "no change to YCC" → yen très faible
- Fed 2024 pivot dovish : "cuts coming" → USD ↓, EURUSD >1.12
- BCE 2025 : "cautious cuts" → EUR stable à faible
"""

ELEMENTS_A_SURVEILLER_DANS_LES_DISCOURS = """
1. **Forward guidance** : "rates will remain restrictive", "we are not thinking about cuts"
2. **Dot Plot / Projections** : nombre de hausses/baisses prévues vs consensus
3. **Mots sur l’inflation** : "more persistent", "progress but not enough"
4. **Mots sur l’emploi / croissance** : "cooling", "resilient", "downside risks"
5. **Réaction à la question Q&A** : souvent plus franche que le scripté
6. **Changement de mots clés** : "vigilant" → "concerned", "patient" → "cautious"

Règle LKL : 
- Toute phrase avec "persistent" / "higher for longer" / "decisive action" → hawkish alert
- "data dependent" répété 3 fois + "no rush" → dovish alert
"""

def get_banques_centrales_summary():
    return """
Banques centrales discours :
Hawkish ("persistent inflation", "higher for longer") → USD ↑
Dovish ("data dependent", "patient") → USD ↓
Neutre → faible mouvement sauf dot plot surprise
Exemples : Powell "pain" 2022 → USD +10%, Fed 2024 pivot → USD ↓
"""

def get_full_banques_centrales():
    return (
        BANQUES_CENTRALESS_DISCOURS_INTRO + "\n\n" +
        DEFINITIONS_TONS + "\n\n" +
        IMPACTS_TON_SUR_LE_FOREX + "\n\n" +
        "Éléments clés à surveiller :\n" + ELEMENTS_A_SURVEILLER_DANS_LES_DISCOURS
    )
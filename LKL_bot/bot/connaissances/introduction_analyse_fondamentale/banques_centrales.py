
"""
Banques Centrales – Rôle, taux d'intérêt, politique monétaire et impact Forex
Version : 1.0
Connaissances essentielles pour traders Forex
"""

BANQUES_CENTRALESS_INTRODUCTION = """
Les **banques centrales** sont les institutions les plus influentes sur les marchés financiers mondiaux, 
y compris le Forex. Leurs décisions sur les taux d'intérêt, la masse monétaire et la politique monétaire 
peuvent provoquer des mouvements massifs sur les devises, les obligations, les actions et les matières premières.
"""

QUE_SONT_LES_BANQUES_CENTRALESS = """
**Définition** :  
Institution publique (ou semi-publique) chargée de gérer la politique monétaire d'un pays ou d'une zone monétaire.

**Principales responsabilités** :
- Contrôler l'inflation (objectif souvent ~2 %)
- Promouvoir la croissance économique et un niveau d'emploi élevé
- Maintenir la stabilité du système financier
- Émettre et gérer la monnaie
- Réglementer et superviser les banques commerciales
- Gérer les réserves de change
- Agir en tant que prêteur en dernier recours en cas de crise

**Action la plus importante pour les marchés** :  
Modification des **taux d'intérêt directeurs** et gestion de la **masse monétaire**.
"""

PRINCIPALES_BANQUES_CENTRALESS = """
Les banques centrales les plus suivies par les traders Forex (en raison du volume des devises) :

1. **Federal Reserve (Fed)** – États-Unis – USD  
   → La plus influente au monde

2. **Banque Centrale Européenne (BCE)** – Zone Euro – EUR

3. **Bank of England (BoE)** – Royaume-Uni – GBP

4. **Bank of Japan (BoJ)** – Japon – JPY

5. **Swiss National Bank (SNB)** – Suisse – CHF

6. **Bank of Canada (BoC)** – Canada – CAD

7. **Reserve Bank of Australia (RBA)** – Australie – AUD

8. **Reserve Bank of New Zealand (RBNZ)** – Nouvelle-Zélande – NZD

Autres importantes :  
- People's Bank of China (PBoC) – CNY  
- Banco Central do Brasil (BCB) – BRL  
- Banco de México (Banxico) – MXN
"""

BANQUES_CENTRALESS_ET_TAUX_D_INTERET = """
Le principal outil des banques centrales est le **taux d'intérêt directeur** (taux de base, policy rate).

**Objectif** : maintenir l'équilibre entre :
- Croissance économique trop rapide → inflation excessive
- Croissance trop lente → chômage élevé et stagnation

**Mécanisme** :
- Taux bas → emprunter devient moins cher → entreprises investissent, ménages consomment → croissance ↑
- Taux hauts → emprunter devient plus cher → dépenses et investissements ↓ → croissance ralentie, inflation maîtrisée

**Exemples concrets** :
- Taux élevés → banques préfèrent déposer à la banque centrale (sécurisé) → prêtent moins → économie ralentit
- Taux bas → banques prêtent plus facilement → liquidités circulent → croissance stimulée
"""

COMMENT_LES_TAUX_D_INTERET_AFFECTENT_LES_MARCHES = """
**Impact sur le Forex** :

- **Taux plus élevés** (ou hausse attendue) → devise attire les capitaux → demande ↑ → devise **appréciée**
- **Taux plus bas** (ou baisse attendue) → devise moins attractive → demande ↓ → devise **dépréciée**

**Carry Trade** :  
Stratégie populaire consistant à :
- Emprunter dans une devise à faible taux (ex. JPY, CHF)
- Investir dans une devise à taux élevé (ex. AUD, NZD, USD)
- Profiter du différentiel de taux (si pas de variation trop forte du change)

**Autres marchés** :
- Taux hauts → obligations perdent de la valeur → actions souvent sous pression
- Taux bas → obligations gagnent → actions souvent soutenues
"""

REUNIONS_DES_BANQUES_CENTRALESS = """
**Calendrier** :  
Chaque banque centrale a son propre calendrier de réunions (ex. FOMC 8 fois par an pour la Fed).

**Éléments suivis par les marchés** :
- Décision sur les taux (hausse, baisse, statu quo)
- Communiqué officiel
- Conférence de presse du gouverneur / président
- Projections économiques (dot plot Fed, staff projections BCE)
- Minutes / compte rendu (publié 2–3 semaines après)
- **Forward guidance** : indications sur les futures décisions

**Ton** :
- **Hawkish** (faucon) : combat l'inflation → hausse des taux ou moins d'assouplissement
- **Dovish** (colombe) : soutient la croissance → baisse des taux ou maintien accommodant

**Réaction marché** : souvent plus forte sur le **ton** et la **surprise** que sur le changement de taux lui-même.
"""

ASSOUPLISSEMENT_QUANTITATIF_QE = """
**Quantitative Easing (QE)** :  
Politique non conventionnelle utilisée quand les taux sont déjà très bas (proche de 0 %).

**Mécanisme** :
- Banque centrale achète massivement des obligations (gouvernementales, corporate)
- Injecte de la monnaie dans l'économie
- Baisse les taux à long terme
- Encourage l'emprunt et l'investissement

**Effet sur devises** :  
Généralement **dépréciatif** (plus de monnaie → valeur ↓)

Exemples :
- Fed après 2008 et 2020
- BCE 2015–2018
- BoJ depuis 2013 (QE massif)
"""

INTERVENTIONS_DIRECTES = """
**Interventions sur le marché des changes** :  
Achat ou vente directe de devises pour influencer le taux de change.

**Exemples fréquents** :
- **Banque du Japon** : vend des yens pour limiter l'appréciation (yen trop fort → exportations pénalisées)
- **SNB** (Suisse) : achète des euros pour empêcher le franc suisse de devenir trop fort (2011–2015 : plancher EUR/CHF à 1.20)

**Caractéristiques** :
- Souvent surprises (annoncées après coup ou pas du tout)
- Difficiles à anticiper
- Impact très fort mais temporaire si le marché est contre
- Moins fréquentes aujourd'hui (sauf BoJ et SNB occasionnellement)
"""

PRINCIPAUX_ENSEIGNEMENTS_BANQUES_CENTRALESS = [
    "Les banques centrales sont les acteurs les plus puissants sur le Forex",
    "Le taux d'intérêt directeur est leur principal outil",
    "Taux ↑ → devise généralement plus forte ; Taux ↓ → devise plus faible",
    "Hawkish = combat inflation → taux plus hauts ; Dovish = soutient croissance → taux plus bas",
    "Les surprises et le forward guidance provoquent les plus gros mouvements",
    "Le QE injecte de la monnaie → généralement dépréciatif pour la devise",
    "Les interventions directes sont rares mais explosives",
    "Toujours surveiller le calendrier des réunions (FOMC, BCE, BoJ, etc.)",
    "Le différentiel de taux entre deux pays influence fortement les paires (carry trade)"
]

def get_banques_centrales_summary() -> str:
    """Résumé court pour notifications, logs ou dashboard"""
    return """
Les banques centrales contrôlent la politique monétaire et influencent fortement les devises.
→ Taux ↑ / hawkish → devise ↑
→ Taux ↓ / dovish / QE → devise ↓
Réunions (FOMC, BCE, BoJ...) = volatilité élevée.
Interventions directes rares mais très impactantes.
"""

def get_full_banques_centrales_explanation() -> str:
    """Explication complète pour documentation ou formation"""
    parts = [
        BANQUES_CENTRALESS_INTRODUCTION,
        "\n\n" + QUE_SONT_LES_BANQUES_CENTRALESS,
        "\n\nPrincipales banques centrales :\n" + PRINCIPALES_BANQUES_CENTRALESS,
        "\n\nTaux d'intérêt :\n" + BANQUES_CENTRALESS_ET_TAUX_D_INTERET,
        "\n\nFonctionnement des taux :\n" + COMMENT_LES_TAUX_D_INTERET_AFFECTENT_LES_MARCHES,
        "\n\nImpact marchés :\n" + COMMENT_LES_TAUX_D_INTERET_AFFECTENT_LES_MARCHES,
        "\n\nRéunions :\n" + REUNIONS_DES_BANQUES_CENTRALESS,
        "\n\nAssouplissement quantitatif (QE) :\n" + ASSOUPLISSEMENT_QUANTITATIF_QE,
        "\n\nInterventions directes :\n" + INTERVENTIONS_DIRECTES,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_BANQUES_CENTRALESS)
    ]
    return "".join(parts)


# Pour tester
if __name__ == "__main__":
    print(get_banques_centrales_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_banques_centrales_explanation())

"""
Inflation – Concepts clés pour l'analyse fondamentale en Forex
Version : 1.0
Regroupe les définitions, impacts et exemples liés à l'inflation, la déflation, etc.
"""

INFLATION_INTRODUCTION = """
L'inflation est un des piliers de l'analyse fondamentale en trading Forex.
Elle influence directement les décisions des banques centrales sur les taux d'intérêt, 
ce qui a un impact majeur sur la force ou la faiblesse des devises.

Les banques centrales ont généralement un double mandat :
- Maintenir un niveau élevé d'emploi
- Assurer la stabilité des prix (contrôler l'inflation)

La plupart ciblent une inflation annuelle autour de **2 %** (Banque d'Angleterre, Fed, BCE, etc.).
"""

QU_EST_CE_QUE_L_INFLATION = """
**Définition** :  
L'inflation est la **hausse soutenue et généralisée des prix** des biens et services dans une économie au fil du temps.

Elle est mesurée principalement par :
- L'Indice des Prix à la Consommation (IPC / CPI)
- L'Indice des Dépenses de Consommation Personnelle (PCE – préféré par la Fed)
- Autres : PPI, IPCH (Europe), etc.

Pourquoi une inflation faible et stable est-elle souhaitable ?
- Elle signale une croissance économique saine
- Elle évite la déflation (voir plus bas)
- Elle donne de la marge aux banques centrales pour baisser les taux en cas de ralentissement
- Elle incite les agents économiques à consommer et investir plutôt qu'à thésauriser

Objectif typique : **~2 % par an**  
→ Trop basse (< 1 %) → risque de stagnation / déflation  
→ Trop haute (> 4–5 %) → risque de perte de pouvoir d'achat et d'hyperinflation
"""

HYPERINFLATION = """
**Hyperinflation** : inflation extrêmement élevée et incontrôlable  
(typiquement > 50 % par mois ou > 1000 % par an)

Conséquences :
- Effondrement de la valeur de la monnaie
- Perte totale de confiance dans la devise
- Passage à des monnaies étrangères ou au troc
- Crise économique et sociale majeure

Exemples historiques :
- Allemagne (République de Weimar) : 1921–1923
- Zimbabwe : 2007–2009 (pic à 89,7 sextillions % par mois)
- Hongrie : 1945–1946
- Venezuela : 2016–2020
- Russie post-URSS (début 1990)

Aujourd'hui : les banques centrales restent extrêmement vigilantes pour éviter ce scénario.
"""

DEFLATION = """
**Déflation** : baisse générale et durable des prix (inflation < 0 %)

À première vue positive pour le consommateur (tout devient moins cher),  
mais très dangereuse pour l'économie :

Conséquences :
- Les entreprises voient leurs marges diminuer → réduisent salaires ou licencient
- Hausse du chômage → baisse de la demande
- Les consommateurs reportent leurs achats (attente de prix encore plus bas)
- Spirale déflationniste : chômage ↑ → demande ↓ → prix ↓ → plus de chômage

Exemples :
- Grande Dépression (années 1930)
- Japon : décennies 1990–2010 (désinflation persistante + déflation par périodes)

Réaction des banques centrales : assouplissement agressif (taux à 0 %, QE, etc.)
"""

REFATION_ET_DESINFLATION = """
**Reflation** (regonflement) :  
Augmentation du taux d'inflation (souvent après une période de faible inflation ou déflation)  
→ Souvent voulue et provoquée par les politiques monétaires (baisse des taux, QE)

**Désinflation** :  
Ralentissement du taux d'inflation (l'inflation reste positive mais diminue)  
Exemple : inflation passe de 6 % à 3 % → c'est de la désinflation (pas de la déflation)

Exemple historique :
- Japon 1990–2010 : désinflation persistante → stagnation → "décennies perdues"
- Réponse : QE massif par la Banque du Japon pour tenter de relancer l'inflation
"""

QU_EST_CE_QUE_LA_ZINFLATION = """
**Zinflation** (zero inflation) :  
Situation où l'inflation est proche de **0 %** sur une longue période  
et où les taux d'intérêt restent très bas ou à zéro.

Dans les années 1990, certains (dont Alan Greenspan) voyaient la zinflation comme un idéal :  
stabilité parfaite des prix.

Aujourd'hui considérée comme **indésirable** :
- Risque de glisser vers la déflation
- Peu de marge pour les banques centrales en cas de crise (taux déjà à 0 %)
- Stagnation économique (exemple japonais)

Modèle actuel préféré : **inflation faible mais positive** (~2 %) pour garder une marge de manœuvre.
"""

IMPACT_SUR_LE_FOREX = """
**Inflation et devises** – Règles générales :

- Inflation plus élevée que prévu → anticipation de **hausse des taux** → devise ↑
- Inflation plus faible que prévu → anticipation de **baisse ou maintien des taux** → devise ↓
- Hyperinflation → destruction de la devise (ex. : ZWL, VEF → chute libre)
- Déflation persistante → politique ultra-accommodante → devise faible ou stable basse
- Désinflation contrôlée (vers 2 %) → neutre à positif si la banque centrale est crédible

Attention : le marché réagit surtout à la **surprise** par rapport aux attentes  
et au **contexte** (inflation déjà haute ou basse, position de la banque centrale).
"""

PRINCIPAUX_ENSEIGNEMENTS_INFLATION = [
    "L'inflation cible idéale est autour de 2 % par an",
    "Une inflation trop élevée mène à des hausses de taux → devise plus forte",
    "Une inflation trop faible ou négative (déflation) mène à des baisses de taux → devise plus faible",
    "L'hyperinflation détruit la confiance dans la monnaie",
    "La déflation crée une spirale dangereuse (baisse des prix → chômage → moins de demande)",
    "La désinflation est une baisse du rythme de l'inflation (pas une baisse des prix)",
    "La reflation est une hausse voulue de l'inflation (souvent par QE)",
    "La zinflation (0 %) est aujourd'hui considérée comme risquée",
    "Les surprises d'inflation provoquent une forte volatilité sur le Forex"
]

def get_inflation_summary() -> str:
    """Résumé court pour logs, notifications ou dashboard"""
    return """
L'inflation mesure la hausse des prix.  
Cible des banques centrales : ~2 % par an.  
→ Inflation ↑ > attentes → hausse probable des taux → devise ↑  
→ Inflation ↓ ou déflation → politique accommodante → devise ↓  
Hyperinflation et déflation sont des scénarios extrêmes à éviter absolument.
"""

def get_full_inflation_explanation() -> str:
    """Explication complète pour documentation ou formation"""
    parts = [
        INFLATION_INTRODUCTION,
        "\n\n" + QU_EST_CE_QUE_L_INFLATION,
        "\n\nHyperinflation :\n" + HYPERINFLATION,
        "\n\nDéflation :\n" + DEFLATION,
        "\n\nReflation & Désinflation :\n" + REFATION_ET_DESINFLATION,
        "\n\nZinflation :\n" + QU_EST_CE_QUE_LA_ZINFLATION,
        "\n\nImpact Forex :\n" + IMPACT_SUR_LE_FOREX,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_INFLATION)
    ]
    return "".join(parts)


# Pour tester
if __name__ == "__main__":
    print(get_inflation_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_inflation_explanation())
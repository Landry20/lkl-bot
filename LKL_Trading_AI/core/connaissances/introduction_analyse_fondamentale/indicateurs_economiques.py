
"""
Principaux indicateurs et annonces économiques en analyse fondamentale
Version : 1.1
Ce fichier regroupe les 6 indicateurs / annonces les plus suivis sur les marchés Forex.
"""

INDICATEURS_ECONOMIQUES_INTRODUCTION = """
Les indicateurs et annonces économiques sont au cœur de l'analyse fondamentale.
Ils permettent de comprendre la santé réelle d'une économie et d'anticiper les décisions 
des banques centrales, qui influencent fortement les devises.

Même si vous tradez principalement en technique, suivre ces publications est essentiel 
car elles provoquent souvent les plus gros mouvements de prix (surtout en cas de "surprise").

Voici les 6 indicateurs et annonces les plus importants à surveiller :
"""

INDICATEURS_CLES = [
    {
        "nom": "Masse salariale non agricole (NFP – Non-Farm Payrolls)",
        "pays": "États-Unis",
        "fréquence": "Mensuelle – premier vendredi du mois",
        "contenu": [
            "Nombre net d'emplois créés (hors agriculture, emplois privés à but non lucratif, ménages)",
            "Taux de chômage",
            "Salaire horaire moyen (Average Hourly Earnings)",
            "Taux de participation au marché du travail"
        ],
        "importance": """
Le NFP reste l'un des indicateurs les plus impactants sur le dollar US et sur les marchés mondiaux.
La Fed a un double mandat : plein emploi + stabilité des prix.
→ Emploi fort → anticipation de hausse de taux → USD généralement plus fort
→ Emploi faible → anticipation de baisse de taux ou maintien → USD sous pression
        """,
        "points_cles": [
            "Très forte volatilité attendue à la publication",
            "L'écart par rapport au consensus (prévisions moyennes des économistes) est plus important que le chiffre brut",
            "Les révisions des deux mois précédents peuvent aussi bouger le marché"
        ]
    },
    {
        "nom": "Indice des Prix à la Consommation (IPC / CPI)",
        "pays": "Chaque pays (USA, Zone Euro, UK, Canada, etc.)",
        "fréquence": "Mensuelle",
        "contenu": [
            "Mesure l'évolution des prix d'un panier de biens et services consommés par les ménages",
            "Headline CPI : inclut alimentation et énergie (volatiles)",
            "Core CPI : hors alimentation et énergie (préféré par beaucoup de banques centrales)"
        ],
        "autres_mesures_inflation": [
            "PCE Price Index (préféré par la Fed)",
            "PPI – Indice des prix à la production",
            "Prix à l'import/export",
            "Indice des prix à la consommation harmonisé (IPCH – Europe)"
        ],
        "importance": """
Les banques centrales ciblent généralement une inflation autour de 2 % (1–3 % toléré).
→ Inflation trop élevée → risque de resserrement monétaire → devise souvent plus forte
→ Inflation trop faible ou déflation → risque d'assouplissement → devise sous pression
        """,
        "points_cles": [
            "Core CPI souvent plus regardé que le headline",
            "Surprise à la hausse = volatilité forte"
        ]
    },
    {
        "nom": "Réunions des banques centrales",
        "pays": "Fed (FOMC), BCE, BoE, BoJ, RBA, etc.",
        "fréquence": "6 à 8 fois par an (parfois plus en cas de crise)",
        "contenu": [
            "Décision sur les taux directeurs",
            "Communiqué officiel",
            "Conférence de presse du gouverneur / président",
            "Projections économiques (dot plot pour la Fed)",
            "Minutes / compte rendu (publié 2–3 semaines après)"
        ],
        "importance": """
Les annonces de taux et surtout le ton (hawkish / dovish) peuvent provoquer des mouvements massifs.
→ Hausse de taux + ton hawkish → devise ↑
→ Baisse de taux ou forward guidance dovish → devise ↓
        """,
        "points_cles": [
            "La conférence de presse et les questions-réponses sont souvent plus importantes que la décision elle-même",
            "Le forward guidance (indication sur les futures décisions) est scruté"
        ]
    },
    {
        "nom": "Rapports sur le moral / confiance des consommateurs et des entreprises",
        "pays": "USA (Michigan, Conference Board), Zone Euro, UK, etc.",
        "fréquence": "Mensuelle",
        "exemples": [
            "Consumer Confidence Index (Conference Board)",
            "University of Michigan Consumer Sentiment",
            "ZEW Economic Sentiment (Allemagne)",
            "IFO Business Climate Index (Allemagne)"
        ],
        "importance": """
Indicateurs avancés : ils mesurent le sentiment actuel et les intentions futures.
→ Confiance élevée → consommation et investissement ↑ → croissance probable
→ Confiance faible → dépenses ↓ → risque de ralentissement
        """,
        "points_cles": [
            "Souvent considérés comme indicateurs précurseurs",
            "Moins volatils que NFP ou CPI, mais utiles pour anticiper les tendances"
        ]
    },
    {
        "nom": "Indice des Directeurs d'Achat (PMI – Purchasing Managers' Index)",
        "pays": "Mondial, USA, Zone Euro, UK, Chine, Japon, etc.",
        "fréquence": "Mensuelle",
        "interprétation": {
            "> 50": "Expansion du secteur",
            "= 50": "Stagnation",
            "< 50": "Contraction du secteur"
        },
        "types": [
            "PMI Manufacturier",
            "PMI des Services",
            "PMI Composite (global)"
        ],
        "importance": """
Indicateur très rapide (publié en début de mois pour le mois précédent).
Reflète directement l'activité réelle des entreprises.
→ PMI > 50 et en hausse → croissance probable → devise positive
→ PMI < 50 ou en baisse → risque de ralentissement
        """
    },
    {
        "nom": "Ventes au détail et ventes de véhicules",
        "pays": "USA, Zone Euro, UK, etc.",
        "fréquence": "Mensuelle",
        "contenu": [
            "Ventes au détail (Retail Sales) : dépenses des consommateurs sur biens",
            "Ventes de véhicules : indicateur plus spécifique mais rapide"
        ],
        "importance": """
Mesure directe de la consommation, moteur principal des économies développées.
→ Ventes en hausse → consommation forte → croissance et inflation potentielles
→ Ventes en baisse → risque de ralentissement économique
        """,
        "points_cles": [
            "Les ventes de véhicules sont parfois considérées comme un indicateur avancé des ventes au détail",
            "Core retail sales (hors autos et essence) souvent plus regardé"
        ]
    }
]

def get_indicateurs_summary() -> str:
    """Retourne un résumé clair et concis de tous les indicateurs"""
    lines = [INDICATEURS_ECONOMIQUES_INTRODUCTION, ""]
    for ind in INDICATEURS_CLES:
        lines.append(f"► {ind['nom']}")
        if "pays" in ind:
            lines.append(f"   Pays principal : {ind['pays']}")
        if "fréquence" in ind:
            lines.append(f"   Fréquence : {ind['fréquence']}")
        lines.append("")
    return "\n".join(lines)

def get_detailed_indicator(nom: str) -> dict | None:
    """Retourne les détails complets d'un indicateur par son nom"""
    for ind in INDICATEURS_CLES:
        if nom.lower() in ind["nom"].lower():
            return ind
    return None

# Pour tester / visualiser
if __name__ == "__main__":
    print(get_indicateurs_summary())
    print("\nExemple détail NFP :")
    nfp = get_detailed_indicator("NFP")
    if nfp:
        print(nfp["importance"])
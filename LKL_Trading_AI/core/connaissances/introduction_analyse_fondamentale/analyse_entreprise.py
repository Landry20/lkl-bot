
"""
Analyse Fondamentale d'une Entreprise (pour actions cotées)
Version : 1.0
Connaissances clés pour évaluer si une action est sous-évaluée ou surévaluée
"""

ANALYSE_ENTREPRISE_INTRODUCTION = """
L'analyse fondamentale d'une entreprise consiste à examiner toutes les données disponibles 
pour déterminer la **valeur intrinsèque** d'une action et décider si elle est :
- **sous-évaluée** (opportunité d'achat)
- **surévaluée** (opportunité de vente ou évitement)

Elle se divise en deux grands axes :
1. Analyse interne de l'entreprise (finances, résultats, ratios)
2. Analyse externe (contexte économique, secteur, concurrence)
"""

BENEFICES_ET_RAPPORTS_FINANCIERS = """
**Les rapports financiers obligatoires** (pour les sociétés cotées) :
- Rapport trimestriel (10-Q aux USA)
- Rapport annuel (10-K aux USA) – plus complet
- Publication pendant la **saison des résultats** (4 périodes par an)

**Documents principaux à analyser** :

1. **Compte de résultat (Income Statement)**  
   - Revenus / Chiffre d'affaires (Revenue / Sales)  
   - Coût des marchandises vendues (COGS)  
   - Dépenses opérationnelles  
   - Résultat opérationnel (EBIT)  
   - Résultat net (Net Income / Profit)  
   - Bénéfice par action (EPS – Earnings Per Share)  
   - Marge brute, marge opérationnelle, marge nette  

2. **Bilan (Balance Sheet)**  
   - Actifs (Assets) : courant (cash, stocks, créances) + non courant (immobilisations, brevets…)  
   - Passif (Liabilities) : dettes court terme + long terme  
   - Capitaux propres (Equity) = Actifs – Passif  
   → Principe : Actifs = Passif + Capitaux propres  

3. **Tableau des flux de trésorerie (Cash Flow Statement)**  
   - Flux d’exploitation (Operating Cash Flow) – le plus important  
   - Flux d’investissement (Investing Cash Flow)  
   - Flux de financement (Financing Cash Flow)  
   → Permet de voir si l’entreprise génère vraiment du cash ou si elle brûle de la trésorerie
"""

RATIOS_FINANCIERS_IMPORTANTS = """
**Ratios les plus utilisés pour évaluer une entreprise** :

1. **Ratio Cours / Bénéfice (PER – Price / Earnings Ratio)**  
   PER = Cours de l’action / Bénéfice par action (EPS)  
   → Combien payez-vous pour 1 € de bénéfice ?  
   - PER bas → potentiellement sous-évaluée (ou problèmes)  
   - PER élevé → croissance attendue forte ou surévaluation  
   → Comparer au secteur et à l’historique

2. **Ratio Cours / Valeur Comptable (P/B – Price / Book Ratio)**  
   P/B = Cours de l’action / Valeur comptable par action  
   Valeur comptable = (Actifs – Passif) / Nombre d’actions  
   → < 1 → action vendue en dessous de sa valeur comptable (souvent valeur)  
   → > 1 → valorisation des actifs intangibles (marque, brevets, etc.)

3. **Rendement des Actifs (ROA – Return On Assets)**  
   ROA = Résultat net / Total Actif  
   → Efficacité dans l’utilisation des actifs pour générer du profit

4. **Rendement des Capitaux Propres (ROE – Return On Equity)**  
   ROE = Résultat net / Capitaux propres  
   → Efficacité pour les actionnaires (souvent > 15 % considéré bon)

Autres ratios utiles :
- **Dette / Capitaux propres** (Debt-to-Equity) – niveau d’endettement
- **Marge nette** (Net Margin)
- **Croissance des revenus** (Revenue Growth)
- **Free Cash Flow Yield** – cash disponible après investissements
"""

FACTEURS_PLUS_LARGES_ET_APPROCHE_DESCENDANTE = """
**Approche descendante (Top-Down)** recommandée :

1. **Économie globale**  
   - Croissance du PIB  
   - Taux d’intérêt & politique monétaire  
   - Inflation  
   - Chômage  
   - Confiance consommateurs / entreprises  

2. **Secteur d’activité**  
   - Tendances sectorielles (ex. transition énergétique, IA, e-commerce)  
   - Réglementations nouvelles  
   - Concurrence accrue ou consolidation  
   - Demande cyclique ou structurelle  

3. **Position de l’entreprise dans son secteur**  
   - Part de marché  
   - Avantage concurrentiel (moat) : marque, brevets, réseau, coûts bas…  
   - Comparaison des ratios avec les concurrents (PER, ROE, marge, croissance)  

4. **Éléments qualitatifs**  
   - Qualité de la direction  
   - Innovation / R&D  
   - Brevets, propriété intellectuelle  
   - Risques (litiges, dépendance à un client/produit)  
   - Gouvernance et ESG (environnement, social, gouvernance)
"""

PRINCIPAUX_ENSEIGNEMENTS_ANALYSE_ENTREPRISE = [
    "L’analyse fondamentale cherche la valeur intrinsèque vs le prix de marché",
    "Les trois états financiers essentiels : compte de résultat, bilan, flux de trésorerie",
    "Le flux de trésorerie d’exploitation est souvent le plus révélateur de la santé réelle",
    "Le PER doit être comparé au secteur et à l’historique – pas en absolu",
    "ROE et ROA mesurent l’efficacité de la gestion",
    "Approche top-down : économie → secteur → entreprise",
    "Regarder la croissance des revenus + marges + endettement dans le temps",
    "Les actifs intangibles (marque, brevets) expliquent souvent un P/B élevé",
    "Une seule saison de résultats ne suffit pas – analyser les tendances",
    "Comparer systématiquement avec les concurrents directs"
]

def get_analyse_entreprise_summary() -> str:
    """Résumé court pour notifications ou dashboard rapide"""
    return """
Analyse fondamentale d’une entreprise = évaluer si l’action est sous-évaluée ou surévaluée.
Clés :
- Compte de résultat, Bilan, Flux de trésorerie
- Ratios : PER, P/B, ROE, ROA
- Approche top-down : économie → secteur → entreprise
- Comparer croissance, marges, dettes avec concurrents
"""

def get_full_analyse_entreprise_explanation() -> str:
    """Explication complète pour documentation ou formation"""
    parts = [
        ANALYSE_ENTREPRISE_INTRODUCTION,
        "\n\n" + BENEFICES_ET_RAPPORTS_FINANCIERS,
        "\n\nRatios financiers :\n" + RATIOS_FINANCIERS_IMPORTANTS,
        "\n\nFacteurs plus larges (approche top-down) :\n" + FACTEURS_PLUS_LARGES_ET_APPROCHE_DESCENDANTE,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_ANALYSE_ENTREPRISE)
    ]
    return "".join(parts)


# Pour tester / visualiser
if __name__ == "__main__":
    print(get_analyse_entreprise_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_analyse_entreprise_explanation())

"""
Masse salariale non agricole (NFP - Non-Farm Payrolls)
Version : 1.0
Connaissances clés pour traders Forex sur le rapport NFP
"""

NFP_INTRODUCTION = """
Le rapport sur la **masse salariale non agricole (NFP)** est l'un des événements économiques 
les plus importants et les plus volatils du mois sur les marchés financiers, en particulier sur le Forex.

Il s'agit du rapport mensuel américain qui mesure la création (ou destruction) nette d'emplois 
hors secteur agricole, ménages privés et organisations à but non lucratif aux États-Unis.
"""

QU_EST_CE_QUE_LE_NFP = """
**Contenu du rapport** (publié dans "Employment Situation Summary") :
- **Non-Farm Payrolls** : nombre net d'emplois créés / perdus le mois précédent
- **Taux de chômage** (Unemployment Rate)
- **Salaire horaire moyen** (Average Hourly Earnings) – indicateur d'inflation salariale
- **Taux de participation à la force de travail** (Participation Rate)
- Révisions des deux mois précédents

**Publication** :
- Premier vendredi du mois à 8h30 ET (13h30 GMT / 14h30 heure de Paris)
- Couvre les données du mois précédent
- Publié par le Bureau of Labor Statistics (BLS)
"""

POURQUOI_LE_NFP_EST_IMPORTANT = """
La Réserve fédérale (Fed) a un **double mandat** :
1. Plein emploi (maximum employment)
2. Stabilité des prix (~2 % d'inflation)

Le NFP est l'indicateur le plus direct et le plus fiable sur l'état du marché du travail américain.
→ Emploi fort (NFP élevé + salaire en hausse) → Fed plus susceptible de **resserrement** (hausse des taux)
→ Emploi faible (NFP bas + chômage en hausse) → Fed plus susceptible d’**assouplissement** (baisse ou maintien des taux)

Puisque les États-Unis représentent la première économie mondiale, les décisions de la Fed influencent fortement :
- Le dollar américain (USD)
- Les marchés mondiaux (actions, obligations, matières premières, Forex)
"""

IMPACT_SUR_LE_MARCHE_DES_CHANGES = """
**Règles générales d'impact (sur USD)** :

- **NFP nettement supérieur aux attentes** (surtout > +200 000) → USD ↑ (forte appréciation)
- **NFP conforme aux attentes** → volatilité faible à modérée
- **NFP nettement inférieur aux attentes** → USD ↓ (affaiblissement)

Composantes très regardées :
- **Salaire horaire moyen** : hausse → pression inflationniste → USD positif
- **Taux de chômage** : baisse → positif pour USD

**Surprises vs consensus** :
- L'écart par rapport aux prévisions (Bloomberg, Reuters, etc.) est souvent plus important que le chiffre absolu
- Révisions des mois précédents peuvent changer la réaction

**Volatilité** :
- Mouvements de 50 à 200+ pips possibles en quelques minutes sur EURUSD, GBPUSD, USDJPY, etc.
- Spreads très élargis juste avant/après publication
"""

COMMENT_EXPLOITER_LES_DONNEES_NFP = """
Options courantes des traders :

1. **Clôturer toutes les positions avant** (le plus prudent)  
   → Évite les gaps, spreads élargis et appels de marge

2. **Ne pas trader pendant la publication**  
   → Attendre 15–60 minutes que la volatilité initiale se calme

3. **Trader la réaction immédiate** (scalping)  
   → Très risqué, nécessite exécution rapide et faible latence

4. **Trader après la poussière retombe**  
   → Observer la direction réelle + niveaux techniques (retracement, support/résistance)

**Risques majeurs** :
- Gaps qui sautent les stops
- Volatilité extrême dans les 1–5 premières minutes
- Mouvement en V (hausse puis inversion rapide)
"""

DEUX_FACONS_DE_NEGOCIER_LES_NFP = """
1. **Avant la publication** (anticipation) :
   - Basé sur consensus + biais macro (inflation, croissance, discours Fed)
   - Utiliser ordres pendants (buy stop / sell stop)
   - Stop loss large obligatoire (risque de gap)
   - Instrument très liquide et volatil (EURUSD, USDJPY, Gold souvent)

2. **Après la publication** (réaction) :
   - Attendre la première impulsion (1–10 min)
   - Chercher un retracement (pullback) vers un niveau technique
   - Entrer dans la direction du mouvement principal si confirmation
   - Stratégie de repli (fade the spike) souvent utilisée

Exemple classique : NFP très décevant → USD chute immédiatement → retracement haussier → achat sur le pullback
"""

STRATEGIE_DE_REPLI_APRES_NFP = """
**Stratégie la plus citée** : **le retracement / pullback post-NFP**

Principe :
- Attendre la réaction initiale violente (souvent exagérée)
- Observer un retour vers un niveau clé (Fibonacci 38.2/50/61.8 %, VWAP, support/résistance)
- Entrer dans la direction du mouvement principal avec stop serré

Exemple historique (mars 2019) :
- Consensus : ~180 000 emplois
- Réel : +20 000 (très décevant)
- Réaction immédiate : EURUSD monte fortement
- Puis retracement rapide → retour sous le niveau pré-NFP
- Entrée longue sur retracement → mouvement haussier ensuite

**Règle** : pas de garantie absolue → toujours stop loss + gestion stricte du risque
"""

AUTRES_CHIFFRES_DE_L_EMPLOI = """
Le NFP concerne uniquement les États-Unis.  
Pour les autres devises, surveiller les équivalents :

- **Zone Euro** : Taux de chômage, emploi Eurostat
- **Royaume-Uni** : Claimant Count Change, ILO Unemployment Rate
- **Australie** : Employment Change, Unemployment Rate
- **Canada** : Employment Change, Unemployment Rate
- **Japon** : Unemployment Rate, Jobs-to-Applicants Ratio
- **Suisse** : Unemployment Rate

Ces données ont un impact moindre que le NFP, mais restent importantes pour les paires concernées.
"""

PRINCIPAUX_ENSEIGNEMENTS_NFP = [
    "Le NFP est l'indicateur le plus volatil du mois sur le Forex",
    "NFP > attentes + salaires en hausse → USD plus fort",
    "NFP < attentes → USD plus faible",
    "La surprise par rapport au consensus compte plus que le chiffre absolu",
    "Éviter d’être en position juste avant (spreads + gaps)",
    "La réaction immédiate est souvent exagérée puis corrigée",
    "Stratégie de retracement (pullback) très utilisée après publication",
    "Aucune stratégie n’est infaillible – gestion du risque obligatoire",
    "Surveiller salaire horaire et taux de chômage en complément"
]

def get_nfp_summary() -> str:
    """Résumé court pour notifications ou logs"""
    return """
Le NFP mesure les emplois créés aux USA (hors agriculture).
Publié 1er vendredi du mois à 13h30 GMT.
→ NFP fort > attentes → USD ↑ (hausse probable des taux)
→ NFP faible < attentes → USD ↓
Très forte volatilité → prudence extrême (spreads, gaps).
Meilleure approche : attendre retracement post-publication.
"""

def get_full_nfp_explanation() -> str:
    """Explication complète pour dashboard, formation ou référence"""
    parts = [
        NFP_INTRODUCTION,
        "\n\n" + QU_EST_CE_QUE_LE_NFP,
        "\n\n" + POURQUOI_LE_NFP_EST_IMPORTANT,
        "\n\nImpact Forex :\n" + IMPACT_SUR_LE_MARCHE_DES_CHANGES,
        "\n\nComment exploiter :\n" + COMMENT_EXPLOITER_LES_DONNEES_NFP,
        "\n\nDeux façons de trader :\n" + DEUX_FACONS_DE_NEGOCIER_LES_NFP,
        "\n\nStratégie de repli :\n" + STRATEGIE_DE_REPLI_APRES_NFP,
        "\n\nAutres chiffres emploi :\n" + AUTRES_CHIFFRES_DE_L_EMPLOI,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_NFP)
    ]
    return "".join(parts)


# Pour tester
if __name__ == "__main__":
    print(get_nfp_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_nfp_explanation())
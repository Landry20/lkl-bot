
"""
Produit Intérieur Brut (PIB / GDP)
Version : 1.0
Connaissances clés pour traders Forex sur le PIB
"""

PIB_INTRODUCTION = """
Le Produit Intérieur Brut (PIB ou GDP en anglais) représente la **valeur totale marchande** 
de tous les biens et services finaux produits au sein d'une économie sur une période donnée 
(généralement un trimestre ou une année).

C'est l'indicateur le plus global et le plus suivi pour mesurer :
- La taille d'une économie
- Son taux de croissance (ou de contraction)
- Sa santé économique générale

Aux États-Unis, le Bureau of Economic Analysis (BEA) le décrit comme « l'indicateur le plus suivi de l'économie américaine ».
"""

PIB_COMPOSITION = """
Le PIB est calculé selon trois approches équivalentes :
1. Approche par la production (valeur ajoutée par secteur)
2. Approche par les dépenses :
   - Consommation des ménages (C) ≈ 70 % aux USA
   - Investissement des entreprises (I)
   - Dépenses publiques (G)
   - Exportations nettes (X - M)
   → Formule célèbre : PIB = C + I + G + (X - M)
3. Approche par les revenus (salaires, profits, intérêts, etc.)

Pour les traders Forex, c'est surtout **la variation trimestrielle annualisée** qui compte.
"""

PIB_PUBLICATION = """
Publication typique (États-Unis – BEA) :
- Trois estimations par trimestre :
  1. **Advance / Preliminary** (estimation avancée) → ~4 semaines après fin du trimestre → plus impactante
  2. **Second estimate** (révision intermédiaire)
  3. **Final estimate** (définitif) → ~3 mois après fin du trimestre
- Autres pays : trimestriel (Zone Euro, UK, Japon, Canada, Australie, etc.)
- Certaines économies (Chine, Inde) publient aussi des données annuelles ou trimestrielles très suivies

Calendrier : très prévisible → à ajouter dans ton agenda ou calendrier économique
"""

TAUX_DE_CROISSANCE_IDEAL = """
Taux de croissance annuel considéré comme sain par la majorité des économistes :
- **2 % à 3 %** → croissance équilibrée, sans surchauffe ni récession
  - Permet création d'emplois, hausse du niveau de vie
  - Inflation modérée

Interprétation :
- < 1 % → croissance faible → risque de stagnation / récession → banque centrale dovish
- 0 % ou négatif → récession technique (deux trimestres consécutifs négatifs)
- > 4–5 % → croissance forte → risque de surchauffe et d'inflation → banque centrale hawkish
"""

IMPACT_IMMEDIAT_SUR_LE_FOREX = """
Réaction typique à la publication du PIB (surtout US) :

1. **PIB réel > prévisions (surprise positive)**  
   → Devise ↑ (USD plus fort si US)  
   → Anticipation de resserrement monétaire ou économie robuste

2. **PIB réel dans la fourchette des attentes**  
   → Réaction faible à nulle  
   → Nécessite de comparer avec trimestre précédent et autres pays

3. **PIB réel < prévisions (surprise négative)**  
   → Devise ↓ (USD plus faible)  
   → Anticipation de politique plus accommodante

Plus l'écart (surprise) est grand → plus la volatilité est forte (souvent 50–150+ pips en quelques minutes sur les paires majeures).
"""

TENDANCES_LONG_TERME_ET_PIB = """
Le PIB a un impact plus structurel que immédiat :
- Une économie dont le PIB croît régulièrement plus vite que ses concurrents → sa devise a tendance à s'apprécier sur le long terme
- Exemple historique (2009–2015) :
  - USA : croissance plus rapide que la Zone Euro après la crise de 2008
  - Résultat : EUR/USD a fortement baissé (de ~1.50 en 2008 vers 1.05–1.10 en 2015)
- Crise de la dette souveraine européenne + croissance américaine plus solide → euro affaibli durablement

Règle : comparer le différentiel de croissance PIB entre deux zones → influence le biais long terme d'une paire
"""

REACTION_DES_TRADERS_AUX_DONNEES_PIB = """
Conseils pratiques pour les traders Forex :

- **Court terme** :
  - La réaction immédiate est souvent exagérée puis corrigée
  - Attendre 5–30 minutes après publication pour éviter la volatilité initiale
  - Utiliser niveaux techniques (supports/résistances, Fibonacci) pour entrer sur retracement

- **Moyen/long terme** :
  - Une seule publication ne change pas le tableau fondamental
  - Regarder la **tendance** sur plusieurs trimestres + révisions
  - Comparer PIB US vs Zone Euro vs UK vs Japon → biais sur EURUSD, GBPUSD, USDJPY

- **Pièges courants** :
  - PIB conforme aux attentes → souvent peu de mouvement
  - PIB fort mais banque centrale dovish → devise peut baisser malgré tout
  - Révisions des trimestres précédents peuvent être plus importantes que le chiffre actuel

- **Combinaison** : PIB + inflation (CPI) + emploi (NFP) + politique monétaire donne une vision beaucoup plus complète
"""

PRINCIPAUX_ENSEIGNEMENTS_PIB = [
    "Le PIB mesure la croissance économique globale d'un pays",
    "Croissance saine : 2–3 % par an",
    "PIB > attentes → devise généralement plus forte (court terme)",
    "L'impact immédiat est souvent volatile et corrigé ensuite",
    "Les tendances de croissance à long terme influencent fortement les mouvements structurels des devises",
    "Toujours comparer avec les autres grandes économies",
    "Une seule donnée PIB ne suffit pas à inverser un biais fondamental",
    "Éviter les positions juste avant la publication (volatilité)",
    "Utiliser en combinaison avec CPI, NFP, décisions de taux"
]

def get_pib_summary() -> str:
    """Résumé court pour notifications, logs ou dashboard rapide"""
    return """
Le PIB mesure la valeur totale des biens et services produits dans une économie.
- Croissance saine : 2–3 % par an
- PIB > attentes → devise ↑ (anticipation de taux plus hauts)
- PIB < attentes → devise ↓
- Impact plus structurel que spéculatif : influence le biais long terme des paires
- Volatilité forte sur les surprises, mais souvent corrigée après.
"""

def get_full_pib_explanation() -> str:
    """Explication complète pour documentation ou formation"""
    parts = [
        PIB_INTRODUCTION,
        "\n\n" + PIB_COMPOSITION,
        "\n\nPublication : " + PIB_PUBLICATION,
        "\n\nTaux idéal :\n" + TAUX_DE_CROISSANCE_IDEAL,
        "\n\nImpact immédiat Forex :\n" + IMPACT_IMMEDIAT_SUR_LE_FOREX,
        "\n\nTendances long terme :\n" + TENDANCES_LONG_TERME_ET_PIB,
        "\n\nComment réagir en trading :\n" + REACTION_DES_TRADERS_AUX_DONNEES_PIB,
        "\n\nPrincipaux enseignements :",
        "\n• " + "\n• ".join(PRINCIPAUX_ENSEIGNEMENTS_PIB)
    ]
    return "".join(parts)


# Pour tester rapidement
if __name__ == "__main__":
    print(get_pib_summary())
    print("\n" + "="*80 + "\n")
    print(get_full_pib_explanation())
# knowledge/savoir/discours_et_narratifs/interpretation_discours.py
"""
Interprétation des discours - Règles pratiques pour trader + alertes bot
Version : 2.0
"""

INTERPRETATION_INTRO = """
Interpréter un discours n’est pas subjectif : il existe des **mots-clés**, **phrases types** et **changements de ton** qui sont devenus des signaux de marché très suivis.

Règles générales :
- 1 mot peut changer 200 pips (ex. "patient" → "vigilant")
- Le Q&A (questions-réponses) est souvent plus révélateur que le texte lu
- Comparer avec discours précédent = détecter pivot
"""

CHECKLIST_INTERPRETATION_DISCOURS = """
1. **Mots inflation** :
   - Persistante / entrenched / sticky → hawkish
   - Transitoire / temporary / moderating → dovish
   - "Progress but not enough" → hawkish modéré

2. **Mots croissance/emploi** :
   - Resilient / strong → hawkish
   - Cooling / downside risks / weakening → dovish

3. **Forward guidance** :
   - "Higher for longer", "restrictive for some time" → hawkish
   - "We can be patient", "no rush", "data will tell" → dovish

4. **Dot plot / projections** :
   - Plus de hausses que consensus → hawkish
   - Moins de hausses ou cuts anticipés → dovish

5. **Changements subtils** :
   - "We are attentive" → "We are concerned" = pivot hawkish
   - "Balanced risks" → "Downside risks predominate" = pivot dovish

6. **Conférence de presse pièges** :
   - Réponse agacée ou défensive → ton plus hawkish/dovish que prévu
   - "I don’t want to pre-commit" → souvent dovish caché
"""

ALERTES_BOT_LKL = """
Règles alertes Telegram / backend LKL :
- Phrase avec "persistent" ou "higher for longer" → Alert "HAWKISH – USD long potentiel"
- Phrase avec "patient" répété + "no hurry" → Alert "DOVISH – USD short potentiel"
- Dot plot shift +0.5% ou +1 hike → Alert "HAWKISH SURPRISE"
- Q&A président dit "we are concerned about inflation" → Alert "PIVOT HAWKISH"
- Mots "sanctions" / "tariffs" dans discours président → Alert "GEOPO + USD"
"""

EXEMPLES_INTERPRETATION = """
- Powell 26/08/2022 Jackson Hole : "Restoring price stability will likely require maintaining a restrictive policy stance for some time" → hawkish clair → USD rally
- Lagarde juillet 2022 : "We will do whatever it takes to bring inflation back" → hawkish → EUR rebond
- Powell mars 2024 : "We are gaining greater confidence that inflation is moving sustainably toward 2%" → dovish pivot → USD ↓
- BoJ Ueda 2024 : "We will continue YCC for now" → yen faible persistant
"""

def get_interpretation_summary():
    return """
Interprétation discours :
Hawkish = "persistent", "higher for longer", "restrictive"
Dovish = "patient", "data dependent", "downside risks"
Alertes LKL : mots-clés inflation + forward guidance + Q&A
"""

def get_full_interpretation():
    return (
        INTERPRETATION_INTRO + "\n\n" +
        CHECKLIST_INTERPRETATION_DISCOURS + "\n\n" +
        ALERTES_BOT_LKL + "\n\n" +
        EXEMPLES_INTERPRETATION
    )
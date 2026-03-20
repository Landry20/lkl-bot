
"""
Indicateurs Avancés Macro - ISM, JOLTS, Commandes industrielles, etc.
Version : 2.0 - Cours détaillé pour anticiper les tendances
"""

INDICATEURS_AVANCES_INTRO = """
Les indicateurs avancés (leading indicators) donnent des signaux **avant** les données officielles (PIB, emploi, inflation).

Ils permettent au bot LKL :
- D’anticiper les surprises NFP/CPI/PIB
- D’ajuster le biais avant les annonces majeures
- De détecter les tournants de cycle
"""

PRINCIPAUX_INDICATEURS_AVANCES = """
1. **ISM Manufacturing PMI** (US)
   - >50 : expansion → USD positif
   - <50 : contraction → USD négatif
   - Composantes clés : Nouvelles commandes, Emploi, Prix payés
   - Publication : 1er jour ouvrable du mois – 15h00 GMT

2. **ISM Services PMI** (US)
   - Plus important que manufacturing (services = 70 % économie US)
   - Impact similaire à NFP en termes de volatilité

3. **JOLTS (Job Openings and Labor Turnover Survey)** – US
   - Offres d’emploi : >8M → marché travail tendu → inflation ↑ → USD ↑
   - Quits rate : élevé → pouvoir salariés → salaires ↑
   - Publication : début de mois – 15h00 GMT

4. **Commandes industrielles / Production industrielle** – US, Allemagne, Chine
   - Commandes ↑ → croissance future → devise ↑
   - Allemagne très suivi (leader Eurozone)

5. **Indicateurs de confiance** :
   - Confiance consommateurs (Michigan, Conference Board) – US
   - ZEW / IFO – Allemagne (très corrélé EUR)
   - Confiance entreprises → investissement futur

6. **Indicateurs avancés Chine** (très important pour AUD/NZD/CAD)
   - Caixin PMI Manufacturier/Services
   - Crédit social, ventes immobilières
"""

IMPACTS_FOREX_CONCRETS = """
- ISM Manufacturing >52 + surprise → USD ↑ 50–100 pips
- JOLTS offres >9M → anticipation NFP fort → USD pré-hausse
- Caixin Chine <50 → AUD/NZD/CAD ↓ anticipé
- ZEW Allemagne très négatif → EURUSD ↓ avant PIB Eurozone
"""

REGLES_INTEGRATION_BOT_LKL = """
Règles automatiques :
- ISM US Flash <50 → réduire exposition USD longs
- JOLTS offres ↑ + ISM emploi ↑ → biais NFP hawkish → préparer USD long
- Caixin Chine faible → alerte "RISK COMMODITIES" → AUD/NZD short potentiel
- Chaînage indicateurs : ISM + JOLTS + Confiance → score anticipation NFP (0–100)
- Backend : envoyer score anticipation au Laravel avant NFP/CPI
"""

def get_indicateurs_avances_summary():
    return """
Indicateurs avancés : ISM PMI, JOLTS, commandes industrielles, Caixin Chine.
Utilité : anticiper NFP/CPI/PIB → ajuster biais avant annonces.
"""

def get_full_indicateurs_avances():
    return (
        INDICATEURS_AVANCES_INTRO + "\n\n" +
        PRINCIPAUX_INDICATEURS_AVANCES + "\n\n" +
        IMPACTS_FOREX_CONCRETS + "\n\n" +
        REGLES_INTEGRATION_BOT_LKL
    )
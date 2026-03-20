
"""
Balance Commerciale & Compte Courant - Impact Forex
Version : 2.0 - Cours détaillé
"""

BALANCE_COMMERCIALE_INTRO = """
La balance commerciale = Exportations – Importations de biens et services.
Elle fait partie du **compte courant** (balance commerciale + revenus + transferts).

Règle de base :
- Surplus commercial → demande de la devise ↑ → appréciation
- Déficit commercial → offre de la devise ↑ → dépréciation

Impact réel : plus fort sur devises commodity et petites économies
"""

IMPACTS_PAR_TYPE_DE_DEVISE = """
1. **Commodity currencies** (AUD, CAD, NZD, NOK, RUB) :
   - Surplus → prix matières premières ↑ → devise très forte
   - Exemple : Pétrole ↑ → Canada exporte plus → CAD ↑ (USDCAD ↓)

2. **Grandes économies** (USD, EUR, JPY) :
   - Impact plus faible (flux capitaux dominent)
   - Déficit US chronique → USD ↓ pression long terme (mais refuge compense)

3. **Émergents** (TRY, ZAR, MXN, BRL) :
   - Déficit → vulnérabilité → dépréciation rapide en risk-off

Autres facteurs :
- Balance énergétique : Gaz ↑ → NOK ↑, EUR ↓ (importateur)
- Balance manufacturière : Chine surplus → CNY ↑ pression (contrôlé)
"""

EXEMPLES_HISTORIQUES = """
- Australie 2010–2013 : Boom minier Chine → AUDUSD >1.10
- Canada 2022 : Pétrole spike → USDCAD <1.25
- Eurozone 2011–2012 : Déficit énergie + dette → EURUSD <1.20
- Japon 2013–2015 : Déficit commercial (nucléaire arrêté) → JPY faible malgré carry
"""

REGLES_TRADING_LKL = """
- Prix pétrole +10 % → long USDCAD, short EURUSD
- Balance Chine faible → short AUDUSD, NZDUSD
- Surplus Eurozone + croissance faible → EUR stable ou ↓ (carry vs croissance)
- Filtre bot : Si balance US surprise négative + inflation haute → USD hawkish quand même
"""

def get_balance_summary():
    return """
Balance commerciale : Surplus → devise ↑ | Déficit → devise ↓
Fort impact : AUD, CAD, NOK (commodities)
Faible impact : USD, EUR, JPY (flux capitaux dominent)
"""

def get_full_balance():
    return (
        BALANCE_COMMERCIALE_INTRO + "\n\n" +
        IMPACTS_PAR_TYPE_DE_DEVISE + "\n\n" +
        EXEMPLES_HISTORIQUES + "\n\n" +
        REGLES_TRADING_LKL
    )
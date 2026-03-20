
"""
Discours des Présidents, Gouvernements et Leaders Politiques - Impact Forex
Version : 2.0 - Focus sur narratifs économiques et géopolitiques
"""

PRESIDENTS_GOUVERNEMENTS_INTRO = """
Les discours politiques (présidents, ministres des finances, ministres des affaires étrangères) 
ont un impact **indirect mais parfois très fort** sur les devises, surtout quand ils touchent :
- La politique budgétaire (dépenses, dette, taxes)
- Les relations internationales (tarifs, sanctions, alliances)
- La perception de stabilité politique
"""

TYPES_DE_NARRATIFS_POLITIQUES = """
1. **Fiscal hawk / fiscal dove** :
   - Fiscal hawk : "réduire déficit", "contrôle dette" → devise ↑ (crédibilité)
   - Fiscal dove : "dépenses massives", "stimulus" → devise ↓ si dette inquiétante

2. **Protectionnisme / tarifs** :
   - Tarifs élevés → devise du pays imposant ↑ court terme, mais ↓ moyen terme (ralentissement commerce)
   - Exemple Trump 2018–2020 : tarifs Chine → USD ↑ initial, puis AUD/CNY ↓

3. **Stabilité politique interne** :
   - Crise gouvernementale, élections serrées, impeachment → devise ↓
   - Exemple GBP 2022 Truss mini-budget → GBP crash 1.03

4. **Géopolitique / diplomatie** :
   - "Nous défendrons Taiwan" → USD ↑, CNY ↓, AUD/JPY sensibles
   - "Sanctions renforcées" → devise ciblée ↓, or ↑
   - "Accord commercial" → devises concernées ↑

5. **Narratif populiste vs institutionnel** :
   - Populiste (anti-élite, anti-banque centrale) → devise ↓ (crainte instabilité)
   - Institutionnel / pro-marché → devise stable ou ↑
"""

EXEMPLES_IMPACTS_RECENTS = """
- Trump 2024 réélection discours : "tarifs 60% Chine" → USD ↑, CNY ↓ contrôlé, AUD/NZD ↓
- Macron 2024 dissolution Assemblée → EUR ↓ temporaire (incertitude politique France)
- Meloni Italie 2022–2025 : discours pro-UE et stabilité → EUR stable
- Milei Argentine 2023 : discours ultra-libéral → peso rebond initial puis volatilité
- Sunak / Starmer UK 2024 : discours fiscal prudent → GBP stable
"""

REGLES_TRADING_POLITIQUE_LKL = """
Règles LKL Bot :
- Élection serrée ou crise gouvernementale → short devise concernée (GBP, EUR, etc.)
- Discours protectionniste fort → long USD, short AUD/CNY
- "Dette hors de contrôle" → devise ↓ + or ↑
- Alert Telegram si président/ministre dit "sanctions" ou "tarifs" sur pays majeur
- Backend : bloquer trades si VIX >35 + news politique majeure
"""

def get_presidents_summary():
    return """
Présidents/gouvernements :
Fiscal hawk → devise ↑ | Fiscal dove / populiste → devise ↓
Tarifs / protectionnisme → USD ↑ court terme
Crise politique → devise concernée crash
"""

def get_full_presidents():
    return (
        PRESIDENTS_GOUVERNEMENTS_INTRO + "\n\n" +
        TYPES_DE_NARRATIFS_POLITIQUES + "\n\n" +
        EXEMPLES_IMPACTS_RECENTS + "\n\n" +
        REGLES_TRADING_POLITIQUE_LKL
    )
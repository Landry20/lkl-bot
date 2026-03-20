
"""
Comportements de marché & psychologie des traders - Impact Forex
Version : 2.0 - Très détaillé avec exemples et pièges classiques
"""

PSYCHOLOGIE_INTRODUCTION = """
Les mouvements de prix ne sont pas seulement macro ou fondamentaux : 
70 % des mouvements à court/moyen terme sont drivés par la psychologie collective 
et les comportements prévisibles des différents types de traders.
"""

BIAS_COGNITIFS_IMPORTANTS = """
1. **FOMO** (Fear Of Missing Out)
   - Comportement : achats panique quand le prix accélère
   - Impact : exhaustion tops, blow-off tops
   - Exemple : BTC 69k 2021, EURUSD 1.23 2021 → reversal violent

2. **FUD** (Fear, Uncertainty, Doubt)
   - Comportement : ventes panique sur news négatives
   - Impact : capitulation bottoms
   - Exemple : GBPUSD 1.03 2022 (Truss crisis) → bottom puis rebond

3. **Herding** (effet de troupeau)
   - Comportement : tout le monde suit la même direction
   - Impact : overshooting → mouvement exagéré puis retour brutal
   - Exemple : USDJPY 151–161 2023 → herding carry → intervention BoJ

4. **Anchoring** (ancrage)
   - Comportement : fixation sur niveaux psychologiques (1.1000, 150.00, 2000 or)
   - Impact : supports/résistances très forts
   - Exemple : EURUSD bloque longtemps à 1.2000, puis cassure → forte accélération

5. **Loss aversion** + **Disposition effect**
   - Comportement : couper gains trop tôt, laisser pertes courir
   - Impact : stops chassés en dessous support, puis vrai mouvement
   - Exemple : stop hunting classique avant NFP (prix descend chasser stops retail, puis monte)

6. **Confirmation bias**
   - Comportement : voir seulement les news qui confirment sa position
   - Impact : traders long restent long malgré reversal macro
"""

PIEGES_CLASSIQUES_OBSERVES_EN_FOREX = """
1. **Stop hunting** : gros acteurs poussent le prix vers zones de stops retail (sous support, au-dessus résistance) avant vrai mouvement
2. **Fakeout / False breakout** : cassure d’un niveau puis retour immédiat (trap haussier/baissier)
3. **Liquidity grab** : prix va chercher liquidité (stops + ordres pendants) puis reversal
4. **News fade** : réaction initiale violente sur news → puis retour dans direction opposée
   Exemple : NFP très fort → USD monte 100 pips → puis redescend (fade)

Exemple concret 2023 :
EURUSD 1.1270 (résistance ronde) → fake breakout → stop hunting → chute 200 pips
"""

IMPACT_SUR_STRATEGIE_TRADING = """
- Ne jamais mettre stop sur niveau rond évident
- Attendre confirmation après news (pas rentrer dans première bougie)
- Chercher liquidité grab avant vrai mouvement
- Observer volume + order flow (si possible) pour détecter herding
- Utiliser time-based exits (fin session London/NY) pour éviter exhaustion
"""

def get_comportements_summary():
    return """
Psychologie Forex : FOMO (tops), FUD (bottoms), herding (overshoot), anchoring (niveaux ronds), stop hunting, fakeouts.
Pièges : news fade, liquidity grab, false breakouts.
"""

def get_full_comportements():
    return (
        PSYCHOLOGIE_INTRODUCTION + "\n\n" +
        BIAS_COGNITIFS_IMPORTANTS + "\n\n" +
        PIEGES_CLASSIQUES_OBSERVES_EN_FOREX + "\n\n" +
        IMPACT_SUR_STRATEGIE_TRADING
    )

"""
Cours Complet sur Cryptos / Bitcoin - Impacts, Facteurs de Mouvement, Géopolitique
Version : 2.0 - Étendu pour LKL Bot (BTCUSD, ETHUSD focus)
Allocation max 1% - Haut risque/volatilité
"""

CRYPTO_INTRODUCTION = """
Cryptos (focus Bitcoin BTCUSD) : Marché 24/7, volume 2T$ market cap 2026, volatilité extrême (500-2000$/jour BTC).
- BTC rôle : Digital gold, store of value, hedge inflation/censorship
- Acteurs : Whales (5%), miners (10%), institutions (30% post-ETF), retail (40%), bots (15%)
- Corrélations : +0.7 SP500 (risk-on asset), -0.5 USD (anti-fiat), +0.6 or (digital gold)
- Risques : Régulation, hacks, flash crashes, leverage liquidation cascades
- LKL Bot : 1% max, scalping 15min, news filter strict (ETF news, halving)
"""

BTC_IMPACTS = {
    "caracteristiques": "Fixed supply 21M, halving tous 4 ans (2024: 3.125 BTC/block), mining PoW",
    "facteurs_mouvement": [
        "Adoption institutionnelle : ETF approval 2024 → BTC >100k",
        "Inflation fiat : QE Fed → BTC ↑ (hedge dévaluation USD)",
        "Régulation : Ban Chine 2021 → BTC -50%, US SEC greenlight → ↑",
        "Géopolitique : Guerres (Ukraine) → BTC ↑ (refuge non-confiscable)",
        "Halving : Supply cut → BTC ↑ historique (+300% post-2020)",
        "Macro risk-on : SP500 ATH → BTC ↑, VIX >40 → BTC ↓ initial puis rebound",
        "Whales/memes : Elon tweets 2021 → +20%, FTX crash 2022 → -70%",
        "Energy/mining : Ban mining Russie → hashrate ↓ → BTC ↓ temporaire",
        "Exemple 2022 : Guerre Ukraine + Fed hikes → BTC 15k low (fear)",
        "Exemple 2024 : Halving + ETF → BTC 150k ATH",
        "Exemple 2025 : Géopolitique US-China → BTC +50% (dé-dollarisation)"
    ]
}

ETH_IMPACTS = {
    "caracteristiques": "Platform smart contracts, PoS depuis 2022, supply infini mais burns",
    "facteurs_mouvement": [
        "DeFi/NFT boom : ETH ↑ (gas fees)",
        "Upgrades : Merge 2022 → ETH +100% (éco-friendly)",
        "Régulation : SEC vs ETH securities → ↓ si négatif",
        "Géopolitique : Censure résistante → ETH ↑ en crises",
        "Corrélation BTC : ETH/BTC ratio 0.05-0.08, suit BTC bull/bear"
    ]
}

STRATEGIE_CRYPTO_LKL = """
**Règles strictes LKL Bot** :
- Max 1% capital (0.01 BTC/trade)
- Scalping 15-30min : Volatilité >5% jour = flat
- Long BTC si halving near + risk-on
- Hedge : BTC long si guerre/inflation, short si Fed hawkish
- News filter : ETF/regul alert Telegram + pause 1h
- Backend : Analyse impact géopolitique/macro avant trade
- Dashboard : Screenshot chart + 'BTC Impact: Guerre → Target 80k'"
"""

def get_crypto_summary() -> str:
    return """
BTC : Guerre/régulation/halving/inflation → ↑ massif (hedge digital gold). Volatilité extrême.
Exemples : Ukraine 2022 -70%, Halving 2024 +200%.
LKL : 1% max, long risk-on, hedge guerre.
ETH : Suit BTC + DeFi upgrades.
"""

def get_full_crypto_explanation() -> str:
    lines = [CRYPTO_INTRODUCTION, "\n\nBitcoin (BTCUSD) Impacts :\n"]
    lines.append(f"   Caractéristiques : {BTC_IMPACTS['caracteristiques']}")
    lines.append("   Facteurs Mouvement :")
    for item in BTC_IMPACTS['facteurs_mouvement']:
        lines.append(f"     - {item}")
    lines.append("\n\nEthereum (ETHUSD) Impacts :\n")
    lines.append(f"   Caractéristiques : {ETH_IMPACTS['caracteristiques']}")
    lines.append("   Facteurs Mouvement :")
    for item in ETH_IMPACTS['facteurs_mouvement']:
        lines.append(f"     - {item}")
    lines.append("\n\nStratégie LKL Bot :\n" + STRATEGIE_CRYPTO_LKL)
    return "\n".join(lines)
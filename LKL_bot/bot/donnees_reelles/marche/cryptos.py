import MetaTrader5 as mt5

def get_crypto_data(symbol):
    """
    Récupère les données pour les cryptomonnaies (BTCUSD, ETHUSD, etc.) via MT5.
    """
    symbol_info = mt5.symbol_info(symbol)
    if not symbol_info:
        return None
    
    tick = mt5.symbol_info_tick(symbol)
    return {
        'symbol': symbol,
        'price': tick.bid if tick else None,
        'spread': symbol_info.spread,
        'type': 'CRYPTO'
    }

def analyser_sentiment_crypto(symbol):
    """
    Simule une analyse de sentiment spécifique aux cryptos (Fear & Greed Index logic).
    """
    # Ici on pourrait appeler une API externe type Alternative.me
    return "Optimisme modéré sur la blockchain. ⛓️✨"

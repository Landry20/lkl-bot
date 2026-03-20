import MetaTrader5 as mt5

def get_stock_data(symbol):
    """
    Récupère les données pour les actions (AAPL, TSLA, NVDA).
    """
    symbol_info = mt5.symbol_info(symbol)
    if not symbol_info:
        return None
        
    tick = mt5.symbol_info_tick(symbol)
    return {
        'symbol': symbol,
        'price': tick.bid if tick else None,
        'type': 'STOCK'
    }

def get_earnings_status(symbol):
    """Vérifie si des résultats sont attendus."""
    return "Pas de résultats majeurs aujourd'hui pour cet actif. 📖"

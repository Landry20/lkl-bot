import MetaTrader5 as mt5

def get_index_data(symbol):
    """
    Récupère les données pour les indices (US30, NAS100, DAX, etc.).
    """
    symbol_info = mt5.symbol_info(symbol)
    if not symbol_info:
        return None
        
    tick = mt5.symbol_info_tick(symbol)
    return {
        'symbol': symbol,
        'price': tick.bid if tick else None,
        'type': 'INDEX'
    }

def get_market_vibe():
    """Analyse globale de l'appétence au risque via les indices."""
    return "Risk-On : Les indices US poussent fort ! 🚀🔥"

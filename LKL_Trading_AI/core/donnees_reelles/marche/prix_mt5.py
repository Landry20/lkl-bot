import MetaTrader5 as mt5

def get_current_price(symbol):
    """
    Récupère le dernier prix (Tick) pour un symbole.
    """
    tick = mt5.symbol_info_tick(symbol)
    if tick:
        return tick.bid
    return None

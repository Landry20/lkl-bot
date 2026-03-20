import MetaTrader5 as mt5
from configuration import LOT_SIZE
from communication.envoi_backend import send_to_laravel
from communication.notifications import send_notification

def calculate_lot(symbol, sl_pips):
    """
    Calcule le lot en fonction du capital.
    """
    account = mt5.account_info()
    balance = account.balance if account else 0
    
    if balance < 100:
        return 0.01
    elif balance < 300:
        return 0.02
    else:
        return 0.05

def open_trade(user_id, symbol, action, ta_data):
    """
    Ouvre une position avec gestion du risque basique.
    """
    from connexion_mt5 import place_order # Import tardif pour éviter import circulaire
    lot = calculate_lot(symbol, 0)
    price = ta_data['price']
    atr = ta_data['atr']
    sl = price - atr * 2 if action == "buy" else price + atr * 2
    tp = price + atr * 3 if action == "buy" else price - atr * 3

    result = place_order(user_id, symbol, action, sl=sl, tp=tp)
    return result

def check_breakeven():
    """
    Sécurise les positions en profit.
    """
    positions = mt5.positions_get()
    if not positions:
        return
    for pos in positions:
        if "LKL" not in pos.comment:
            continue
        
        symbol_info = mt5.symbol_info(pos.symbol)
        if not symbol_info: continue
        
        profit_pips = abs(pos.price_current - pos.price_open) / symbol_info.point
        
        if profit_pips > 35: # Breakeven après 35 pips
            request = {
                "action": mt5.TRADE_ACTION_SLTP,
                "position": pos.ticket,
                "sl": pos.price_open,
                "tp": pos.tp
            }
            mt5.order_send(request)
            print(f"[RISK] BE activé pour {pos.symbol}")
            
            # Info au backend
            send_to_laravel('trades/update', {
                'ticket': pos.ticket,
                'status': 'BE_ACTIVATED',
                'symbol': pos.symbol
            })

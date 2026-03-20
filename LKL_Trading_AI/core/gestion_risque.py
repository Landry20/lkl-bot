import MetaTrader5 as mt5
from core.config_manager import config
from core.notification_manager import notification_manager

def calculate_lot(symbol, sl_pips):
    """
    Calcule le lot en fonction du capital.
    """
    account = mt5.account_info()
    balance = account.balance if account else 0
    
    # Simple logic for now, can be enhanced with config
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
    from core.connexion_mt5 import place_order # Import local
    
    price = ta_data['price']
    atr = ta_data.get('atr', 0.0010) # Default ATR if missing
    sl = price - atr * 2 if action == "buy" else price + atr * 2
    tp = price + atr * 3 if action == "buy" else price - atr * 3

    # user_id is unused in local mode but kept for signature compatibility if needed, else ignore
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
            res = mt5.order_send(request)
            if res.retcode == mt5.TRADE_RETCODE_DONE:
                print(f"[RISK] BE activé pour {pos.symbol}")
                notification_manager.send("Breakeven", f"BE activé pour {pos.symbol}", "INFO")

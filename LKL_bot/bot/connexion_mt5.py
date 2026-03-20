import datetime
import MetaTrader5 as mt5
import requests
from configuration import MT5_LOGIN, MT5_PASSWORD, MT5_SERVER, LOT_SIZE, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from communication.notifications import send_notification

import os

def find_terminal_path():
    """Cherche le chemin de terminal64.exe dans les emplacements communs."""
    paths = [
        r"C:\Program Files\MetaTrader 5\terminal64.exe",
        r"C:\Program Files (x86)\MetaTrader 5\terminal64.exe",
    ]
    appdata = os.getenv('APPDATA')
    if appdata:
        paths.append(os.path.join(appdata, "MetaQuotes", "Terminal", "terminal64.exe"))
    
    for p in paths:
        if os.path.exists(p):
            return p
    return None

def init(login=None, password=None, server=None):
    if not mt5.initialize():
        path = find_terminal_path()
        if path:
            if not mt5.initialize(path=path):
                return False, f"Échec Init MT5: {mt5.last_error()}"
        else:
            return False, "MT5 non trouvé."

    if not login or not password or not server:
        return False, "Identifiants MT5 manquants."
    
    if not mt5.login(int(login), password, server):
        err = f"Login échoué. Code: {mt5.last_error()}"
        mt5.shutdown()
        return False, err
        
    return True, "Success"

def send_telegram(msg: str):
    """Notification externe (Telegram) - Acceptable car non-Laravel"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}, timeout=5)
    except:
        pass

def place_order(user_id, symbol, action, sl=None, tp=None):
    symbol_info = mt5.symbol_info(symbol)
    if not symbol_info:
        send_notification(user_id, "error", f"Symbole {symbol} non trouvé.")
        return None
        
    tick = mt5.symbol_info_tick(symbol)
    if not tick:
        send_notification(user_id, "error", f"Prix indisponible pour {symbol}.")
        return None
        
    price = tick.ask if action == "buy" else tick.bid
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": LOT_SIZE,
        "type": mt5.ORDER_TYPE_BUY if action == "buy" else mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": sl or (price - 50 * symbol_info.point if action == "buy" else price + 50 * symbol_info.point),
        "tp": tp or (price + 100 * symbol_info.point if action == "buy" else price - 100 * symbol_info.point),
        "deviation": 20,
        "magic": 1001,
        "comment": f"LKL {symbol}",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    result = mt5.order_send(request)
    if result and result.retcode == mt5.TRADE_RETCODE_DONE:
        send_telegram(f"Trade {action.upper()} {symbol} @ {price:.5f}")
        return result
    else:
        err_msg = f"Échec {action.upper()} {symbol}: {result.retcode if result else 'Erreur'}"
        send_notification(user_id, "error", f"🚨 {err_msg}")
        return None

def get_account_info():
    acc = mt5.account_info()
    if not acc: return None
    
    now = datetime.datetime.now()
    start_day = datetime.datetime(now.year, now.month, now.day)
    history = mt5.history_deals_get(start_day, now)
    
    daily_profit = sum(deal.profit for deal in history) if history else 0.0
            
    return {
        'name': acc.name,
        'balance': acc.balance,
        'equity': acc.equity,
        'daily_profit': daily_profit
    }

def shutdown():
    mt5.shutdown()

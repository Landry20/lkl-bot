# bot/strategy.py
def get_strategy(symbol: str, ta: dict):
    confluence = len(ta['signals']) >= 1  # Au moins 1 signal
    price = ta['price']
    ma_cross = price > ta['ma20'] and ta['ma20'] > ta['ma50']  # Bullish cross

    if ta['action'] == 'buy' and confluence and price > ta['sr_minor_support']:
        tp_pips = 10 if ma_cross else 50  # Scalp 10 pips / Swing 50
        sl_pips = 5 if ma_cross else 25
        return {
            'type': 'SCALP' if ma_cross else 'SWING',
            'tp_pips': tp_pips,
            'sl_pips': sl_pips,
            'reason': f"Confluence: {', '.join(ta['signals'])} + S/R + MA"
        }

    if ta['action'] == 'sell' and confluence and price < ta['sr_minor_resistance']:
        tp_pips = 10 if not ma_cross else 50
        sl_pips = 5 if not ma_cross else 25
        return {
            'type': 'SCALP' if not ma_cross else 'SWING',
            'tp_pips': tp_pips,
            'sl_pips': sl_pips,
            'reason': f"Confluence: {', '.join(ta['signals'])} + S/R + MA"
        }

    return None

def get_strategy_v2(symbol: str, ta: dict):
    """
    Retourne les paramètres de sortie (SL/TP) basés sur la confluence L_K_L.
    """
    if not ta or not ta.get('action'):
        return None

    action = ta['action']
    price = ta['price']
    fibo = ta['fibo']
    h4 = ta['h4']
    
    # Calcul des pips (différence de prix / point)
    # Note: On laisse main.py gérer la conversion en prix réel
    
    # Stratégie L_K_L : Stop Loss basé sur l'invalidation Fibonacci
    sl_price = None
    tp_price = None

    if fibo:
        # On détermine à quel niveau la confirmation a eu lieu
        # (C'est une estimation basée sur la proximité du prix actuel)
        if action == 'buy':
            if abs(price - fibo['38.2']) < abs(price - fibo['50.0']):
                # Confirmation à 38.2% -> SL à 61.8%
                sl_price = fibo['61.8']
            elif abs(price - fibo['50.0']) < abs(price - fibo['61.8']):
                # Confirmation à 50% -> SL à 100% (ou début d'impulsion)
                sl_price = h4['price'] - (price - h4['price']) * 0.1 # Simulé
            else:
                # Confirmation à 61.8% -> SL à 100% (Début d'impulsion)
                sl_price = h4['price'] # Début du mouvement H4

            tp_price = price + (price - sl_price) * 2 # Ratio 1:2
        else:
            if abs(price - fibo['38.2']) < abs(price - fibo['50.0']):
                sl_price = fibo['61.8']
            else:
                sl_price = h4['price']
            
            tp_price = price - (sl_price - price) * 2

    # Calcul final des pips pour le bot
    if sl_price:
        sl_pips = int(abs(price - sl_price) * 100000 / 10) # Conversion pips standard
        tp_pips = int(abs(price - tp_price) * 100000 / 10)
    else:
        sl_pips = 30
        tp_pips = 60

    return {
        'type': 'LKL_SCALP_DAYTRADING',
        'sl_pips': max(10, sl_pips),  # Minimum 10 pips pour le scalping
        'tp_pips': max(15, tp_pips),  # Minimum 15 pips pour sortir vite
        'reason': ta['reason']
    }
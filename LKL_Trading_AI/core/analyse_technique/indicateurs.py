# bot/ta_analyzer.py
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import talib
from datetime import datetime

def get_smma(df, period=50):
    """Calcul de la SMMA (Smoothed Moving Average)"""
    # SMMA(N) est équivalent à EMA(2N-1)
    ema_period = 2 * period - 1
    return talib.EMA(df['close'], timeperiod=ema_period)

def get_market_structure(df):
    """Détecte les HH/HL ou LH/LL sur les 50 dernières bougies"""
    highs = df['high'].iloc[-50:].values
    lows = df['low'].iloc[-50:].values
    
    # Simplification : Comparaison des derniers pics/creux
    last_highs = talib.MAX(df['high'], timeperiod=10).iloc[-20:]
    last_lows = talib.MIN(df['low'], timeperiod=10).iloc[-20:]
    
    is_uptrend = (df['close'].iloc[-1] > last_highs.iloc[-5]) and (df['low'].iloc[-1] > last_lows.iloc[-5])
    is_downtrend = (df['close'].iloc[-1] < last_lows.iloc[-5]) and (df['high'].iloc[-1] < last_highs.iloc[-5])
    
    if is_uptrend: return "Bullish (HH/HL)"
    if is_downtrend: return "Bearish (LH/LL)"
    return "Range"

def get_fibonacci_zone(symbol, timeframe, trend):
    """Calcule la Golden Zone de Fibonacci (38.2, 50, 61.8)"""
    # Récupérer l'impulsion (50 bougies)
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)
    if rates is None: return None
    df = pd.DataFrame(rates)
    
    if "Bullish" in trend:
        # Impulsion haussière : du creux au sommet
        low_idx = df['low'].idxmin()
        high_idx = df['high'].idxmax()
        if low_idx < high_idx: # Valide
            start_price = df['low'].min()
            end_price = df['high'].max()
        else:
            return None
    else:
        # Impulsion baissière : du sommet au creux
        high_idx = df['high'].idxmax()
        low_idx = df['low'].idxmin()
        if high_idx < low_idx:
            start_price = df['high'].max()
            end_price = df['low'].min()
        else:
            return None

    diff = abs(start_price - end_price)
    levels = {
        '38.2': end_price - 0.382 * diff if trend == "Bullish" else end_price + 0.382 * diff,
        '50.0': end_price - 0.500 * diff if trend == "Bullish" else end_price + 0.500 * diff,
        '61.8': end_price - 0.618 * diff if trend == "Bullish" else end_price + 0.618 * diff
    }
    return levels

def analyze_technical(symbol: str):
    # 1. Analyse multi-timeframe
    timeframes = {
        'H4': mt5.TIMEFRAME_H4,
        'H1': mt5.TIMEFRAME_H1,
        'M30': mt5.TIMEFRAME_M30,
        'M5': mt5.TIMEFRAME_M5
    }
    
    results = {}
    for tf_name, tf_val in timeframes.items():
        rates = mt5.copy_rates_from_pos(symbol, tf_val, 0, 200)
        if rates is None: continue
        df = pd.DataFrame(rates)
        
        # SMMA 50
        smma = get_smma(df, 50)
        current_smma = smma.iloc[-1]
        price = df['close'].iloc[-1]
        
        # Structure de marché
        structure = get_market_structure(df)
        
        results[tf_name] = {
            'price': price,
            'smma_50': current_smma,
            'pos_to_smma': 'above' if price > current_smma else 'below',
            'structure': structure
        }

    # Tendance mère (H4)
    h4 = results.get('H4')
    if not h4: return None

    # Fibonacci sur H1 (précision du retracement)
    fibo = get_fibonacci_zone(symbol, mt5.TIMEFRAME_H1, h4['structure'])

    # Détection Price Action (M5 pour l'entrée Scalping/Day Trading)
    rates_m5 = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, 50)
    if rates_m5 is not None:
        df_m5 = pd.DataFrame(rates_m5)
    else:
        df_m5 = pd.DataFrame()
    
    # Chandeliers (simplifié)
    signals = []
    # Engulfing
    if not df_m5.empty:
        # Engulfing
        if df_m5['close'].iloc[-1] > df_m5['open'].iloc[-2] and df_m5['close'].iloc[-2] < df_m5['open'].iloc[-2]:
            signals.append("Bullish Engulfing")
        if df_m5['close'].iloc[-1] < df_m5['open'].iloc[-2] and df_m5['close'].iloc[-2] > df_m5['open'].iloc[-2]:
            signals.append("Bearish Engulfing")

    # Action suggérée
    action = None
    reason = []
    
    if h4['pos_to_smma'] == 'above' and "Bullish" in h4['structure']:
        if fibo and h4['price'] <= fibo['38.2'] and h4['price'] >= fibo['61.8']:
            if "Bullish Engulfing" in signals:
                action = 'buy'
                reason = "Trend H4 Bull + SMMA OK + Fibonacci Zone + Price Action confirmation"

    elif h4['pos_to_smma'] == 'below' and "Bearish" in h4['structure']:
        if fibo and h4['price'] >= fibo['38.2'] and h4['price'] <= fibo['61.8']:
            if "Bearish Engulfing" in signals:
                action = 'sell'
                reason = "Trend H4 Bear + SMMA OK + Fibonacci Zone + Price Action confirmation"

    return {
        'action': action,
        'reason': reason,
        'signals': signals,
        'h4': h4,
        'h1': results.get('H1'),
        'fibo': fibo,
        'price': h4['price']
    }

def calculer_volatilite_relative(symbol, current_atr, avg_atr_20):
    """
    Compare l'ATR actuel à sa moyenne historique.
    """
    if avg_atr_20 == 0: return 1.0
    return current_atr / avg_atr_20

def est_volatilite_elevee(vol_rel):
    return vol_rel > 1.5

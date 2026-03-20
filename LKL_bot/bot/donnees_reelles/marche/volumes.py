def analyser_volume_relatif(current_vol, avg_vol):
    """
    Analyse si le volume actuel est supérieur à la normale (indication de force).
    """
    if avg_vol == 0: return 1.0
    return current_vol / avg_vol

def est_volume_anormal(vol_rel):
    return vol_rel > 2.0

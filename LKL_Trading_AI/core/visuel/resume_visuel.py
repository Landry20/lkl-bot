from utils.personnalite import PersonnaliteBot

def generer_resume_fondamental(analyses):
    """
    Génère un résumé textuel ultra-chic et animé pour le Dashboard 🌟✨🚀
    """
    bot = PersonnaliteBot()
    resumes = []
    
    # 🎯 Macro-Économie
    if 'macro' in analyses:
        m = analyses['macro']
        biais = m.get('biais', 'neutre').upper()
        resumes.append(f"🎯 **Macro** : Biais {biais} {bot.humaniser('', 'gentil')} (Confiance: {m.get('confiance', 0)}% 🔥)")
        
    # 🚩 Géo-Politique
    if 'geopolitique' in analyses:
        g = analyses['geopolitique']
        status = '🚨 DANGER' if g.get('risque_global', 0) > 70 else '✅ STABLE'
        resumes.append(f"🚩 **Géo** : Risque {g['risque_global']}% - {status} 🌍🛡️")

    # 🧠 Sentiment (Micro)
    if 'micro' in analyses:
        resumes.append(f"🧠 **Sentiment** : {analyses['micro'].get('explication', 'Neutre')} 🧐📊")

    # 💎 Avis Personnel du Bot
    avis = bot.donner_avis_tranche(analyses.get('macro', {}).get('biais', 'neutre'))
    
    return " | ".join(resumes) + f"\n\n✨ **MON AVIS D'EXPERT** : {avis} 🤝🔥💎"

def preparer_alertes_dashboard(analyses):
    """
    Prépare les alertes critiques avec des emojis percutants 🚨🛑⛈️
    """
    alertes = []
    if 'geopolitique' in analyses and analyses['geopolitique'].get('risque_global', 0) > 85:
        alertes.append("🚨 **ALERTE ROUGE GÉOPOLITIQUE** : Danger immédiat, protégez vos trades ! 🛡️🛑")
    
    return alertes

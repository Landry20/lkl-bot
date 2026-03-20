# bot/main.py
import schedule
import time
import MetaTrader5 as mt5

# === IMPORTS LOCAUX (ARCHITECTURE FRANÇAISE) ===
# Communication
from communication.envoi_backend import send_to_laravel
from communication.reception_backend import get_from_laravel
from communication.notifications import send_notification
from communication.push_python_api import push_analysis_to_dashboard

# Logique Bot
from connexion_mt5 import init, shutdown, get_account_info
from analyse_technique.indicateurs import analyze_technical
from gestion_risque import open_trade, check_breakeven, calculate_lot
from journaux.gestion_logs import log_announcement, log_position, purge_old
from analyse_technique.strategie_utilisateur import get_strategy_v2
from configuration import SYMBOLS, WORKING_DAYS
from visuel.generateur_graphiques import generate_analysis_chart, generate_fundamental_pulse_chart

# Raisonnement & Données Réelles
from raisonnement.analyse_macroeconomique import analyser_macro_complete
from raisonnement.analyse_geopolitique import analyser_geopolitique
from raisonnement.analyse_microeconomique import analyser_micro
from raisonnement.analyse_discours import analyser_discours
from raisonnement.synthese_fondamentale import synthese_fondamentale_complete
from raisonnement.comparateur_paires import comparer_devises_globalement

from donnees_reelles.news_scraper import NewsScraper
from donnees_reelles.geopolitique.actualites import get_geopolitical_news, get_current_hotspots
from donnees_reelles.geopolitique.conflits_en_cours import get_ongoing_conflicts_summary
from donnees_reelles.geopolitique.sanctions_actives import get_active_sanctions
from donnees_reelles.discours.discours_banques_centrales import get_latest_bc_speeches
from donnees_reelles.discours.discours_politiques import get_major_political_events
from donnees_reelles.discours.transcriptions import transcrire_media_recent
from donnees_reelles.marche.donnees_techniques import get_market_sentiment
from donnees_reelles.marche.prix_mt5 import get_current_price
from visuel.resume_visuel import generer_resume_fondamental
from apprentissage.ajustement_scores import charger_poids
from utils.state_manager import StateManager
from utils.personnalite import PersonnaliteBot
from donnees_reelles.marche.catastrophes import get_disaster_alerts, analyser_impact_catastrophe
from apprentissage.meta_apprentissage import MetaCerveau
from visuel.briefing_vocal import generer_briefing_quotidien
from donnees_reelles.marche.sentiment_social import croiser_donnees_v3, get_institutional_bias, get_social_sentiment

# === VARIABLES DE COEUR GLOBALES ===
GLOBAL_CURRENCY_SCORES = {}
bot_state = StateManager()
bot_ego = PersonnaliteBot()


def _sync_announcements_to_laravel(speeches, politique):
    """
    Envoie les événements (discours BC, politique) au backend pour le menu Announce (calendrier).
    Aujourd'hui, demain, semaine — visibles dans les onglets Macro / Géo.
    N'envoie que si la liste des événements a changé (évite doublons).
    """
    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    events_for_hash = []
    res_users = get_from_laravel('bot/users')
    user_id = 1
    if res_users and res_users.get('status') == 'success' and res_users.get('data'):
        user_id = res_users['data'][0].get('id', 1)
    bank_currency = {"FED": "USD", "BCE": "EUR", "BOE": "GBP"}
    to_send = []
    for s in (speeches or []):
        ev = {
            "user_id": user_id,
            "date": s.get("date", today),
            "time": s.get("time"),
            "currency": bank_currency.get(s.get("bank", ""), "USD"),
            "event": s.get("title", s.get("speaker", "Discours BC")),
            "impact": "HIGH",
            "source": s.get("bank"),
            "url": s.get("link")
        }
        events_for_hash.append((ev["date"], ev["event"]))
        to_send.append(ev)
    for p in (politique or []):
        pub = p.get("published", today)
        if isinstance(pub, str) and len(pub) >= 10:
            date = pub[:10]
        else:
            date = today
        ev = {
            "user_id": user_id,
            "date": date,
            "time": None,
            "currency": "GEO",
            "event": p.get("event", p.get("title", "Événement politique")),
            "impact": str(p.get("impact", "MEDIUM")).upper()[:6] or "MEDIUM",
            "source": "CFR",
            "url": p.get("link")
        }
        if ev["impact"] not in ("HIGH", "MEDIUM", "LOW"):
            ev["impact"] = "MEDIUM"
        events_for_hash.append((ev["date"], ev["event"]))
        to_send.append(ev)
    if events_for_hash and bot_state.has_changed("announcements_sync", sorted(events_for_hash)):
        for ev in to_send:
            send_to_laravel("announcements", ev)
        print("[PULSE] Calendrier mis à jour (menu Announce)")


def fundamental_pulse():
    """
    Cœur du projet : Analyse tous les dossiers et envoie les informations structurées au front-end.
    Chaque partie (Macro, Géo, Micro, Discours) est traitée ici.
    """
    print("\n" + "="*50)
    print("🌍 LKL FUNDAMENTAL PULSE - DÉMARRAGE DU RAISONNEMENT TOTAL")
    print("="*50)

    # 1. Données Réelles De Profondeur (Deep Intelligence)
    hotspots = get_current_hotspots()
    conflits = get_ongoing_conflicts_summary() # Nouveau: Scrape CrisisGroup
    politique = get_major_political_events() # Nouveau: Scrape CFR/IFES
    sanctions = get_active_sanctions()
    market_sentiment = get_market_sentiment()
    speeches = get_latest_bc_speeches()
    
    # Prix pour détection de divergence
    price_now = get_current_price("EURUSD")
    price_prev = price_now * 0.998 if price_now else None # Mock de la variation précédente pour l'exemple
    
    # 2. Raisonnement Par Modules
    analyses_results = {}
    
    # Macro
    analyses_results['macro'] = analyser_macro_complete("EURUSD", {"USD_CPI": 3.1, "EUR_CPI": 2.8})
    
    # Géo (Enrichi avec conflits réels)
    geo_eval = analyser_geopolitique("EURUSD")
    analyses_results['geopolitique'] = {
        'risque_global': geo_eval['risque_global'],
        'biais': geo_eval['biais'],
        'explications': [c['name'] for c in conflits[:3]] + geo_eval['explications'],
        'hotspots': hotspots,
        'sanctions': sanctions
    }

    # Discours (Enrichi avec transcriptions/audio structure)
    current_speech = speeches[0] if speeches else None
    if current_speech:
        # Le bot "comprend" le discours via transcription si disponible
        speech_text = transcrire_media_recent(current_speech.get('link', "")) or current_speech['title']
        speech_analysis = analyser_discours(current_speech['bank'], [speech_text])
        analyses_results['discours'] = {
            'bias': 'bullish' if speech_analysis['ton'] == 'hawkish' else 'bearish' if speech_analysis['ton'] == 'dovish' else 'neutre',
            'content': f"{current_speech['bank']} {current_speech['speaker']}: {speech_text[:60]}...",
            'details': speech_analysis
        }

    # 3. Synthèse Totale & État Réactif
    print("[PULSE] Synthèse Finale & Détection de Changement...")
    synthese = synthese_fondamentale_complete("EURUSD", analyses_results, price_now, price_prev)
    
    # ANTI-RÉPÉTITION : On ne broadcast que si la donnée a RELLEMENT changé
    # On crée un pack de données "visibles" pour le hash
    visible_state = {
        'bias': synthese['biais_final'],
        'confidence': synthese['confiance'],
        'divergence': synthese['divergence'],
        'explanations': synthese['explications'][:2],
        'first_conflict': conflits[0]['name'] if conflits else None
    }
    
    if bot_state.has_changed('fundamental_pulse', visible_state):
        print("[PULSE] 🚀 NOUVELLE INTELLIGENCE DÉTECTÉE - Envoi au Dashboard")
        payload = {
            'category': 'synthese',
            'symbol': 'EURUSD',
            'bias': synthese['biais_final'],
            'confidence': synthese['confiance'],
            'content': f"{bot_ego.humaniser('Intelligence Temporelle : ' + synthese['divergence'])} \n {generer_resume_fondamental(analyses_results)}",
            'details': {
                'explications': synthese['explications'],
                'divergence': synthese['divergence'],
                'conflits_actifs': conflits,
                'politique': politique
            },
            'impact_level': 'high'
        }
        send_to_laravel('bot/fundamental', payload)
        # Impact élevé → notification à tous les utilisateurs
        res = get_from_laravel('bot/users')
        if res and res.get('status') == 'success':
            users = res.get('data', [])
            short_content = f"🌍 Pulse: {synthese['biais_final'].upper()} ({synthese['confiance']}%). {synthese['divergence'][:80]}..."
            for u in users:
                send_notification(u.get('id'), "info", short_content)
    else:
        print("[PULSE] 💤 Aucune nouveauté significative détectée. Silence radio (Anti-répétition).")

    # Synchroniser le calendrier (annonces) : discours BC + événements politiques → menu Announce
    _sync_announcements_to_laravel(speeches, politique)

    # 4. Comparaison et Pulse Visuel
    devises = {"USD": 40, "EUR": -20, "GBP": 10, "JPY": -40, "AUD": 30} # Exemples
    # ... on peut aussi hasher le pulse visuel si besoin ...
    
    pulse_img_path = "../lkl_web/public/charts/fundamental_pulse.png"
    generate_fundamental_pulse_chart(devises, pulse_img_path)
    
    return devises

# === CYCLE DE TRADING PAR UTILISATEUR ===
def process_user(user):
    user_id = user['id']
    username = user['name']
    
    # === CHECK CATASTROPHES NATURELLES ===
    alerts = get_disaster_alerts()
    for alert in alerts:
        if bot_state.has_changed(f"alert_{alert['asset']}", alert['title']):
            print(f"[DISASTER] 🚨 {alert['title']}")
            raison = analyser_impact_catastrophe(alert)
            send_notification(1, "warning", f"{alert['title']}\n\n{raison}")

    # === CHECK SENTIMENT V3 (SOCIAL & COT) ===
    # On simule pour les paires majeures
    sentiment_report = croiser_donnees_v3("EURUSD")
    if bot_state.has_changed("sentiment_v3", sentiment_report):
        print(f"[V3] 🛰️ {sentiment_report}")
        send_notification(user_id, "info", f"✨ **PULSE V3 : Sentiment & Banques** ✨\n\n{sentiment_report}")

    # === BRIEFING QUOTIDIEN V3 ===
    if bot_state.has_changed("daily_briefing", "done_today"):
        meta = MetaCerveau()
        social = get_social_sentiment("EURUSD")
        inst = get_institutional_bias("EURUSD")
        briefing = generer_briefing_quotidien(username, meta.poids_actuels, {**social, **inst})
        send_notification(user_id, "success", briefing)
        print(f"[V3] 🎙️ Briefing envoyé à {username}")

    # === PULSE FONDAMENTAL ===
    send_notification(user_id, "info", bot_ego.saluer(username), is_silent=True)

    # === ACTIVATION PERSONNALISÉE ===
    if bot_state.has_changed('bot_activation', True):
        msg = bot_ego.activation_message(username)
        send_notification(user_id, "success", msg)
        print(f"[ACTIVATE] Animation de bienvenue envoyée pour {username}!")

    # === LOG DE DÉBOGAGE CONNEXION ===
    masked_pass = "*" * len(user['mt5_password']) if user['mt5_password'] else "NONE"
    print(f"[DEBUG] Tentative MT5 pour {username} (ID: {user_id})")
    print(f"        Login: {user['mt5_login']} | Server: {user['mt5_server']} | Pass: {masked_pass}")

    # Connexion spécifique au compte MT5 de l'utilisateur
    success, error_msg = init(login=user['mt5_login'], password=user['mt5_password'], server=user['mt5_server'])
    if not success:
        print(f"[ERROR] {error_msg}")
        send_notification(user_id, "error", f"❌ Échec Connexion MT5: {error_msg}. Vérifiez vos accès.")
        return

    # === SYNC STATS ===
    try:
        info = get_account_info()
        if info:
            send_to_laravel('bot/sync', {
                'user_id': user_id,
                'mt5_name': info['name'],
                'balance': info['balance'],
                'equity': info['equity'],
                'today_profit': info['daily_profit'],
                'active_deals': mt5.positions_total()
            })
    except Exception as e:
        err = f"Erreur Sync Stats pour {username}: {str(e)}"
        print(f"[ERROR] {err}")
        send_notification(user_id, "error", f"🚨 Erreur Sync Dashboard: {str(e)}")

    trades_today = 0
    symbols_scanned = 0

    # === ANALYSE PAR SYMBOLE ===
    for name, symbol in SYMBOLS.items():
        try:
            # 1. Analyse Fondamentale de Précision
            dataset = {"USD_CPI": 3.4, "EUR_CPI": 2.9} # Exemple, à lier à un flux réel plus tard
            fonda_res = analyser_macro_complete(symbol, dataset)
            biais_fonda = fonda_res['biais']
            
            # ANTI-RÉPÉTITION pour les notifications de symboles
            signal_state = {'symbol': symbol, 'biais': biais_fonda, 'confiance': fonda_res['confiance']}
            if bot_state.has_changed(f"fonda_{user_id}_{symbol}", signal_state):
                msg_fonda = f"🔍 {symbol}: Biais {biais_fonda.upper()} ({fonda_res['confiance']}%). {fonda_res['conclusion']}"
                send_notification(user_id, "info", msg_fonda, is_silent=True)

            # 2. Analyse technique avancée
            ta = analyze_technical(symbol)
            if not ta: continue
            
            # Vérification de l'alignement Fondamental vs Technique
            action = ta['action']
            if action and action != 'none':
                if action == 'buy' and biais_fonda == 'bearish':
                    print(f"[REJECT] {symbol} BUY rejeté par biais Fondamental Bearish")
                    send_notification(user_id, "info", f"🚫 SIGNAL REJETÉ: Achat {symbol} bloqué par biais Fondamental Bearish.")
                    continue
                if action == 'sell' and biais_fonda == 'bullish':
                    print(f"[REJECT] {symbol} SELL rejeté par biais Fondamental Bullish")
                    send_notification(user_id, "info", f"🚫 SIGNAL REJETÉ: Vente {symbol} bloqué par biais Fondamental Bullish.")
                    continue

            chart_path = f"charts/{user_id}_{symbol}_analysis.png"
            generate_analysis_chart(symbol, [{'close': ta['price']} for _ in range(20)], ta, f"../lkl_web/public/{chart_path}")
            ta['chart_url'] = f"/{chart_path}"
            
            # 3. Demande de confirmation à Laravel
            check_data = {
                'user_id': user_id,
                'symbol': symbol,
                'trend': ta['h4']['structure'],
                'action': ta['action'] if ta['action'] else 'none',
                'timeframe': 'M5',
                'fibo_zone': ta.get('fibo_zone'),
                'smma_50_pos': ta['h4']['pos_to_smma'],
                'image_url': ta.get('chart_url'),
                'details': f"Fonda: {biais_fonda}, TA: {ta['h4']['pos_to_smma']}, Fibo: {ta['fibo']}"
            }
            
            confirmation = send_to_laravel('analyses/check', check_data)
            # Envoyer l’analyse au dashboard Python (menu Fonda / Analyses) pour affichage immédiat
            push_analysis_to_dashboard(
                symbol,
                ta.get('action') or 'none',
                ta['h4'].get('structure', 'neutral'),
                ta.get('fibo_zone') or '',
                confirmation.get('count', 0) if confirmation else 0,
                [],
                image_url=ta.get('chart_url'),
                details=check_data.get('details', '')
            )

            if action:
                send_notification(user_id, "analysis", f"Analyse {symbol}: Zone {ta.get('fibo_zone')}. Confirmation: {confirmation.get('count',0)}/2", is_silent=True)

            if not confirmation or not confirmation.get('confirmed'):
                symbols_scanned += 1
                continue

            # 4. Vérification de l'autorisation de TRADING (Nouveau)
            if not user.get('trading_authorized'):
                print(f"[AUTH] Trading non autorisé pour {username} sur {symbol}. Signal enregistré mais non exécuté.")
                send_notification(user_id, "warning", f"⚠️ Signal {symbol} {action.upper()} détecté mais NON EXÉCUTÉ (Autorisation 'Trader' requise).")
                continue

            print(f"[SIGNAL] {symbol}: CONFIRMÉ pour {username}!")

            # 5. Stratégie et Lot
            strategy = get_strategy_v2(symbol, ta)
            if not strategy: continue
                
            sl_pips = strategy['sl_pips']
            tp_pips = strategy['tp_pips']
            lot = calculate_lot(symbol, sl_pips)

            # 6. Exécution
            result = open_trade(user_id, symbol, action, ta)
            
            if result:
                print(f"[TRADE] EXÉCUTÉ pour {username}: {symbol} {action.upper()}")
                send_notification(user_id, "trade", f"✅ Trade EXÉCUTÉ: {action.upper()} {symbol} @ {ta['price']}")

                trade_data = {
                    'user_id': user_id,
                    'symbol': symbol,
                    'type': action,
                    'entry_price': ta['price'],
                    'sl': ta['price'] - 50 * mt5.symbol_info(symbol).point if action == 'buy' else ta['price'] + 50 * mt5.symbol_info(symbol).point,
                    'tp': ta['price'] + 100 * mt5.symbol_info(symbol).point if action == 'buy' else ta['price'] - 100 * mt5.symbol_info(symbol).point,
                    'lot': lot,
                    'reason': ta.get('reason', 'Signal Confirmé'),
                    'mt5_order_id': str(result.order)
                }
                send_to_laravel('trades', trade_data)
                trades_today += 1

        except Exception as e:
            err_msg = f"Erreur critique sur {symbol}: {str(e)}"
            print(f"[SYMBOL ERROR] {err_msg}")
            
        symbols_scanned += 1

    send_notification(user_id, "info", f"✅ Cycle terminé pour {username}. {symbols_scanned} symboles analysés. {trades_today} positions ouvertes.", is_silent=True)
    
    check_breakeven()
    shutdown()

# === CYCLE GLOBAL ===
def trading_cycle():
    # 0. Récupération des réglages globaux (GET)
    settings = get_from_laravel('settings')
    if not settings or settings.get('bot_running') != '1':
        return

    # === RAISONNEMENT TOTAL (PULSE) ===
    global GLOBAL_CURRENCY_SCORES
    GLOBAL_CURRENCY_SCORES = fundamental_pulse()

    # 1. Récupération des utilisateurs MT5 (GET)
    res = get_from_laravel('bot/users')
    if not res or res.get('status') != 'success':
        print("[BOT] Erreur récupération utilisateurs")
        return

    users = res.get('data', [])
    for user in users:
        process_user(user)

# === PLANIFICATION ===
schedule.every(2).minutes.do(trading_cycle)

if __name__ == "__main__":
    print("=== LKL BOT MULTI-USER DÉMARRÉ (COMMUNICATION SPLIT) ===")
    trading_cycle()
    while True:
        schedule.run_pending()
        time.sleep(1)

"""
GESTION DES LOGS
Rotation et écriture dans les fichiers journaux.
"""
import logging
import os
from datetime import datetime

# Chemins des logs
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
DECISIONS_LOG = os.path.join(LOG_DIR, 'decisions.log')
ERREURS_LOG = os.path.join(LOG_DIR, 'erreurs.log')
ACTIVITE_LOG = os.path.join(LOG_DIR, 'activite.log')

# Configuration
def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.FileHandler(log_file, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Loggers
logger_decisions = setup_logger('Decisions', DECISIONS_LOG)
logger_erreurs = setup_logger('Erreurs', ERREURS_LOG, logging.ERROR)
logger_activite = setup_logger('Activite', ACTIVITE_LOG)

def log_decision(message):
    logger_decisions.info(message)
    print(f"[DECISION] {message}")

def log_error(message):
    logger_erreurs.error(message)
    print(f"[ERREUR] {message}")

def log_activite(message):
    logger_activite.info(message)
    # print(f"[ACTIVITE] {message}") # Optionnel pour ne pas polluer la console

# Fonctions de compatibilité avec l'ancien code (à migrer progressivement)
def log_announcement(a_type, currency, event, impact, dt):
    msg = f"ANNONCE: {a_type} | {currency} | {event} | {impact} | {dt}"
    log_activite(msg)

def log_position(symbol, ot, lot, entry, sl, tp, reason):
    msg = f"POSITION: {ot} {symbol} | Lot: {lot} | @ {entry} | SL: {sl} | TP: {tp} | Reason: {reason}"
    log_decisions(msg) # C'est une décision de trading

def purge_old():
    # Simplifié : Rotation logs ou archivage (à implémenter si besoin)
    pass
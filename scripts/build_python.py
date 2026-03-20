import PyInstaller.__main__
import os
import shutil

# Définition des chemins
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DIST_DIR = os.path.join(BASE_DIR, 'dist')
WORK_DIR = os.path.join(BASE_DIR, 'build')
BINARY_NAME = 'lkl_engine'

# Nettoyage
if os.path.exists(DIST_DIR): shutil.rmtree(DIST_DIR)
if os.path.exists(WORK_DIR): shutil.rmtree(WORK_DIR)

# Lancement de PyInstaller
PyInstaller.__main__.run([
    'LKL_Trading_AI/main.py',                  # Script principal
    '--name=%s' % BINARY_NAME,                 # Nom de l'exécutable
    '--onefile',                               # Un seul fichier .exe
    '--console',                               # Garder la console pour le debug (mettre --noconsole pour prod)
    '--clean',
    '--distpath=%s' % DIST_DIR,
    '--workpath=%s' % WORK_DIR,
    '--specpath=%s' % BASE_DIR,
    # Inclusions de données
    '--add-data=LKL_Trading_AI/data;data',     
    # Import cachés souvent manqués par PyInstaller
    '--hidden-import=talib',
    '--hidden-import=MetaTrader5',
    '--hidden-import=sqlite3',
    '--hidden-import=pandas',
    '--hidden-import=numpy',
])

print(f"[BUILD SUCCESS] Binaire généré dans {DIST_DIR}/{BINARY_NAME}.exe")

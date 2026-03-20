# 🛠️ Guide d'Installation - LKL Trading AI Desktop

Ce projet nécessite quelques outils système pour compiler l'interface native (Tauri) et le moteur de trading. Suivez ces étapes dans l'ordre.

## 1. Installation de Rust (Le plus important)
Tauri est construit en Rust. C'est lui qui crée l'exécutable (`.exe`) et l'installeur (`.msi`).

1. **Téléchargez l'installateur** : [rustup-init.exe](https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe)
2. **Installation des outils de build C++** : 
   - Lors de l'installation de Rust, il vous demandera d'installer les "Visual Studio Build Tools".
   - Si vous ne les avez pas, téléchargez [Visual Studio Community 2022](https://visualstudio.microsoft.com/fr/downloads/).
   - Dans l'installateur Visual Studio, cochez **"Développement Desktop en C++"** (Desktop development with C++).
   - Redémarrez votre ordinateur après l'installation.
3. **Vérification** : Ouvrez un terminal et tapez :
   ```bash
   cargo --version
   ```
   *Si vous voyez un numéro de version, Rust est prêt.*

## 2. Installation de Node.js (Pour l'interface React)
1. **Téléchargez Node.js** : [LTS Version (Recommandé)](https://nodejs.org/)
2. **Vérification** :
   ```bash
   node -v
   npm -v
   ```

3. **Préparer le projet (Réinstallation des dépendances)**

Une fois les outils installés, ouvrez un terminal dans le dossier du projet :

1. **Installer les dépendances Frontend** :
   ```bash
   cd lkl_web
   npm install
   ```

2. **Configurer le moteur Python** :
   ```bash
   # À la racine du projet
   python -m venv .venv
   .venv\Scripts\activate
   pip install MetaTrader5 schedule requests pymysql TA-Lib pandas matplotlib
   ```

3. **Générer le moteur Python (Moi, Antigravity, j'ai déjà fait cette étape pour vous)** :
   ```bash
   # (Optionnel si vous changez le code Python)
   python scripts/build_python.py
   ```

## 4. Lancer ou Compiler l'application

### Mode Développement (Pour tester)
Cela lance l'application dans une fenêtre native avec rechargement automatique :
```bash
cd lkl_web
npm run tauri dev
```

### Mode Production (Générer l'Installeur .exe)
Cela crée un fichier d'installation propre dans `lkl_web/src-tauri/target/release/bundle/msi/` :
```bash
cd lkl_web
npm run tauri build
```

---
> [!IMPORTANT]
> MetaTrader 5 doit être installé sur votre machine pour que le bot puisse se connecter.

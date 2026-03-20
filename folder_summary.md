# Résumé des Fonctionnalités par Dossier - LKL Bot

Ce document détaille le rôle et les fonctionnalités de chaque dossier du projet **LKL Bot**, un système de trading automatisé "Fundamental First".

---

## 📂 `lkl_backend` (Laravel PHP)
**Rôle :** Le "cerveau" administratif et la base de données centrale.
- **Gestion des Utilisateurs :** Inscription, authentification et gestion des permissions.
- **Stockage des Données :** Base de données pour les comptes de trading (Logins MT5), les statistiques de performance et les configurations du bot.
- **News Engine :** Récupération et stockage des annonces économiques cruciales.
- **Canaux Temps Réel :** Utilisation de WebSockets (via Pusher/Laravel Echo) pour envoyer instantanément les mises à jour du bot vers l'interface utilisateur.
- **API REST :** Fournit les points de terminaison (`Endpoints`) pour que la partie Python et l'interface Web puissent communiquer.

---

## 📂 `lkl_web` (React + Vite + Tauri)
**Rôle :** L'interface utilisateur (GUI) pour PC.
- **Dashboard :** Visualisation en temps réel du Capital, de l'Équité et des transactions en cours.
- **Contrôle du Bot :** Boutons pour démarrer/arrêter le bot et configurer les paramètres de risque.
- **Analyse Fondamentale :** Affichage des actualités économiques et du sentiment de marché calculé.
- **Tauri Integration :** Permet de transformer une application web en une application native Windows (`.exe`), offrant une expérience fluide et sécurisée.

---

## 📂 `LKL_Trading_AI` (Python)
**Rôle :** Le moteur d'exécution et d'intelligence.
- **`core/` :** Contient la logique métier, notamment :
  - `fundamental_bias.py` : Analyseur de sentiment basé sur l'IA/Keywords pour déterminer si une monnaie est Haussière ou Baissière.
  - `ta_analyzer.py` : Analyseur technique (RSI, MACD, SMMA) pour confirmer les entrées de trade.
  - `risk_manager.py` : Calcule la taille des lots et gère les Stop Loss / Take Profit.
- **`main.py` :** La boucle principale du bot qui synchronise les actions entre MT5 et le backend.
- **`mt5_connector.py` :** Interface de communication directe avec la plateforme MetaTrader 5.

---

## 📂 `LKL_bot`
**Rôle :** Version de distribution ou héritée.
- Contient une version consolidée du moteur et de l'interface, souvent utilisée pour des tests rapides ou des déploiements pré-configurés.

---

## 📂 `scripts`
**Rôle :** Outils d'automatisation.
- **`build_python.py` :** Compile le code Python en un exécutable autonome pour qu'il soit intégré dans l'application finale sans nécessiter l'installation de Python sur chaque machine.

---

## 📂 `data`, `build`, `dist`
- **`data/` :** Stockage local des logs, des états du bot et des fichiers temporaires.
- **`build/` & `dist/` :** Dossiers générés automatiquement lors de la compilation de l'interface et du moteur.

---

## 📂 `.venv`
- **Rôle :** Environnement Python isolé contenant toutes les bibliothèques nécessaires (MetaTrader5, Pandas, TA-Lib, etc.), garantissant que le bot fonctionne de la même manière sur tous les ordinateurs.

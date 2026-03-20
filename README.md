# 🤖 LKL Bot - Fundamental First Trading AI

LKL Bot est un système de trading automatisé sophistiqué qui combine l'analyse fondamentale en temps réel avec des indicateurs techniques avancés pour exécuter des décisions de trading intelligentes sur MetaTrader 5.

## 🌟 Points Forts

- **Stratégie "Fundamental First"** : Contrairement aux bots classiques, LKL Bot analyse d'abord le sentiment économique global via NewsAPI avant de valider une opération techniquement.
- **Multi-Utilisateurs** : Architecture conçue pour gérer plusieurs comptes de trading simultanément avec isolation complète.
- **Interface Desktop Moderne** : Interface fluide construite avec React et Tauri, offrant une expérience native sous Windows.
- **Synchronisation Temps Réel** : Monitoring en direct de vos performances (Balance, Équité, Profits) via WebSockets.
- **Gestion du Risque Intégrée** : Calcul automatique des lots, Stop Loss et Take Profit pour protéger votre capital.

## 🏗️ Architecture

Le projet est divisé en trois composants principaux :

1.  **Backend (Laravel)** : Gère les données, les utilisateurs et la communication temps réel.
2.  **Frontend (React/Tauri)** : L'application PC pour piloter le bot.
3.  **AI Engine (Python)** : Le moteur de trading qui analyse les marchés et exécute les ordres sur MT5.

## 🚀 Installation Rapide

Pour installer le projet sur votre PC de développement :

1.  **Prérequis** :
    - [Rust & C++ Build Tools](https://www.rust-lang.org/)
    - [Node.js](https://nodejs.org/)
    - [Python 3.10+](https://www.python.org/)
    - MetaTrader 5 installé.

2.  **Configuration** :
    - Clonez le dépôt : `git clone https://github.com/Landry20/lkl-bot.git`
    - Installez les dépendances web : `cd lkl_web && npm install`
    - Configurez le backend Laravel : `cd lkl_backend && composer install && cp .env.example .env && php artisan key:generate`

3.  **Lancement** :
    - Lancez le backend : `php artisan serve`
    - Lancez l'interface : `cd lkl_web && npm run tauri dev`

*Pour un guide détaillé, consultez [INSTALL_DESKTOP.md](./INSTALL_DESKTOP.md).*

## 🛠️ Technologies Utilisées

- **Frontend** : React, Vite, Tauri, Tailwind CSS.
- **Backend** : PHP Laravel, MySQL, Pusher.
- **Trading AI** : Python, MetaTrader5 API, TA-Lib, NewsAPI.

---
Développé avec ❤️ pour des performances de trading optimales.

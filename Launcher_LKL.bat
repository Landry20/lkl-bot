@echo off
TITLE LKL Bot Ecosystem Launcher
COLOR 0B

echo =========================================================
echo             LKL BOT - GLOBAL LAUNCHER
echo =========================================================
echo.

echo [1/5] Demarrage du Backend Laravel...
start "LKL BACKEND" cmd /k "cd lkl_backend && php artisan serve"

echo [2/5] Demarrage du Temps Reel (WebSockets)...
start "LKL WEBSOCKETS" cmd /k "cd lkl_backend && php artisan reverb:start"

echo [3/5] Demarrage du Backend Python FastAPI...
start "LKL PYTHON API" cmd /k "cd LKL_bot\api_server && ..\venv\Scripts\activate && python start_server.py"

echo [4/5] Demarrage du Frontend React (Port 3000)...
start "LKL FRONTEND" cmd /k "cd lkl_web && npm run dev"

echo [5/5] Demarrage du Trading Bot (Python)...
start "LKL TRADING BOT" cmd /k "cd LKL_bot && venv\Scripts\activate && python bot/main.py"

echo.
echo =========================================================
echo   TOUS LES SYSTEMES SONT OPERATIONNELS SUR :
echo   - Backend Laravel : http://127.0.0.1:8000
echo   - Backend Python  : http://127.0.0.1:8001
echo   - Temps Reel      : Port 8080 (Actif)
echo   - Frontend        : http://localhost:3000
echo =========================================================
echo.
pause

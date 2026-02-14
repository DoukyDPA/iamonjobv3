@echo off
echo ================================
echo   IAMonJob - Demarrage rapide
echo ================================
echo.

cd backend

echo Installation des dependances...
pip install -r requirements.txt
echo.

echo Demarrage du serveur backend...
echo Le serveur sera accessible sur http://localhost:5000
echo.
echo Ouvrez ensuite frontend/index.html dans votre navigateur
echo.

python app.py

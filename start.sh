#!/bin/bash

echo "================================"
echo "  IAMonJob - Démarrage rapide"
echo "================================"
echo ""

cd backend

echo "Installation des dépendances..."
pip3 install -r requirements.txt
echo ""

echo "Démarrage du serveur backend..."
echo "Le serveur sera accessible sur http://localhost:5000"
echo ""
echo "Ouvrez ensuite frontend/index.html dans votre navigateur"
echo ""

python3 app.py

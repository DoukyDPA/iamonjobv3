# IAMonJob V3 - Application Web d'Analyse de CV

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](CHANGELOG.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Application web moderne pour l'analyse professionnelle de CV** avec Intelligence Artificielle (Claude API).

> 💡 **Note** : Cette V3 est une application web complète, différente des versions précédentes d'IAMonJob.

![IAMonJob V3 Screenshot](https://via.placeholder.com/800x400/667eea/ffffff?text=IAMonJob+V3+Interface)

---

---

## 📑 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Modules disponibles](#-modules-disponibles)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Utilisation](#-utilisation)
- [Architecture](#-architecture)
- [Sécurité](#-sécurité)
- [Déploiement](#-déploiement-en-production)
- [API Endpoints](#-api-endpoints)
- [Conseils](#-conseils)
- [Contribution](#-contribution)
- [Dépannage](#-dépannage)
- [License](#-license)

---

## 🎯 Fonctionnalités

- ✅ Upload de CV (PDF, Word, TXT, Images)
- ✅ Upload optionnel d'offre d'emploi
- ✅ Analyse complète ou personnalisée (11 modules disponibles)
- ✅ Interface moderne et responsive
- ✅ Résultats détaillés générés par Claude AI

## 📋 Modules disponibles

### Modules CV seul (sans offre d'emploi)
1. **Analyse du CV** - Analyse complète avec forces et faiblesses
2. **Tableau des compétences** - Matrices hard skills et soft skills
3. **Notation et améliorations** - Note /10 et plan d'amélioration
4. **Évolutions professionnelles** - Pistes de reconversion et évolution

### Modules CV + Offre d'emploi
5. **Gap Analysis** - Écarts CV vs poste ciblé
6. **Optimisation ATS** - Mots-clés et compatibilité ATS
7. **Lettre de motivation** - Draft personnalisé
8. **Pitch "Parlez-moi de vous"** - Versions 30s, 2-3min, 5min
9. **Dans la tête du recruteur** - Récit narratif du recruteur
10. **Questions d'entretien** - 12 questions types avec réponses
11. **Veille entreprise** - Fiche sur l'entreprise cible

## 🚀 Installation

### Prérequis

- Python 3.8+
- Node.js (optionnel, pour servir le frontend)
- Clé API Claude (Anthropic)

### Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Le serveur démarre sur `http://localhost:5000`

### Frontend

Option 1 : Serveur simple Python
```bash
cd frontend
python -m http.server 8000
```

Option 2 : Ouvrir directement `index.html` dans le navigateur

L'application sera accessible sur `http://localhost:8000`

## 🔑 Configuration

### Obtenir une clé API Claude

1. Créez un compte sur [console.anthropic.com](https://console.anthropic.com/)
2. Générez une clé API
3. Entrez la clé dans l'interface web (elle commence par `sk-ant-...`)

### Variables d'environnement (optionnel)

Créez un fichier `.env` dans le dossier `backend/` :

```env
ANTHROPIC_API_KEY=sk-ant-...
PORT=5000
```

## 📖 Utilisation

1. **Ouvrez l'application** dans votre navigateur
2. **Entrez votre clé API** Claude
3. **Uploadez votre CV** (obligatoire)
4. **Uploadez l'offre d'emploi** (optionnel)
5. **Choisissez le type d'analyse** :
   - Dossier complet (tous les modules disponibles)
   - Modules personnalisés (sélection manuelle)
6. **Cliquez sur "Générer l'analyse"**
7. **Attendez 30-60 secondes** pour les résultats

## 🏗️ Architecture

```
iamonjob_app/
├── backend/
│   ├── app.py              # Serveur Flask + API endpoints
│   ├── requirements.txt    # Dépendances Python
│   ├── uploads/           # Dossier temporaire des fichiers uploadés
│   └── outputs/           # Dossier des PDF générés
├── frontend/
│   └── index.html         # Interface utilisateur
└── README.md
```

## 🔒 Sécurité

- Les fichiers uploadés sont stockés temporairement et supprimés après analyse
- La clé API est envoyée uniquement via HTTPS (en production)
- Aucune donnée n'est stockée après l'analyse
- Utilisez CORS en production avec des origines spécifiques

## 🌐 Déploiement en Production

### Backend (Heroku, Railway, etc.)

```bash
# Installer gunicorn
pip install gunicorn

# Créer un Procfile
echo "web: gunicorn app:app" > Procfile

# Déployer
git push heroku main
```

### Frontend (Netlify, Vercel, etc.)

1. Modifier `API_URL` dans `index.html` avec l'URL de production
2. Déployer le dossier `frontend/`

## 📊 API Endpoints

### `GET /api/health`
Health check

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2025-02-14T10:30:00"
}
```

### `POST /api/analyze`
Analyser un CV

**Form Data:**
- `api_key`: Clé API Claude
- `cv`: Fichier CV (required)
- `job_offer`: Fichier offre d'emploi (optional)
- `analysis_type`: "complete" ou "custom"
- `modules`: Liste des modules (si custom)

**Response:**
```json
{
  "success": true,
  "analysis": "...",
  "timestamp": "2025-02-14T10:30:00",
  "modules_generated": "all",
  "job_offer_included": true
}
```

### `GET /api/modules`
Liste des modules disponibles

**Response:**
```json
{
  "cv_only": [...],
  "cv_and_offer": [...]
}
```

## 💡 Conseils

- **Formats de CV recommandés** : PDF ou DOCX pour de meilleurs résultats
- **Qualité des images** : Si vous uploadez une photo de CV, assurez-vous qu'elle soit nette
- **Offre d'emploi** : Plus l'offre est détaillée, plus l'analyse sera précise
- **Temps d'attente** : L'analyse complète prend 30-60 secondes

## 🐛 Dépannage

### Erreur CORS
Si vous avez des erreurs CORS, assurez-vous que le backend tourne sur `localhost:5000`

### Erreur API
Vérifiez que votre clé API est valide et que vous avez des crédits

### Fichier trop volumineux
La limite est de 5 MB par fichier (configuré dans Flask)

## 📝 License

MIT License

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📧 Support

Pour toute question, consultez :
- 📖 [Documentation complète](GUIDE.md)
- 🐛 [Signaler un bug](https://github.com/VOTRE-USERNAME/iamonjobv3/issues/new?template=bug_report.md)
- 💡 [Demander une fonctionnalité](https://github.com/VOTRE-USERNAME/iamonjobv3/issues/new?template=feature_request.md)
- 💬 [Discussions GitHub](https://github.com/VOTRE-USERNAME/iamonjobv3/discussions)

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour :
- 🔀 Comment créer une Pull Request
- 📝 Standards de code
- 🧪 Guide de tests
- 📋 Code de conduite

## 📝 License

MIT License - voir [LICENSE](LICENSE) pour plus de détails.

## 🌟 Remerciements

- [Anthropic](https://www.anthropic.com) pour l'API Claude
- [Flask](https://flask.palletsprojects.com/) pour le framework backend
- Tous les contributeurs qui ont participé au projet

## 📊 Statistiques

![GitHub stars](https://img.shields.io/github/stars/VOTRE-USERNAME/iamonjobv3?style=social)
![GitHub forks](https://img.shields.io/github/forks/VOTRE-USERNAME/iamonjobv3?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/VOTRE-USERNAME/iamonjobv3?style=social)

---

<p align="center">
  Fait avec ❤️ pour aider les demandeurs d'emploi
</p>


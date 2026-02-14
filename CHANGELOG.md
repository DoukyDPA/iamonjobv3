# Changelog

Tous les changements notables de ce projet seront documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### À venir
- Export PDF des analyses (génération complète via script Python)
- Support multilingue (EN, ES, DE)
- Mode sombre pour l'interface
- Sauvegarde des analyses dans le navigateur
- Intégration avec d'autres APIs d'IA

## [3.0.0] - 2025-02-14

### 🎉 Version initiale - IAMonJob V3

Application web complète pour l'analyse de CV par IA.

### ✨ Fonctionnalités principales
- **Interface web moderne** avec design gradient violet/rose
- **Upload drag & drop** pour CV et offres d'emploi
- **Support multi-formats** : PDF, DOCX, TXT, images (PNG, JPG)
- **11 modules d'analyse** IAMonJob
- **API REST Flask** complète et documentée
- **Affichage temps réel** des résultats d'analyse
- **Responsive design** (mobile, tablette, desktop)

### 🔧 Technique
- Backend Flask 3.0 (Python 3.8+)
- Intégration API Claude (Anthropic SDK 0.39.0)
- Frontend HTML5/CSS3/JavaScript vanilla
- Docker & docker-compose ready
- CI/CD avec GitHub Actions

### 📦 Modules d'analyse
**CV seul (4 modules)** :
1. Analyse du CV
2. Tableau des compétences
3. Notation et améliorations
4. Évolutions professionnelles

**CV + Offre (7 modules supplémentaires)** :
5. Gap Analysis
6. Optimisation ATS
7. Lettre de motivation
8. Pitch "Parlez-moi de vous"
9. Dans la tête du recruteur
10. Questions d'entretien
11. Veille entreprise

### 🔐 Sécurité
- Validation stricte des fichiers uploadés
- Suppression automatique après analyse
- Support CORS configurable
- Variables d'environnement pour secrets
- Rate limiting prêt pour production

### 📖 Documentation
- README complet avec guide d'installation
- Guide d'utilisation visuel (GUIDE.md)
- Templates GitHub (Issues, PRs)
- Code de conduite et guide de contribution
- Tests unitaires avec pytest

---

## 💡 À propos des versions

Cette application (V3) est une **nouvelle application web** distincte des versions précédentes d'IAMonJob qui étaient basées sur une architecture différente.

### Ajouté
- 🎉 Version initiale de l'application
- ✨ Interface web moderne et responsive
- 📤 Upload de CV (PDF, Word, TXT, images)
- 📋 Upload optionnel d'offre d'emploi
- 🎯 11 modules d'analyse IAMonJob
- 🔧 API REST complète avec Flask
- 🔐 Intégration sécurisée avec Claude API
- 📊 Affichage des résultats en temps réel
- 🐳 Support Docker et docker-compose
- 📖 Documentation complète (README, GUIDE)
- 🚀 Scripts de démarrage rapide (Windows/Linux/Mac)

### Modules disponibles
1. Analyse du CV
2. Tableau des compétences
3. Notation et améliorations
4. Évolutions professionnelles
5. Gap Analysis
6. Optimisation ATS
7. Lettre de motivation
8. Pitch "Parlez-moi de vous"
9. Dans la tête du recruteur
10. Questions d'entretien
11. Veille entreprise

### Sécurité
- Validation des fichiers uploadés
- Suppression automatique après analyse
- Support CORS configurable
- Variables d'environnement pour secrets

---

## Format de versionnement

- **MAJOR** : Changements incompatibles de l'API
- **MINOR** : Ajout de fonctionnalités compatibles
- **PATCH** : Corrections de bugs compatibles

### Types de changements

- `Ajouté` : nouvelles fonctionnalités
- `Modifié` : changements de fonctionnalités existantes
- `Déprécié` : fonctionnalités bientôt supprimées
- `Supprimé` : fonctionnalités supprimées
- `Corrigé` : corrections de bugs
- `Sécurité` : corrections de vulnérabilités

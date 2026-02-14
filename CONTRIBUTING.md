# Guide de Contribution

Merci de votre intérêt pour contribuer à IAMonJob ! 🎉

## Comment contribuer

### 1. Fork & Clone

```bash
# Forkez le repo iamonjobv3 sur GitHub
# Puis clonez votre fork
git clone https://github.com/VOTRE-USERNAME/iamonjobv3.git
cd iamonjobv3
```

### 2. Créez une branche

```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
# ou
git checkout -b fix/correction-bug
```

### 3. Développez

- Suivez le style de code existant
- Ajoutez des commentaires si nécessaire
- Testez vos modifications

### 4. Committez

```bash
git add .
git commit -m "feat: description de la fonctionnalité"
# ou
git commit -m "fix: description de la correction"
```

**Format des commits :**
- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `style:` Formatage, style
- `refactor:` Refactorisation
- `test:` Tests
- `chore:` Maintenance

### 5. Pushez & Pull Request

```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

Puis créez une Pull Request sur GitHub.

## Standards de code

### Python (Backend)
- Suivre PEP 8
- Utiliser des docstrings
- Type hints recommandés

### JavaScript (Frontend)
- ES6+ moderne
- Commentaires pour les fonctions complexes
- Noms de variables descriptifs

### CSS
- Classes descriptives
- Organisation logique
- Responsive design

## Tests

Avant de soumettre une PR :

```bash
# Backend
cd backend
python -m pytest

# Frontend
# Testez manuellement dans le navigateur
```

## Questions ?

Ouvrez une issue sur GitHub ou contactez les mainteneurs.

## Code de Conduite

Soyez respectueux, bienveillant et constructif dans vos interactions.

Merci pour votre contribution ! 💜

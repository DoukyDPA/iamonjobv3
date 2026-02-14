# Politique de Sécurité

## Versions Supportées

| Version | Support         |
| ------- | --------------- |
| 1.0.x   | :white_check_mark: |

## Signaler une Vulnérabilité

Si vous découvrez une vulnérabilité de sécurité, veuillez **NE PAS** ouvrir une issue publique.

### Comment signaler

1. **Email** : Envoyez un email à [security@votre-domaine.com]
2. **Décrivez** la vulnérabilité en détail
3. **Incluez** les étapes pour reproduire si possible
4. **Attendez** une réponse sous 48h

### Ce que nous faisons

1. Nous confirmons la réception sous 48h
2. Nous évaluons la vulnérabilité
3. Nous développons un correctif
4. Nous publions le correctif
5. Nous vous créditons (si vous le souhaitez)

## Bonnes Pratiques de Sécurité

### Pour les utilisateurs

- ✅ Ne partagez JAMAIS votre clé API Claude
- ✅ Utilisez des variables d'environnement pour les secrets
- ✅ Limitez les permissions de votre clé API
- ✅ Mettez à jour régulièrement l'application
- ✅ Utilisez HTTPS en production
- ✅ Ne commitez pas de fichiers `.env`

### Pour les développeurs

- ✅ Validez toutes les entrées utilisateur
- ✅ Sanitisez les fichiers uploadés
- ✅ Limitez la taille des fichiers
- ✅ Utilisez des tokens CSRF en production
- ✅ Auditez les dépendances régulièrement
- ✅ Chiffrez les données sensibles

## Dépendances

Vérifiez régulièrement les vulnérabilités :

```bash
# Backend Python
pip install safety
safety check

# Audit npm si utilisé
npm audit
```

## Mises à jour de sécurité

Les correctifs de sécurité sont publiés dès que possible avec :
- Version patch (x.x.X)
- Release notes détaillées
- Migration guide si nécessaire

Merci de nous aider à garder IAMonJob sécurisé ! 🔒

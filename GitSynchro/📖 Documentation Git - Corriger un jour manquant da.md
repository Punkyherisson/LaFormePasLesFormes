 jij_u<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# 📖 Documentation Git - Corriger un jour manquant dans le journal

## Contexte du problème

**Date : 09 décembre 2025**
Un commit du **28 novembre 2025** manquait dans le repo `LaFormePasLesFormes/ApprentissageEtCoaching`.
`git status` montrait la branche à jour avec GitHub, mais `git log` confirmait l'absence du 28/11.

## Séquence complète de correction (Windows CMD)

```bash
# Étape 1 : Créer le fichier du jour manquant
cd "C:\Github.com\Punkyherisson\LaFormePasLesFormes\ApprentissageEtCoaching"
echo 2025-11-28 - Travail du jour manquant > journal_2025-11-28.md
echo. >> journal_2025-11-28.md
echo - Activité physique effectuée >> journal_2025-11-28.md
echo - Notes prises sur [sujet] >> journal_2025-11-28.md
echo - Préparation pour le 29/11 >> journal_2025-11-28.md

# Étape 2 : Ajouter et commiter avec date rétroactive
git add journal_2025-11-28.md
set GIT_AUTHOR_DATE=2025-11-28 12:00:00 +0100 ^
&& set GIT_COMMITTER_DATE=2025-11-28 12:00:00 +0100 ^
&& git commit -m "2025-11-28: Compléter journal - travail du jour manquant"

# Étape 3 : Pousser sur GitHub
git push origin main
```


## Résultat obtenu

```
* 23962cb 2025-11-28 2025-11-28: Travail du jour manquant  ✅
* f86945d 2025-12-09 Retructuration projet
* a7acb1f 2025-12-08 Restructuration 2
...
```


## Explications techniques

| Variable | Rôle | Impact GitHub |
| :-- | :-- | :-- |
| `GIT_AUTHOR_DATE` | Date d'écriture du commit | ✅ Contribution comptée le 28/11 |
| `GIT_COMMITTER_DATE` | Date de validation finale | Affichage dans `git log %cd` |
| `--allow-empty` | Permet commit sans changements | Utile pour dates rétroactives |

## Vérifications post-correction

```bash
# Log avec dates auteur/commit
git log --oneline -5 --pretty=format:"%h %ad %cd %s" --date=short

# Statut branche
git status

# Comparaison local/distant
git log origin/main..HEAD --oneline
```


## Notes importantes

- ✅ **GitHub compte les contributions par `GIT_AUTHOR_DATE`**
- ✅ **L'historique reste intègre** (pas de rebase forcé)
- ✅ **Documentation fidèle** du travail effectué
- ⚠️  Utiliser **uniquement pour journaux de bord**, pas pour falsifier l'historique de code

**Copiez ce contenu dans `docs/git-correction-28nov2025.md`** pour référence future ! 🎉

```markdown
<!-- Sauvegardez ce fichier dans votre repo -->
git add docs/git-correction-28nov2025.md
git commit -m "Documentation: Correction commit manquant 28/11"
git push origin main
```


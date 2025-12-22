<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Procédure complète : Commit oublié (rétrodaté)

**Quand tu as oublié de commiter/pousser le 21/12** :

```cmd
REM 1. Ajouter les fichiers modifiés
git add .

REM 2. Forcer la date AUJOURD'HUI (même année que maintenant)
set GIT_AUTHOR_DATE="2025-12-21 12:00:00 +0100"
set GIT_COMMITTER_DATE="2025-12-21 12:00:00 +0100"

REM 3. Commit + push
git commit -m "2025-12-21: [ton message]"
git push origin main
```

**✅ Résultat** : GitHub compte une contribution le 21/12 dans ton streak[^1]

## Nettoyer après (commits suivants = date normale)

**Après un commit rétrodaté, les variables restent actives** → tes prochains commits auront la mauvaise date !

**Nettoyer IMMÉDIATEMENT après** :

```cmd
REM PowerShell
Remove-Item Env:\GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:\GIT_COMMITTER_DATE -ErrorAction SilentlyContinue

REM CMD
set GIT_AUTHOR_DATE=
set GIT_COMMITTER_DATE=
```

**Vérifier que c'est propre** :

```cmd
git add test.txt  REM Crée un fichier test
git commit -m "test date normale"
git log -1 --pretty=fuller
```

→ `AuthorDate` doit être **aujourd'hui** (22/12/2025), pas 21/12[^2]

## Script 1-clic (à copier dans un .bat)

Crée `commit-retro.bat` dans ton repo :

```batch
@echo off
echo Date du commit (AAAA-MM-JJ HH:MM:SS +0100) ?
set /p DATE="> "

git add .
set GIT_AUTHOR_DATE="%DATE%"
set GIT_COMMITTER_DATE="%DATE%"
git commit -m "Commit retro: %DATE%"
git push origin main

REM Nettoyage auto
set GIT_AUTHOR_DATE=
set GIT_COMMITTER_DATE=
echo Variables nettoyées ! Prochains commits = date normale.
pause
```


## Checklist rapide

| Étape | Commande | ✅ Vérif |
| :-- | :-- | :-- |
| 1. Ajouter | `git add .` | `git status` |
| 2. Dater | `set GIT_AUTHOR_DATE="2025-12-21 12:00:00 +0100"` | - |
| 3. Commit | `git commit -m "..."` | `git log -1 --pretty=fuller` |
| 4. Push | `git push origin main` | GitHub.com |
| 5. Nettoyer | `set GIT_AUTHOR_DATE=` | Test commit normal |

**Mémoire** : Tu fais ça souvent pour `LaFormePasLesFormes` → toujours nettoyer après ![^3]
<span style="display:none">[^4]</span>

<div align="center">⁂</div>

[^1]: https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference

[^2]: https://stackoverflow.com/questions/11856983/why-is-git-authordate-different-from-commitdate

[^3]: tools.version_control

[^4]: https://www.perplexity.ai/search/d65566bd-fa5a-44b4-90ed-fd1901068e25


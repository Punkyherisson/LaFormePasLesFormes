<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# ca yest je me souviens j'ai fait ca hier car j'ai eu un pb similaire Tu as (volontairement ou non) utilisé une date forcée via git commit --date ou les variables GIT_AUTHOR_DATE / GIT_COMMITTER_DATE (moins probable si tu ne l’as jamais fait).


Oui, c’est exactement ça : en forçant la date hier, tu as “programmé” ton commit pour le 17 décembre, et la commande d’aujourd’hui a juste réutilisé cette date forcée.[^1][^2]

## Ce qui s’est passé

- Quand tu fais `git commit --date "..."`, Git écrit cette date dans `AuthorDate` (et souvent tu synchronises aussi `GIT_COMMITTER_DATE`, donc les deux champs sont au 17).[^2][^1]
- Si les variables d’environnement `GIT_AUTHOR_DATE` / `GIT_COMMITTER_DATE` restent définies dans ton shell/PowerShell, elles s’appliquent aussi aux commits suivants, même si tu ne remets pas `--date`.[^3][^4]

Résultat : ton commit de ce matin a pris la même date future que celui que tu voulais “réparer”.

## Comment éviter que ça recommence

1. **Nettoyer les variables d’environnement** dans ton terminal avant de continuer à travailler, surtout après un commit avec date custom.[^5][^3]
    - PowerShell :

```powershell
Remove-Item Env:\GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:\GIT_COMMITTER_DATE -ErrorAction SilentlyContinue
```

    - Bash (Git Bash, WSL, etc.) :

```bash
unset GIT_AUTHOR_DATE
unset GIT_COMMITTER_DATE
```

2. **Faire un commit de test** pour vérifier que les dates sont redevenues normales :

```bash
git add .
git commit -m "test dates normales"
git log -1 --pretty=fuller
```

Tu dois voir `AuthorDate` et `CommitDate` à la date/heure réelle.[^6]

## Corriger le commit actuel (si tu veux)

Pour remettre la bonne date sur le dernier commit (celui au 17), tu peux faire :

```bash
git commit --amend --no-edit --date="now"
git push --force-with-lease
```

- `--date="now"` remet la date actuelle comme `AuthorDate`; en général cela met aussi le `CommitDate` à maintenant quand tu amendes.[^7][^6]
- `--force-with-lease` met à jour le dépôt distant avec ce commit corrigé (attention si quelqu’un d’autre a déjà pull).

Si tu veux, tu peux coller ici la commande exacte que tu avais tapée hier avec `--date`, et on vérifie ensemble comment la neutraliser proprement.
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.reddit.com/r/git/comments/ympce5/is_it_possible_to_change_commit_date/

[^2]: https://manpages.ubuntu.com/manpages/jammy/man1/git-commit.1.html

[^3]: https://cassidoo.co/post/change-git-timestamp/

[^4]: https://til.simonwillison.net/git/backdate-git-commits

[^5]: https://garysferrao.github.io/git/commit/date/2015/12/01/change-git-commit-date.html

[^6]: https://graphite.com/guides/git-commit-date

[^7]: https://dev.to/pradumnasaraf/commit-with-a-past-date-and-time-in-git-1j2f

[^8]: https://stackoverflow.com/questions/11856983/why-is-git-authordate-different-from-commitdate

[^9]: https://seasidetesting.com/2024/08/04/author-and-committer-dates-in-git-an-obscure-bug/

[^10]: https://stackoverflow.com/questions/41301627/how-to-update-git-commit-author-but-keep-original-date-when-amending

[^11]: https://stackoverflow.com/questions/28536980/git-change-commit-date-to-author-date

[^12]: https://www.reddit.com/r/git/comments/1buk8ao/accidentally_made_commits_into_the_future/

[^13]: https://learn.microsoft.com/en-us/azure/devops/repos/git/git-dates?view=azure-devops

[^14]: https://gist.github.com/ugultopu/0b6412674073a5b603f8227cb108441c

[^15]: https://www.youtube.com/watch?v=UuwjEsqB1Ig

[^16]: http://jays1204.github.io/git/2021/02/25/git-date.html

[^17]: https://stackoverflow.com/questions/33544733/how-do-i-prevent-future-commit-date-time-in-git-server-origin-side

[^18]: https://git-scm.com/docs/git-commit/2.24.0

[^19]: https://github.com/JoshCheek/stop-committing-in-the-future

[^20]: https://github.com/orgs/community/discussions/22251


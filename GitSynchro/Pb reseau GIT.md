<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# je veux le faire dans cmd

Pour CMD (Invite de commandes Windows), utilisez `set` au lieu de `$env:` pour définir les dates du commit au 11 décembre.[^1][^2]

## Séquence CMD complète

Depuis `C:\Github.com\Punkyherisson\LaFormePasLesFormes`, exécutez :

```
git add "GitSynchro/Aliments a limiter.md"
set GIT_AUTHOR_DATE=2025-12-11 12:00:00 +0100 && set GIT_COMMITTER_DATE=2025-12-11 12:00:00 +0100 && git commit -m "2025-12-11: Aliments à limiter (problème réseau)"
git push origin main
```


## Vérification

```
git log --oneline -3 --pretty=format:"%h %cd %s" --date=short
```

Le commit apparaîtra daté du 11/12/2025. GitHub comptera une contribution ce jour-là.[^3][^1]

<div align="center">⁂</div>

[^1]: https://www.perplexity.ai/search/327c8f4c-1228-4657-b414-c031a61b16b6

[^2]: https://git-scm.com/docs/git-add

[^3]: https://www.perplexity.ai/search/f20629c3-0fa5-416e-8c49-1678fe89491b


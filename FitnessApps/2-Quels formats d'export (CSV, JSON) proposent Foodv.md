<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Quels formats d'export (CSV, JSON) proposent Foodvisor et Yazio

Foodvisor ne propose pas d’export direct en formats standard du type CSV ou JSON directement dans l’application ou via le web. Cependant, il utilise la synchronisation avec Apple Health ou Google Fit, ce qui permet d’exporter vos données indirectement depuis ces plateformes vers des fichiers CSV via des apps tierces compatibles. L’application conserve les données dans le cloud mais ne propose pas de fonction d’export « self-serve » en CSV ou JSON pour l’utilisateur final.[^1][^2]

Yazio ne propose pas d’export natif en CSV ou JSON dans ses menus, même dans la version Pro. Toutefois, si vous synchronisez Yazio avec Samsung Health ou Apple Health, vous pouvez récupérer un export CSV depuis ces applications santé généralistes. Il existe également des scripts et outils tiers (exemple : yazio-csv-exporter sur GitHub) permettant d’extraire des données de Yazio et de les convertir en CSV, mais cela n’est pas officiellement supporté dans l’application elle-même.[^3][^4][^2]

### Comparatif des formats d’export

| Application | Export natif CSV | Export natif JSON | Export indirect (API/santé) | Outils/scrips tiers |
| :-- | :-- | :-- | :-- | :-- |
| Foodvisor | Non | Non | Oui via Apple/Google Health | Possible, non officiel[^1][^2] |
| Yazio | Non | Non | Oui via Apple/Samsung Health | Oui, via GitHub yazio-csv-exporter[^3][^4][^2] |

Aucun des deux ne propose une extraction directe et complète vers CSV/JSON depuis leur interface standard ; il faut passer par des services de santé ou scripts tiers pour obtenir ce type d’export.[^4][^2][^1][^3]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.futura-sciences.com/tech/definitions/logiciels-foodvisor-27099/

[^2]: https://www.dietmate.fr/blog-posts/exporter-toutes-vos-donnees-nutrition-csv

[^3]: https://www.reddit.com/r/yazio/comments/1k5tzki/not_another_yazio_still_doesnt_let_you_export/

[^4]: https://github.com/tobintax

[^5]: https://www.lesnumeriques.com/telecharger/foodvisor-54578

[^6]: https://www.foodvisor.io/fr/terms-of-service/

[^7]: https://www.foodvisor.io/fr/privacy-policy/

[^8]: https://www.forbes.fr/entrepreneurs/comment-foodvisor-lapplication-francaise-qui-scanne-votre-assiette-veut-conquerir-le-monde/

[^9]: https://www.youtube.com/watch?v=uwC8veTrYrc

[^10]: https://support.apple.com/fr-fr/guide/iphone/iph392b962da/ios

[^11]: https://support.kizeo.com/en/articles/11554116-exporting-your-data-the-csv-format

[^12]: https://help.yazio.com/hc/en-us/articles/360002401437-How-do-I-copy-Diary-entries-to-another-day

[^13]: https://foodvisor.wordpress.com/2016/05/10/10-astuces-foodvisor-que-vous-ne-connaissiez-pas/

[^14]: https://www.youtube.com/watch?v=nGPPe0MzskU

[^15]: https://n8n.io/workflows/1731-export-csv-file-to-json/

[^16]: https://play.google.com/store/apps/details?id=io.foodvisor.foodvisor\&hl=ln

[^17]: https://www.foodvisor.io/fr/guides/

[^18]: https://forum.bubble.io/t/easy-way-to-csv-to-json/276577

[^19]: https://www.reddit.com/r/FitnessDE/comments/1ionux5/gute_yazio_alternative/

[^20]: https://nutriscan.app/blog/posts/best-free-ai-calorie-tracking-apps-2025-bd41261e7d


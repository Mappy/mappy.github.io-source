Title: Découpage des polices de caractères
Date: 2018-05-25
Slug: webperfs-split-fonts
Author: Nicolas Bétheuil, Manuel Emeriau, Jonathan Saget, Grégory Paul
Category: Web
Tags: français,javascript,webperfs,docker
Summary: Comment découper une police de caractères en deux nous a fait économiser 220 ko de chargement initial

Après [avoir mis en place SiteSpeed](webperfs-sitespeed.html) et [optimisé le code JavaScript](webperfs-webpack.html), nous avons travaillé sur l’optimisation des polices de caractères du site [mappy](https://fr.mappy.com/).


## Constat

Nous avions vu que le Javascript était la ressource la plus lourde chargée sur le site.
Mais en ne tenant compte que du poids « gzipé » (ce qui nous intéresse au final) on se rend compte que les polices de caractères sont quasiment aussi lourdes.

![taille avant optimisations](images/web/webperfs/size-before-font.png)

_Les barres bleues correspondent à la taille du contenu non compressé, les barres vertes au contenu compressé (`gzip`)._
Les polices de caractères sont compressées, ce qui explique que les 2 barres aient la même taille.

En y regardant de plus près, nous chargeons 5 polices de caractères sur le site :

![tailles des polices](images/web/webperfs/fonts-size-prod.png)

 - la `Fira` en 3 graisses différentes (environ ~60 Ko),
 - la `Thirsty` (~28 Ko),
 - la `MappyIcons` (*~247 Ko*).

Cette `MappyIcons` est très conséquente car elle contient les icônes utilisés sur le site :

![caractères de la police](images/web/webperfs/MappyIcons.png)

Néanmoins, seuls quelques caractères (icônes) sont utilisés sur la page d’accueil. Il est ainsi dommage de charger l’ensemble de la police de caractères.

## Optimisations sur les polices de caractères (fonts)

Grâce à l’[attribut CSS `unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/%40font-face/unicode-range) (relativement [bien supporté](https://caniuse.com/#search=unicode-range)), il est possible de découper la police de caractères en 2, en laissant au navigateur web le soin de charger la ou les bons fichiers en fonction des caractères affichés sur le site.

Après quelques recherches, nous avons trouvé un outil en python (pyftsubset) pour la manipulation de polices de caractères.

Pour rendre cela plus transparent dans notre processus de construction, nous l’avons encapsulé dans [une image docker dénommée `filter-font`](https://github.com/Mappy/filter-font) ([présente sur docker hub](https://hub.docker.com/r/mappydt/filter-font/)), prenant en entrée une police de caractères ainsi qu’une liste de caractères, par exemple :

```
  U+0031 #lieux
  U+0032 #shopping
  U+E005 #iti
```

pour générer 2 polices de résultat, l’une « light » contenant uniquement les caractères demandés, l’autre « the-rest » avec les caractères restants.

Voici un exemple avec les caractères uniquement présents sur la page d’accueil du site Mappy :

![découpage des polices](images/web/webperfs/splitted-fonts.png)

On remarque que la `MappyIcons-Regular-light` occupe ~30 Ko, et seulement ~25 au format `woff2` (lui aussi, [relativement bien supporté](https://caniuse.com/#search=woff2)) au lieu des presque 250 Ko initiaux.

Voici les caractères contenus dans la police « light » :

![caractères de la police light](images/web/webperfs/mappyfont-light.png)


## Gains

Après ces optimisations, la taille des polices de caractères a drastiquement baissé (gain de 220 Ko) :

![taille après optimisations](images/web/webperfs/size-after-font.png)

Au final, cette action d’optimisation ainsi que la séparation du code JavaScript ont eu pour effet de faire baisser notre speed index d’une moyenne de ~6000 à ~4000 (speed index moyen sur 5 pages depuis une connexion 3g) :

![métriques après l’optimisation de la police](images/web/webperfs/after-font-optim.png)

## Et ensuite ?

Nous avons encore quelques pistes pour encore réduire la taille du JavaScript sur le site [mappy](https://fr.mappy.com).
Nous espérons donc à nouveau une baisse de notre speed index.


De façon plus globale, la performance web est très importante pour l’utilisateur, mais aussi pour le référencement (les moteurs de recherche en tiennent compte).
Aussi, la surveillance et l’amélioration des performances doivent être intégrées dans le processus de développement logiciel, idéalement à l’intégration/déploiement continu.
Il est nécessaire de surveiller les indicateurs de performances et de réagir en cas de baisse de performance, au même titre qu’une régression fonctionnelle.



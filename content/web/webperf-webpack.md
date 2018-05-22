Title: Découpage du code JavaScript grâce à webpack
Date: 2018-05-22
Slug: webperfs-webpack
Author: Nicolas Bétheuil, Manuel Emeriau, Jonathan Saget, Grégory Paul
Category: Web
Tags: français,javascript,webperfs
Summary: Comment nous avons utilisé webpack pour découper notre code JavaScript

Après [avoir mis en place SiteSpeed](web-perfs-site-speed.html), il était temps de procéder à des améliorations de performances.

En regardant la composition de nos pages web (grâce à SiteSpeed), on se rend compte que le JavaScript en est la plus grosse partie du site [mappy](https://fr.mappy.com/) :

![taille avant optimisations](images/web/webperfs/size-before-js.png)

Les barres bleues correspondent à la taille du contenu décompréssé, les barres vertes au contenu compressé (`gzip`).

C’est donc sur cette partie que nous nous sommes concentrés dans un premier temps.

## Optimisations sur le JavaScript


### Suppression de code

Une première action a été de supprimer des fonctionnalités ayant peu de valeur ajoutée pour l’utilisateur.


### Webpack à notre secours

La deuxième action, plus conséquente, est de découper le JavaScript en plusieurs parties, pour ne charger que le minimum de code par page.

Nous utilisions `browserify` pour construire notre JavaScript mais, ce dernier est moins outillé pour répondre à ce problème (popularité en baisse donc écosystème assez pauvre).
Par conséquent, nous avons tout d’abord migré de `browserify` vers `webpack`.

Nous avons alors séparé notre code en deux avec un « vendors.js » (contenant nos bibliothèques) et le code de notre application.

Cette séparation a en effet du sens, puisque en utilisant des entêtes de cache relativement long (6 mois sur nos fichiers JavaScript), ce fichier vendors.js aura tendance à rester dans le cache du navigateur. Il ne sera donc pas re-téléchargé pour les prochaines visites sur notre site, tant que ce fichier n’aura pas été mis à jour.
Bien sûr, il convient d’ajouter un suffixe au nom du fichier (une empreinte ou `hash`) qui changera si une bibliothèque était mise à jour.
Cette technique est celle du « [long term caching](https://developers.google.com/web/fundamentals/performance/webpack/use-long-term-caching) ».

![découpage du vendors.js](images/web/webperfs/size-js-vendors.png)


Puis, nous avons commencé à découper le code de façon plus fine pour aboutir a de nombreux plus petits fichiers ou `chunks` dans la dénomination `webpack`.
Dans un premier temps, nous avons abandonné la séparation par langue (qui était intéressant en HTTP/1.1 où l’on cherchait à limiter les fichiers à télécharger mais plus depuis HTTP/2.0, [massivement supporté aujourd’hui](https://caniuse.com/#feat=http2)).
Puis nous avons extrait certaines parties de code qui n’étaient chargées que sur une page dédiée (page d’impression, note de frais).
Enfin, certains `chunks` sont maintenant chargés automatiquement par `webpack` à l’exécution :

![découpage au chargement initial](images/web/webperfs/size-js-more-bundles.png)

On remarque une diminution de 13 Ko par rapport à l’exemple précédent.

Et, au click sur le bouton itinéraire, le code nécessaire se charge à la volée :

![découpage de la partie itinéraire](images/web/webperfs/size-js-bundle-iti.png)


Voici une autre représentation avant / après via [WebPack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer), un formidable outil pour inspecter les `chunks` `webpack` :

Avec la séparation du vendors.js :

![séparation du vendors.js](images/web/webperfs/bundle-vendors.png)

Avec la séparation en multiples `chunks` :

![séparation d’autres morceaux de code](images/web/webperfs/more-js-bundles.png)

On remarque de nombreux `chunks`, heureusement gérés par `webpack`.


### Résultats

Avec ces optimisations, nous sommes passés de 375 Ko de JavaScript (`gzip`) à 335 Ko sur le chargement de la page d’accueil.

![taille après optimisations](images/web/webperfs/size-after-js.png)

La séparation du code JavaScript n’est toutefois pas encore totalement finalisée.
Nous avons en effet encore d’autres point de coupes à effectuer pour diminuer encore la taille du code JavaScript.

Le JavaScript n’étant qu’une partie (certes importante) de notre site, le prochain article détaillera des optimisations sur d’autres types de ressources.

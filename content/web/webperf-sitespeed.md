Title: Automatiser vos relevés de webperfs
Date: 2018-05-16
Slug: webperfs-sitespeed
Author: Nicolas Bétheuil, Manuel Emeriau, Jonathan Saget, Grégory Paul
Category: Web
Tags: français,javascript,webperfs
Summary: Comment nous avons automatisé le lancement de mesures de performances web.

## La Performance Web chez Mappy

Nous surveillons depuis longtemps la performances web (couramment abrégé « webperfs ») sur le site [mappy](https://fr.mappy.com/) mais des évenements récents ont remis ce sujet en haut de nos priorités.

L’usage du site a en effet changé ces dernières années avec de plus en plus de visites depuis des navigateurs mobiles.

Selon [statcounter](http://gs.statcounter.com/platform-market-share/desktop-mobile/france/#yearly-2016-2018), l’audience mobile en France est passé de ~23 % en 2016 à ~38 % en 2018 :

![statistiques mobile versus bureau](images/web/webperfs/stats-mobile-2018.png)

Ainsi, un temps de chargement acceptable depuis un navigateur de « bureau » hier ne l’est plus forcément depuis un téléphone mobile avec une connexion cellulaire moyenne aujourd’hui.

Par ailleurs, Google a [annoncé la modification de son index](https://webmasters.googleblog.com/2016/11/mobile-first-indexing.html) pour se baser sur les sites mobiles en priorité et tient [compte de leurs vitesses de chargement](https://webmasters.googleblog.com/2018/01/using-page-speed-in-mobile-search.html).

Nous avons mené plusieurs actions récemment pour améliorer la vitesse de chargement : la mise en place de mesure automatisée puis un cycle itératif entre des actions de performances web et la vérification de leur impact.

## Des mesures automatisées

### Via WebPageTest

![WebPageTest](images/web/webperfs/webpagetest.png)

Nous utilisons [WebPageTest](https://www.webpagetest.org) depuis 2015 à travers une installation locale.

Cet outil nous donnait satisfaction mais avec 2 contraintes :

 - n’ayant pas trouvé de solution simple, nous notions manuellement chaque semaine certaines valeurs (speed index, temps de chargement, taille de la page) sur un tableau partagé,
 - son installation, notamment pour maintenant lancer des tests sur des téléphones mobiles, est loin d’être une [partie](https://github.com/WPO-Foundation/webpagetest-docs/blob/master/user/Private%20Instances/README.md) [de](https://sites.google.com/a/webpagetest.org/docs/private-instances/locations) [plaisir](https://github.com/WPO-Foundation/webpagetest-docs/blob/master/user/Private%20Instances/wptdriver.md).

WebPageTest n’étant idéal pour nos besoins (automatisation du relevé des métriques et lancement sur navigateurs mobiles), nous avons donc comparé WebPageTest avec [LightHouse](https://developers.google.com/web/tools/lighthouse/), [SiteSpeed](https://www.sitespeed.io/) et [Phantomas](https://www.npmjs.com/package/phantomas).

Nous utilisons déjà Phantomas pour vérifier que certains indicateurs de performance ne régrèssent pas (taille et nombres des JS/CSS, compression `gzip`, etc).

En parlant de métriques, le W3C a d’ailleurs standardisé une API ([Navigation Timing API](https://www.w3.org/TR/navigation-timing/#process)) permettant de recueillir une quantité assez impressionnante de métriques au sein du navigateur :
![Timing overview](images/web/webperfs/timing-overview.png)

Voici la matrice que nous avons utilisé pour prendre notre décision quant aux métriques que proposent ces outils :

![Timing overview](images/web/webperfs/decision-matrix.png)


### Et maintenant SiteSpeed

![SiteSpeed](images/web/webperfs/sitespeed.png)

Nous avons au final porté notre choix sur SiteSpeed pour les raisons suivantes :

 - il s’installe très facilement via [Docker](https://www.sitespeed.io/documentation/sitespeed.io/installation/#docker),
 - il permet de se lancer en simulant un environnement mobile (taille du navigateur et bridage de la connexion),
 - il génère les métriques que nous jugeons nécessaires, ainsi que des rapports détaillés incluant une vidéo du chargement de la page comme le fait WebPageTest ([exemple de rapport](https://examples.sitespeed.io/6.0/2017-11-23-23-43-35/) et d’[une vidéo](https://examples.sitespeed.io/6.0/2017-11-23-23-43-35/pages/en.wikipedia.org/wiki/Main_Page/index.html#browsertime)),
 - il permet facilement d’exporter des graphiques à mettre sur notre « wall » (écran de supervision des métriques du site web).

Il ne restait plus qu’à programmer le lancement de SiteSpeed toutes les heures sur nos différents environnements et sur quelques pages de notre site.


Après un tir, SiteSpeed peut envoyer les métriques dans [grafana](https://grafana.com/), un outil de visualisation de données (`dataviz`).
Cela nous permet de générer un graphique présentant la moyenne des « speed index » sur notre « wall » pour suivre son évolution :

![métriques](images/web/webperfs/wall.png)

Ceci est un synthèse mais de nombreuses autres graphiques sont disponibles :

![grafana](images/web/webperfs/grafana.png)

Vous pouvez découvrir un [exemple intéractif testant wikipedia](https://dashboard.sitespeed.io/d/000000043/page-summary?orgId=1).


Cette première étape finalisée, il est temps de passer aux optimisations, qui feront l’objet de prochains articles.

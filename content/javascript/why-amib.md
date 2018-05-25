Title: Backbone isomorphique maison : pourquoi ?
Date: 2018-01-10
Slug: pourquoi-backbone-isomorphique
Author: Nicolas Bétheuil
Category: Web
Tags: français,javascript,node.js,backbone
Summary: Pourquoi-a-t'on réécrit une librairie isomorphique basée sur backbone ?

Vous l'avez peut-être remarqué, nous avons refait une partie du site il y a bien six mois maintenant : les itinéraires. Nous appelons cela le multipath (prononcer [moultipaðe](https://www.anglaisfacile.com/exercices/exercice-anglais-2/exercice-anglais-66477.php))

Petit tour du propriétaire : vous pouvez dorénavant pour une recherche d'itinéraire avoir les réponses dans plusieurs modes de transport : voiture (évidemment), bus, car, taxi, VTC, transport en commun, à pied ... et beaucoup d'autres modes suivront.

Comme pour n'importe quelle partie du site : le [SEO](https://www.wikiwand.com/fr/Optimisation_pour_les_moteurs_de_recherche) est une exigence forte. Nos pages doivent répondre de la même manière pour un moteur de recherche que pour une navigation utilisateur classique.

Lors de la [migration de PHP vers NodeJS](http://techblog.mappy.com/mappy-com-de-php-a-nodejs.html) réalisée l'année dernière, une architecture a été posée avec une séparation nette entre la partie serveur sous `express` et la partie cliente pilotant des vues `Backbone`. Cela impliquait notamment deux manières complètement différentes de récupérer la donnée avant de rendre la vue. Nous souhaitions explorer d'autres pistes pour faire évoluer l'architecture sans tout refondre. La piste de l'isomorphisme a alors été suivie pour uniformiser cette récupération de donnée. Nous souhaitions également suivre de manière plus rigoureuse le design MV de backbone.

Une autre contrainte était la courbe d'apprentissage et le délai que nous avions pour faire cette évolution stratégique du produit Mappy. Nous étions une équipe de cinq développeurs, les autres connaissaient déjà [backbone](http://backbonejs.org/) et j'arrivais avec plus de connaissances sur [ReactJS](https://reactjs.org/) et la refonte d'un autre site en isomorphique.

Pour des raisons de "time to market", nous ne souhaitions pas migrer tout le site vers React. Par ailleurs, l’ajouter en plus de backbone, avec son ecosystème et ses ~40Kb minifiés & compressés était problèmatique pour des raisons de performance, notamment en mobile.

L'idée était donc d'apporter une réponse proportionnée, adéquate, co-construite et réfléchie sans tout remettre en cause : l'architecture, les compétences de l'équipe et l'ambition stratégique du produit.

Nous avons donc décidé de suivre cette voie de manière itérative. Tout d'abord par un POC (Proof Of Concept) puis par une intégration progressive dans les composants développés en s'attaquant à la plus grosse difficulté suivante.

Nous avons commencé par un POC le 24 avril 2017 : en moins d'une semaine, nous avions une première version fonctionnelle qui montrait comment faire communiquer les composants entre eux avec un code applicatif identique entre la version cliente et serveur. Les nuances clients vs serveur étaient localisées dans ce que nous avons appelé plus tard AMIB pour Asynchronous Mappy Isomorphic Backbone. Le 11 mai, après avoir validé AMIB de façon collégiale en réunion technique, nous avons fusionné cette première version de travail fonctionnelle dans la branche principale ce qui a permis de partager le travail d'implémentation des vues avec les autres membres de l'équipe.

Chez Mappy, nous avons la possibilité d'essayer, d'apprendre, d'expérimenter. On travaille ensemble à définir des objectifs, des modes de collaboration, des jalons, des étapes pour satisfaire les besoins qui nous sont exprimés.

PS : Pour plus de notions / culture / références sur l'isomorphisme ... je vous laisse vous documenter si vous désirez en savoir plus : [chez Airbnb](https://medium.com/airbnb-engineering/isomorphic-javascript-the-future-of-web-apps-10882b7a2ebc) ou [chez M6](http://tech.m6web.fr/isomorphic-single-page-app-parfaite-react-flux/).

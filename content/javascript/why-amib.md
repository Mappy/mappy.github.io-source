Title: Backbone isomorphique maison : pourquoi ?
Date: 2018-01-10
Slug: pourquoi-backbone-isomorphique
Author: Nicolas Bétheuil
Tags: french,javascript,node.js,backbone
Summary: Pourquoi a t'on réécrie une librairie isomorphique backbone ?

Vous avez peut être remarqué, nous avons refait une partie du site il y a bien six mois maintenant : les itinéraires. Nous appellons cela le multipath(prononcer [moultipaðe](https://www.anglaisfacile.com/exercices/exercice-anglais-2/exercice-anglais-66477.php))

Petit tour du propriétaire : vous pouvez dorénavant pour un calcul d'itinéraire avoir les réponses dans plusieurs mode de transport : voiture (évidement), bus, transport-en-commun, à pied ... et beaucoup d'autre modes suivront. 

Pour refaire cette partie du site, nous avions toujours la 'contrainte' forte du [SEO](https://www.wikiwand.com/fr/Optimisation_pour_les_moteurs_de_recherche) : nos pages doivent répondre de la même manière pour un moteur de recherche que pour une navigation utilisateur classique. Le sujet de cette article n'est pas d'expliquer cette tendance dans les développement (le pourquoi) web mais de s'attarder sur le comment. Je vous laisse aller vous documenter si vous désirez en savoir plus par exemple en suivant [ce lien avec airbnb](https://medium.com/airbnb-engineering/isomorphic-javascript-the-future-of-web-apps-10882b7a2ebc) ou [celui la chez m6](http://tech.m6web.fr/isomorphic-single-page-app-parfaite-react-flux/).

Lors de la [migration de PHP vers NodeJS](http://techblog.mappy.com/mappy-com-de-php-a-nodejs.html) réalisée l'année précédente une architecture avait été posée avec une séparation nette entre la partie serveur et la partie cliente. Chacune des parties avait son propre controlleur, l'un express et l'autre custom. Cela impliquait nottament deux maniêres complétement différentes de récupérer la donnée. L'équipe à alors décider de ne pas péréniser cette architecture et de la remettre en cause. La piste de l'isomorphisme a alors été suivi pour uniformiser cette rérupération de donnée. Nous souhaitions également plus suivre le design MV de backbone. 

Une autre contrainte était la courbe d'apprentissage et le délais que nous avions pour faire cette évolution stratégique du produit Mappy. Nous étions une équipe de cinq développeurs, les autres connaissaient déjà [backbone](http://backbonejs.org/) et j'arrivais avec plus de connaissances sur [ReactJS](https://reactjs.org/) et une refonte d'une autre site en isomorphique. 

Nous ne souhaitions pas utiliser React, son écosystème et ses minimum ~40Kb minified + gzipped en plus de backbone sur le site pour des raisons de performance nottament en mobile. 

L'idée était donc d'apporter une réponse proportionnée, adéquate, co-construite et réflechit sans tout remettre en cause : l'architecture, les compétences de léquipe et l'ambition stratégique du produit. 

Nous avons donc décidé de manière itérative d'essayer cette voie tout d'abord par un POC puis par une intégration progressive dans les composants dévoloppées en s'attaquant à la plus grosse difficulté suivante. 

Nous avons commencé par un POC le 24 avril 2017 : en moins d'une semaine, nous avions une première version fonctionnelle qui montrait comment faire communiquer les composants entre eux avec un code applicatif identique entre la version cliente et serveur. Les nuances clients vs serveur étaient localisées dans ce que nous avons appellé plus tard AMIB pour Asynchronous Mappy Isomorphic Backbone. Le 11 mai, nous avons mergé ce poc dans develop ce qui a permis de partager le travail d'implémentation des vues avec les autres membres de l'équipe.

Chez Mappy, nous avons la possibilité d'essayer, d'apprendre, d'expérimenter. On travail ensemble à définir des objectifs, des modes de collaboration, des jalons, des étapes pour satisfaire les besoins qui nous sont exprimés.
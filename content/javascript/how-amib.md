Title: Backbone isomorphique maison : comment ?
Date: 2018-01-10
Slug: comment-backbone-isomorphique
Author: Nicolas Bétheuil
Tags: french,JavaScript,NodeJS,Backbone
Summary: Comment a t'on réécrit une librairie isomorphique Backbone maison ?

Cet article fait écho a [Backbone isomorphique maison : pourquoi ?](/pourquoi-backbone-isomorphique.html). Celui ci va présenter comment AMIB a été construit.

La première difficulté était déjà de définir l'attendu. Quel code nous souhaitions écrire. Nous n'avons pas commencé par les tests contrairement à nos habitudes. Notre objectif était de savoir rapidement si nous étions sur une piste intéressante, pour éventuellement l'abandonner et éviter de gaspiller notre temps.
 
Schéma avec AMIB au milieu et les 2 controlleurs : mise en évidence de la réutilisation vue/modèle entre les deux
Mise en évidence de la structure arborescente 
Et asynchrone

Nous avons donc commencé par écrire :
- [notre première vue](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/fixtures/recursive-children-view/RecursiveChildrenView.js) que nous avons rapidement étoffée 
- pour avoir un modèle et un enfant, 
- puis avec [plusieurs enfant](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/fixtures/multiple-children-view/MultipleChildrenView.js), 
- puis avec un enfant [avec un modèle asynchrone](https://github.com/Mappy/amib/blob/master/fixtures/one-children-with-model/no-children-with-promise-model/NoChildrenWithPromiseModelView.js), c'est à dire un modèle étant une [promesse](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Promise). 

Comme Backbone ne fonctionne pas sous NodeJS à cause de sa dépendance avec JQuery (et l'usage du DOM), nous avons [surchargé/bouchonné les méthodes voulues](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/nodify-backbone.js). Nous avons donc pu exécuter une vue Backbone côté serveur. L'astuce de la [ré-implémentation de setElement](http://backbonejs.org/docs/backbone.html#section-162) permet d'avoir la même interface de sortie. La différence porte juste sur la manière de retourner la vue Backbone afin qu'elle soit [ajoutée soit au DOM dans le navigateur](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/render.js#L164) soit [dans la réponse sous NodeJS](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/render.js#L148).

Nos gabaris/modèles (templates) sont des fichiers twig, l'idée est de simplement importer ceux-ci en tant qu'objet twig via [cette magie](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/node-twigify.js) et voila.

Vous pouvez voir l'usage [côté client](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/renderToDom.client.spec.js#L39) ou [côté serveur](https://github.com/Mappy/amib/blob/master/renderToString.server.spec.js#L23)

Screenshot avec / sans JS 
URL SEO vs Hash
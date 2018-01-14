Title: Backbone isomorphique maison : comment ?
Date: 2018-01-10
Slug: comment-backbone-isomorphique
Author: Nicolas Bétheuil
Tags: french,JavaScript,NodeJS,Backbone
Summary: Comment a t'on réécrit une librairie isomorphique Backbone maison ?

Cet article fait écho a [Backbone isomorphique maison : pourquoi ?](/pourquoi-backbone-isomorphique.html). Celui ci va présenter comment AMIB a été construit.

La première difficulté était déjà de définir l'attendu. Quel code nous souhaitions écrire. Nous n'avons pas commencé par les tests. Notre objectif était de savoir rapidement si nous étions sur une piste intéressante, pour éventuellement l'abandonner et éviter de gaspiller notre temps.
 
Nous avons donc commencé par écrire :
- [notre première vue](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/fixtures/recursive-children-view/RecursiveChildrenView.js) que nous avons rapidement étoffée 
- pour avoir un modèle et un enfant, 
- puis avec [plusieurs enfant](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/fixtures/multiple-children-view/MultipleChildrenView.js), 
- puis avec un enfant [avec un modèle asynchrone](https://github.com/Mappy/amib/blob/master/fixtures/one-children-with-model/no-children-with-promise-model/NoChildrenWithPromiseModelView.js), c'est à dire un modèle étant une [promesse](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Promise). 

Á l'usage, pour tester en vrai, nous nous sommes rendu compte que Backbone ne s’exécute pas côté NodeJS : la dépendance à jQuery n'y ai pas pour rien. Il suffisait alors de [surcharger/bouchonner les méthodes voulues](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/nodify-backbone.js) et nous pouvions exécuter une vue Backbone côté serveur. L'astuce de la [ré-implémentation de setElement](http://backbonejs.org/docs/backbone.html#section-162) permet d'avoir la même interface de sortie. Ce qui change est comment la vue Backbone renvoyée est [ajouté soit au DOM](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/render.js#L164) soit au [flux de la réponse](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/render.js#L148).

Nos templates sont des fichiers twig, une configuration de NodeJS sur [la manière de charger les fichiers par l'extension](https://github.com/Mappy/amib/blob/master/node-twigify.js) et voila.

Vous pouvez alors voir l'usage [côté client](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/renderToDom.client.spec.js#L39) ou [côté serveur](https://github.com/Mappy/amib/blob/master/renderToString.server.spec.js#L23)


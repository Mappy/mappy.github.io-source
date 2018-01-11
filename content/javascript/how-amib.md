Title: Backbone isomorphique maison : comment ?
Date: 2018-01-10
Slug: comment-backbone-isomorphique
Author: Nicolas Bétheuil, Grégory Paul, Manuel Emeriau
Tags: french,JavaScript,NodeJS,Backbone
Summary: Comment a t'on réécrit une librairie isomorphique Backbone maison ?
Status: draft

Cet article fait écho a [Backbone isomorphique maison : pourquoi ?](/pourquoi-backbone-isomorphique.html) Celui-ci va présenter comment AMIB a été construit.

La première difficulté était déjà de définir l'attendu et le code que nous souhaitions écrire. Nous n'avons pas commencé par les tests contrairement à nos habitudes. Notre objectif était de mesurer rapidement si nous étions sur une piste intéressante, pour éventuellement l'abandonner et éviter de gaspiller notre temps.

Nous savions que les interactions allaient se présenter de cette manière
![première idée](/images/javascript/use-case.png)

Nous avons donc commencé par écrire :

 - [notre première vue](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/fixtures/recursive-children-view/RecursiveChildrenView.js) que nous avons rapidement étoffée 
 - pour avoir un modèle et un enfant, 
 - puis avec [plusieurs enfants](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/fixtures/multiple-children-view/MultipleChildrenView.js), 
 - puis avec un enfant [avec un modèle asynchrone](https://github.com/Mappy/amib/blob/master/fixtures/one-children-with-model/no-children-with-promise-model/NoChildrenWithPromiseModelView.js), on appelle ça une [promesse](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Promise). 

L'intérêt de faire fonctionner ce moteur de rendu avec des modèles asynchrones est très simple : nous consommons des services pour afficher les résolutions d'itinéraire, on utilise pour cela des requêtes HTTP, AJAX côté client & `request` côté serveur. Nous devions donc gérer l'asynchronisme de ces requêtes.
 

La copie d'écran annotée en bleu ci-dessous montre l'imbrication des composants entre eux.
![](/images/javascript/component.png)

Comme Backbone ne fonctionne pas sous NodeJS à cause de sa dépendance avec JQuery (et l'usage du DOM), nous avons [surchargé/bouchonné les méthodes voulues](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/nodify-backbone.js). Nous avons donc pu exécuter une vue Backbone côté serveur. L'astuce de la [ré-implémentation de setElement](http://backbonejs.org/docs/backbone.html#section-162) permet d'avoir la même interface de sortie. La différence porte juste sur la manière de retourner la vue Backbone afin qu'elle soit [ajoutée soit au DOM dans le navigateur](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/render.js#L164) soit [dans la réponse sous NodeJS](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/render.js#L148).

Nos gabaris/modèles (templates) sont des fichiers twig, l'idée est simplement d'importer ceux-ci en tant qu'objet twig via [cette magie](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/node-twigify.js) et voilà.

Vous pouvez voir l'usage [côté client](https://github.com/Mappy/amib/blob/73ac67cb25f336374a03cf26745d99f80667f927/renderToDom.client.spec.js#L39) ou [côté serveur](https://github.com/Mappy/amib/blob/master/renderToString.server.spec.js#L23)

Ci-dessous les exemples de la vraie vie :

[Sans JS : en mode SEO](https://fr.mappy.com/itineraire/paris/lyon)

![Sans JS : en mode SEO](/images/javascript/isomorph-no-js.png.png)

[Avec JS : en mode interaction utilisateur](https://fr.mappy.com/#/13/M2/TItinerary/IFRParis%2075001-75116|TOLyon%2069001-69009|MOvoiture|PRcar|RI0/N151.12061,6.11309,3.59153,47.33409/Z4/)

![Avec JS : en mode interaction utilisateur](/images/javascript/isomorph-w-js.png)

Vous pouvez noter de subtiles différences : l'absence de carte ou de barre de catégories en version SEO.

Comme vous l'avez peut-être compris, nous avons investi un peu de temps dans ce moteur de rendu. C'est une expérience très intéressante qui montre comment, en posant clairement un problème, en le découpant en plus petites cibles atteignables, on peut réussir à contruire quelque chose simple d'usage. 

Les objectifs de ce changement d'architecture étaient multiples : ne pas tout remettre en cause, évoluer sereinement vers une autre structure afin d'atteindre les ambitions stratégiques du produit.
Les changements apportés n'ont ont permis de livrer un code plus stable, plus facile à maintenir, plus testable donc plus couvert (de test unitaire).

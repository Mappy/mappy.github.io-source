Title: Une solution simple pour les A/B test
Date: 2015-12-01
Slug: solution-simple-ab-tests
Author: Mappy
Tags: French,JavaScript,ab,test
Summary: Une solution simple à mettre en oeuvre pour monter son A/B test.


Les A/B tests sont aujourd’hui une pratique courante.

Le principe est de servir une variante (d’un changement de couleur à des écrans complètement différents) pour une fonctionnalité à une partie de son audience et pour une période donnée (par exemple 1 ou 2 semaines).
L’intérêt est ensuite de suivre les métriques (clics, taux de conversion, achats, etc) pour le groupe A (sans variante) et le groupe B (avec la variante).
A l’issue de la période, si les métriques pour la variante sont meilleures que la version normale, on transforme la variante en version par défaut.
Il est tout à fait possible d’avoir plus qu’une variante que l’on partagera entre l’audience totale (33 % pour 2 variantes et le défaut, 25 % pour 3 et le défaut, etc).

Le but des A/B tests est de pouvoir tester ce qui fonctionne le mieux en condition réélle pour améliorer continuellement son produit.

## 1ère version sur mappy.com

Nous avons initialement utilisé un outil externe via l’appel d’un JavaScript externe depuis le site mappy.
L’avantage d’une telle solution est le fait qu’il est possible de créér (via du JavaScript) et de lancer ces A/B test dans mise en production, à chaud.
Le principal inconvénient d’une telle solution est le fait qu’il est difficile de réaliser tous les A/B tests souhaités.
En effet, il est difficile de se brancher sur des appels Ajax ou d’autre comportement et on en revient à "surveiller" des changements sur des éléments DOM.
Cela n’est pas performant et on constate rapidement du "flickering" (version initiale suivi de la variante après quelques millisecondes).


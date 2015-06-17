Title: Mappy.com dorénavant responsive !
Date: 2015-06-15
Slug: mappy-responsive
Author: Mappy
Tags: French,JavaScript,responsive
Summary: Explications du remplacement de 2 sites par un site responsive.

Depuis le mercredi 20 mai, mappy.com propose un site unique et responsive pour tous les navigateurs (bureau ou mobile).
En effet, auparavant, les sites fr.mappy.com, fr-be.mappy.com, nl-be.mappy.com et en.mappy.com étaient dédiés au navigateur de bureau et m.mappy.com dédié au navigateurs mobiles.
Ce billet a pour but de présenter le contexte et notre parcours vers cette décision.

# Historiquement 2 sites

Mappy a mis en ligne mobile en ligne il y a plus de 5 ans.
D’abord via des technologies de type BkRender (pour les téléphones très limités de l’époque), le site a évolué à plusieurs reprises vers une version "HTML5" incorporant une base commune de code avec le site principal (notamment backbone et l’API de cartographie Mappy).

### Réflexion autour du Responsive

Il y a plusieurs mois, une preuve de concept a été réalisé pour déterminer la faisabilité technique d’un site reponsive.

L’approche responsive peut s’effectuer de 2 façons, en partie complémentaire :

  - l’**approche côté client** : le même code est envoyé par le serveur à toutes les navigateurs, qu’ils soit mobiles ou non, et l’affichage des éléments graphiques est conditionné par des `media queries` CSS et des comportements différents éventuellement conditionné par du code JavaScript ;
  - l’**approche côté serveur** : un contenu HTML, CSS et JS différent est envoyé à chaque client en fonction du `User-Agent`.

L’approche côté serveur a l’avantage de pouvoir servir un contenu allégé de façon bien plus simple qu’avec l’approche côté cliente (notamment pour les images). Cependant, elle a l’énorme inconvénient de servir un contenu différent en fonction du `User-Agent`, pratique dangereuse en cas de `reverse-proxy` (à moins d’ajouter un entête `Vary: User-Agent` qui rend l’utilisation d’un reverse-proxy caduque). Enfin, il est assez compliqué de déterminer si le navigateur est un téléphone ou une tablette, surtout lorsque certains navigateurs disent qu’ils sont un iPhone, un Android et Windows Phone comme [Windows Phone 8.1](https://msdn.microsoft.com/en-us/library/hh869301%28v=vs.85%29.aspx#code-snippet-11).

L’approche cliente n’a pas ses inconvénients puisque le même contenu est servi à tous mais il est plus difficile de charger un contenu allégé en fonction du navigateur.

### Processus

Le principal avantage est d’éviter le développement des histoires utilisateurs (User Stories) en double, à la fois sur le site principal puis sur le site mobile. En plus du développement, un ensemble de tâches et d’opérations annexes effectuées sur chacun de nos produits sont éliminés en supprimant un produit (tests, correction de jira, déploiements, maintenance des serveurs, etc).

Un autre avantage est le fait qu’une nouvelle histoire utilisateur impactera en même temps l’audience fixe et mobile.
Auparavant, il arrivait que certaines fonctionnalités soit d’abord réalisé sur le site fixe, puis quelques itérations suviantes sur le site mobile.

Enfin, étant donné que le site fr.mappy.com est le même site que les versions étrangères, le passage au "responsive" permet aux versions étrangères de bénéficier directement d’une version mobile.

Il n’y a pas de réel inconvénient par rapport à ce changement mais quelques points de vigilance.
En effet, chaque fonctionnalité est maintenant testé sur plus de support qu’auparavant.
Par ailleurs, lors de la conception, certains points doivent être pris en compte (conception sur petit et grand écran, gestion du touch, image en haute définition, etc).
Enfin, certaines fonctionnalités sont différentes entre le fixe et le mobile. L’itinéraire sur mobile par exemple, présente un écran affichant le sommaire de la feuille de route, écran inexistant sur la version fixe.

### Implémentation

L’implémentation du site "responsive" s’effectue principalement via des "[CSS media queries](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Media_queries?redirectlocale=en-US&redirectslug=CSS%2FMedia_queries)". 3 "breakpoints" principaux ont été défini pour les petits écrans (par exemple les téléphones en portrait/paysage et tablette en portrait), les écrans moyens (par exemple les tablettes en mode paysage) et les grands écrans (toutes les plus grandes définitions).

Une grande partie de nos icônes utilise une police de caractère spéciale (à la manière de [Font Awesome](https://fortawesome.github.io/Font-Awesome/icons/)), permettant de s’abstraire d’une version normale et haute densité de pixel ("retina"). Attention, cette technique n’est utilisable que pour les icônes d’une seule couleur (comme pour nos icônes de catégories).

Certains cas nécessitent l’utilisation de JavaScript pour adapter le comportement à la cible (notamment le choix des emplacements publicitaires à afficher ou les différences de comportement entre les périphèriques).
Néanmoins, la majorité des cas ne concerne que des adatations au niveau des CSS.

### Tests

Afin d’avoir un feedback rapide lors de nos développements mais également pour faciliter les tests manuels, nous avons opté pour quelques supports de téléphones ou tablettes de type "[devicelab](http://devicelab.vanamco.com/" couplé à [GhostLab](http://vanamco.com/ghostlab/).
Enfin, nos tests Selenium sont en cours d’évolution puisqu’il est nécessaire de les lancer sous 2 formats (grand et petit écran).

### Conclusion

Le passage au site "responsive" s’est passé sans accroc.
Les bénéfices portent leur fruit puisque les nouvelles User Stories seront accessibles pour toutes les formats en même temps

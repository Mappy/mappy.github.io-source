Title: Mappy.com dorénavant responsive !
Date: 2015-05-22
Slug: mappy-responsive
Author: Mappy
Tags: French,JavaScript,responsive
Summary: TODO TODO TODO

Depuis le mercredi 20 mai, mappy.com propose un unique site pour tous les navigateurs de bureau ou mobile, au lieu de 2 sites dont un dédiée au mobile comme auparavant. L’approche de type "responsive design" a été rétenue.
Ce billet a pour but de présenter notre contexte et notre parcours vers cette décision.

# Historiquement 2 sites

Mappy a mis en ligne une version mobile de ces services via un site mobile il y a plus de 5 ans.
D’abord via des technologies de type BkRender (pour les téléphones très limités de l’époque), le site a évolué à plusieurs reprises vers une version "HTML5" incorporant une base commune de code avec le site principal (notamment backbone et l’api de cartographie Mappy).

### Réflexion autour du Responsive

C’est après plusieurs mois de maturation et après avoir validé une preuve de concept sur l’adaptation du site principal au "responsive" que la décision de ne servir qu’un unique site a été prise.

Le principal avantage est d’éviter le développement des histoires utilisateurs (User Stories) en double, à la fois sur le site principal puis sur le site mobile. En plus du développement, un ensemble de tâches et d’opérations annexes effectués sur chacun de nos produits sont éliminés en supprimant un produit (tests, correction de jira, déploiements, maintenance des serveurs, etc).

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

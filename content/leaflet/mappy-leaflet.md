Title: mappy.com migre vers Leaflet
Date: 2015-01-22
Slug: mappy-com-migre-vers-leaflet
Authors: Michael Cellier, Grégory Paul
Tags: Leaflet,OpenSource,French,JavaScript
Summary: mappy.com utilise dorénavant l’API OpenSource Leaflet plutôt que son API cartographique “maison”.

# Nouvelle version du site, nouvelle cartographie

En mai 2014, une nouvelle version du site Mappy a vu le jour :

![Version 4](images/leaflet/hp-v4.png)

   Précédente version (4)

![Version 5](images/leaflet/hp-v5.png)

   Nouvelle version (5)


Cette version a entraîné bon nombre de refactoring technique (dont un passage à Backbone par exemple) mais la plus impactante fût la décision de remplacer l’API cartographique JavaScript historique, permettant de manipuler la carte sur le site, par [Leaflet](http://leafletjs.com/).

Leaflet est une API de cartographie JavaScript OpenSource parmis les plus connues et actives. Utilisée par de nombreux sites importants, aussi bien généralistes (Flickr, Foursquare, Pinterest) que spécialistes de la cartographie (Mapbox, OpenStreetMap), elle dispose de plus de 175 contributeurs.

## La compatibilité de la cartographie Mappy avec Leaflet

Notre plateforme cartographique dispose de certaines spécificités par rapport aux standards actuels :

   - une projection [Gall](http://spatialreference.org/ref/esri/world-gall-stereographic/),
   - des tuiles de 384 pixels de large (au lieu des 256 généralement utilisés par les autres acteurs cartographique),
   - 13 niveaux de zoom, avec un facteur 3 entre chaque niveau (au lieu de 20 niveaux et d'un facteur x2).

Elles ont été intégrés sous la forme d’un plugin Leaflet, inspiré du plugin [Mapbox](https://www.mapbox.com/developers/api/). Ce plugin étend l’API Leaflet et intégre également d’autres méthodes pour effectuer des recherches géographiques, des recherches géographiques inversés (quel est le lieu pour telle latitude / longitude ?) et enfin des recherches d’itinéraires via les services de Mappy.

Utilisée aujourd’hui par le site [fixe](http://www.mappy.com), le site [mobile](http://m.mappy.com) et le [widget](http://widgets.mappy.com/map/documentation), cette API est également distribuée aux partenaires. Si vous êtes intéressés, je vous invite à consulter [la page dédiée à intégration de nos services dans vos produits](http://corporate.mappy.com/faq/integrez-mappy/).

## Contributions

Depuis cette migration à Leaflet, nous avons apporté quelques contributions sous la forme de “[pull request](https://github.com/Leaflet/Leaflet/pull/3038)” ou de nouveau plugin ([leaflet-active-area](https://github.com/Mappy/Leaflet-active-area), un prochain article le présentera en détail).

## A l’avenir

Au final, ce passage à Leaflet ne nous apporte que des avantages et nous avons hâte de proposer d’autres “pull requests” ou plugins.

Autre avantage à l'utilisation de Leaflet, la migration vers des projections plus standard - un de nos projet 2015 - aura un très faible coût, et aucune migration d'API ne sera nécessaire.

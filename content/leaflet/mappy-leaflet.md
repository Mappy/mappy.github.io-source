Title: mappy.com migre vers Leaflet
Date: 2014-05-13
Slug: mappy-com-migre-vers-leaflet
Author: Mappy
Tags: Leaflet,OpenSource,French,JavaScript
Summary: mappy.com utilise dorénavant l’API OpenSource Leaflet plutôt que son API cartographique “maison”.

# Une nouvelle version du site, avec Leaflet

En mai 2014, une nouvelle version du site Mappy a vu le jour.

Cette version a entraîné bon nombre de refactoring technique (dont un passage à Backbone par exemple) mais la plus impactante fût la décision de remplacer l’API cartographique JavaScript historique, permettant de manipuler la carte sur le site, par [Leaflet](http://leafletjs.com/).

Leaflet est une l’une des API de cartographie JavaScript OpenSource la plus connue et active.

Cette migration a donc été naturelle.

Plus exactement, c’est une surcouche à l’API Leaflet qui a été développée, permettant de pré-configurer différents services, comme l’utilisation des tuiles (images carrés les unes à côté des autres permettant de dessiner la carte) Mappy ainsi que les services de localisation et d’itinéraires.

Cette API est donc utilisé aujourd’hui par le site [fixe](http://www.mappy.com), le site [mobile](http://m.mappy.com) ainsi que le [widget](http://widgets.mappy.com/map/documentation).

Cette API est d’ailleurs distribuée aux partenaires. Je vous invite à consulter cette page sur l’[intégration de nos services dans vos produits](http://corporate.mappy.com/faq/integrez-mappy/) si elle vous intéresse.

# La compatibilité de la cartographie Mappy avec Leaflet

Afin de rendre utilisable et plus facilement accessible la cartographie Mappy à nos utilisateurs, nous avons développé un plugin Leaflet, inspiré du plugin [Mapbox](https://www.mapbox.com).

Notre plateforme cartographique disposant de certaines spécificités par rapport aux standards actuels, il a fallut intégrer quelques spécificités : 
- une projection [Gall](http://spatialreference.org/ref/esri/world-gall-stereographic/)
- des tuiles de 384 pixels de large (au lieu des 256 généralement utilisés par les autres acteurs cartographique)
- 13 niveaux de zoom, avec un facteur 3 entre chaque niveau (au lieu de 20 niveaux et d'un facteur x2)

Autre avantage à l'utilisation de Leaflet, la migration vers des projections plus standard aura un très faible coût, et aucune migration d'API ne sera nécessaire. 


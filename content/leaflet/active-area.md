Title: Un plugin Leaflet pour le site Mappy (Leaflet-active-area)
Date: 2015-01-13
Slug: leaflet-active-area
Author: Mappy
Tags: Leaflet,OpenSource,French
Summary: Ce plugin leaflet permet de définir une zone utile où seront placé marqueurs et tracé n’occupant qu’une partie de la carte.

# Un plugin Leaflet pour le site mappy.com

### Une nouvelle version du site, avec Leaflet

En mai 2014, une nouvelle version du site Mappy a vu le jour.

Cette mise à jour du site a permis de remplacer l’API JavaScript de cartographie, historiquement "maison", par une nouvelle API bâtie sur Leaflet.
Cette API est d’ailleurs distribuée, confère la page sur l’[intégration de nos services dans vos produits](http://corporate.mappy.com/faq/integrez-mappy/).

### Mise en avant de la carte

L’un des objectifs de cette version fût de mettre en avant la carte dans l’interface (elle n’occupait qu’une petite partie de l’interface de la version précédente). Ainsi, sur les pages de fiche POI ou sur la feuille de route, la carte occupe tout l’écran, du haut en bas de l’écran.

Cela est surtout visible sur les grandes résolutions, où chaque bord laisse place à la carte comme le témoigne les captures d’écran suivantes :

![Itinéraire](images/leaflet-active-area/iti.png)

   [Feuille de route d’un itinéraire](http://fr.mappy.com/itineraire/Paris%2075001%20-%2075116/Vincennes%2094300?opt.vehicle=midcar&opt.cost=time&opt.notoll=0&opt.infotraffic=0&opt.gascost=1.558&opt.gas=petrol&opt.compensation=0&routeidx=0)

![Fiche POI](images/leaflet-active-area/poi.png)

   [Fiche POI](http://fr.mappy.com/poi/51f0bde784aebbc34d4a0cc7)

Comme vous pouvez le voir sur les images ci-dessus et comme la carte occupe presque tout l’écran, le marqueur ou l’itinéraire de la carte n’y sont pas centrés. Le centre de la carte est au centre de l’écran, caché derrière les éléments HTML.
Cela est plus visible lorsque l’on rend transparent ces éléments HTML comme le montrent les images suivantes :

![Itinéraire avec fond transparent](images/leaflet-active-area/iti-transparent.png)

   [Feuille de route d’un itinéraire avec fond transparent](http://fr.mappy.com/itineraire/Paris%2075001%20-%2075116/Vincennes%2094300?opt.vehicle=midcar&opt.cost=time&opt.notoll=0&opt.infotraffic=0&opt.gascost=1.558&opt.gas=petrol&opt.compensation=0&routeidx=0)

![Fiche POI avec fond transparent](images/leaflet-active-area/poi-transparent.png)

   [Fiche POI avec fond transparent](http://fr.mappy.com/poi/51f0bde784aebbc34d4a0cc7)

Les appels à l’API Leaflet (centrage de la carte, centrage de la vue en fonction de marqueurs, d’un itinéraire) vont naturellement avoir pour centre de la carte le centre de l’écran si celle-ci en occupe la quasi-totalité.


### Le plugin Leaflet-active-area

Afin de pouvoir afficher des marqueurs ou un itinéaire de façon décentrée, nous avons développé un plugin Leaflet pour abstraire ce comportement.

Il s’agit du plugin [Leaflet-active-area](https://github.com/Mappy/Leaflet-active-area) qui, comme le montre la [page d’exemple](http://techblog.mappy.com/Leaflet-active-area/examples/index.html), permet d’appeler les méthodes usuelles de Leaflet telles que setView, setZoom, fitBounds tout en "centrant" la carte à partir d’une autre zone.

Le principe est de définir une classe CSS, positionnée de façon absolue, qui sera pris en compte comme zone active de la carte. Ainsi, le centre de la carte sera le centre de cette zone et l’ensemble des marqueurs ou tracés y seront placés.

Le plugin est disponible sur [github](https://github.com/Mappy/Leaflet-active-area) et listé sous [“Other Plugins and Libraries”](http://leafletjs.com/plugins.html#other-plugins-and-libraries) du site leaflet.


Title: State of The Map France 2018: Mappy y était
slug: sotmfr2018-mappy
Date: 2018-06-08
Tags: opensource,sotm,osm
Status: draft

Nous avons été 6 Mappy à avoir la chance d'aller à State Of The Map France 2018 près de Bordeaux, à Pessac.

<img src="//sotm2018.openstreetmap.fr/images/sotm2018_website2.png" width="400">

Ci dessous le compte-rendu rédigé conjointement par les différents participants

# Map Contrib Next

## Fonctionnalité principale
Pouvoir éditer une carte en se fixant un thème (et éventuellement un territoire) précis.

Les organisateurs de la cartoparty ont un accès utilisateur avancé, les autres participants une interface simplifiée et agréable.

## Stack
 - ReactJS
 - OSM request (Utiliser par Pic4Review)
 - Osmose Request
 - [leaflet nectarivore](https://github.com/osmlab/leaflet-nectarivore)
   - permet d'intégrer facilement de la donnée de différentes API dans une carte leaflet
 - OSM UI
   - Une liste de composants UI, spécifique à l'édition OSM (un peu comme un bootstrap OSM ?).

## Démo

[http://next.mapcontrib.xyz](http://next.mapcontrib.xyz)

## Feuille de route
 - visualiser les thèmes v1 + implémentation de fonctionnalités de la v1
 - filtre/recherche parmis les données affichées
 - interface légère + interface avancée (bien longtemps dans le futur)

# Carto Participative

[umap](https://umap.openstreetmap.fr/en/map/new-data_1#12/51.7878/7.6717) plutôt que JOSM ou même ID Editor.

# OSM Togo

Communauté active, qui montre la puissance d'OSM face à des acteurs étatiques / multinationales, même quand les photos aériennes sont de mauvaise qualité.

![](/images/sokode_google.png) ![](/images/sokode_osm.png)

# La donnée cyclable

## Cartographie

### 8 ans de géovélo

- En 6 carto party, les 4 principales communes de Tours ont été cartographié
- faciliter la contribution des utilisateurs
    - remonter vers Géovélo (sans compte OSM) qui va le remonter vers OSM
- De cuisinier à géomaticien/géographe :)

[replay](https://peertube.openstreetmap.fr/videos/watch/5e6cadd3-eca1-4537-a743-461a792c189f)
[présentation](https://fr.slideshare.net/cartocite/acquisition-et-maintenance-des-donnes-vlo-sur-openstreetmap)

## Itinéraire
 - piste cyclable en Hollande autorisées au scooter mais modélisées de la même façon dans OSM.

## Les vélos routes dans OSM
Les vélos routes sont à la fois des itinéraires touristiques définis (La Loire à Vélo) et des euro-véloroutes également reconnus (eurovélo 6).

### Le problème de la "supra-relation"
En pratique les tronçons cyclables sont tous attachés à une même et unique relation (ex : EV6) qui peut faire des centaines de km de long. La préconisation est d'éviter ce genre de supra-relation. Récemment par exemple deux contributeurs ont voulu l'éditer en même temps…

### Comment découper cette supra-relation alors ?

La solution "rationnelle" :

- Couper tous les x kilomètres
- Couper par niveaux administratifs (ex les départements)
- La solution "touristique" :
     - Couper par étape-relais
     - Plus logique pour les contributeurs et les utilisateurs mais pose des problèmes lorsque ces étapes ne sont pas clairement définies dans certaines zones, ou différentes selon le réferentiel européen et régional. Actuellement cette solution est plutôt utilisée en pratique.

Distinguer l'importance de la voie et l'importance du tronçon cyclable.

Faire attention à la distinction primaire/secondaire etc qui correspond à l'importance de la voie routière sur l'ensemble du réseau routier, et la distinction locale/nationale/internationale qui correspond à l'importance de ce passage cyclable dans l'ensemble du réseau véloroute.

### Comment cartographier les liaisons non principales joignant les villes, les liaisons principales, les variantes ?

Une véloroute se compose de liaison la raccrochant aux villes importantes proches, mais aussi de variantes.

Il faut trouver un tag pour qualifier les tronçons / les relations en distinguant les trois types de possibilités.

### Une relation en chantier pour 1 tronçon ??

Aujourd'hui si un élément de la relation est "en projet" la totalité de la relation l'est. Il faudrait enlever ce statut de la relation.

## Les aménagements dans OSM : entre réalité et législation

Les aménagements cyclables sont en théorie facile à cartographier : la législation est claire et précise.

Sauf que dans la réalité, des zones grises apparaissent :

- comment cartographier un aménagement séparé de la route par un grand zébra (bande ou piste?)
- doit on cartographier un aménagement cyclable qui n'est plus utilisé en réalité, ou devenu dangereux ?
- la distinction entre "path" et "footway" est impactant pour l'itinéraire vélo mais repose sur des critères flous
(nature vs urbain ?)

Globalement des choix qui vont différer selon l'objectif final : calculer un itinéraire, faire un état des lieux de l'existant, dénoncer ou souligner la qualité de la couverture cyclable, etc.

#La donnée Transport en commun

##Jungle bus

Constat d'origine : plus de 60% de villes dans le monde n'ont pas de plans de transport public, ni de données exploitables. En gros : il y a des bus, il y a des lignes mais rien d'exploitable en version numérique pour représenter, manipuler, planifier, distribuer cette information. 2% des lignes / arrêts évoluent pour les bus contrairement au métro / tram où les infrasctructures sont plus lourde. Correctement cartographié pour correctement informer est nécessaire.

[Un blog avec plein de tuto](https://nlehuby.5apps.com/) (extraction, visualisation de la donnée).

L'application Jungle Bus :

- une application android
- avec des tuiles vectorielles de Jawgs personnalisées aux couleurs jungle bus
- affichant les infrastructures des bus (lignes, arrêts)
- traduite en six langues
- présente sur le monde entier

L'utilisateur peut ainsi visualiser le réseau de bus, avec la position des arrêts et leurs noms notamment.

Mais il peut aussi éditer cette donnée pour corriger une position erronée ou renseigner des noms manquants.

Cette année, ils ont introduit plusieurs nouveaux outils :

- un chatbot pour modifier encore plus facilement la donnée
- une interface web qui met en évidence les erreurs à corriger, par type d'erreur : [BIFIDUS](https://jungle-bus.github.io/bifidus/#12/48.851/2.3784)
- une interface web qui met en évidence un écart de position ou de nom avec d'autres données TC opendata : VARICELLE
- la possibilité d'exporter la donnée OSM produite au format GTFS via osm2gtfs (voir point suivant)

Ils ont signé en 2018 un partenariat avec un groupement d'acteurs importants de la mobilité en IDF afin de mettre à jour la data (IDF Mobilités, fabrique des mobilités, naviatia, etc.)

Ce travail concerne 1500 lignes et 40 000 arrêts. Il est conséquent, c'est pourquoi ils ont mis en place un protocole à reproduire pour toute autre demande semblable par la suite :

1. Faire un diagnostic qualité de la donnée existante en comparant la donnée OSM et la donnée "référentielle". Dans cet audit, la position des arrêts OSM et référentiel est comparée, ainsi que leur donnée attributaire, sur une grille d'1 km x 1 km. En moyenne, 80% des arrêts OSM ont le même nom que dans la réferentiel et 75% des arrêts OSM sont à moins de 20 m des arrêts de référence
2. Ce travail a permis de mettre en évidence des zones en IDF possédant une donnée de faible qualité. Suite à cela des mapathons sur ces zones ont permis/permettront de redresser la qualité
3. Choisir un mode de gouvernance pour la communauté d'acteurs
4. Choisir des outils pouvant s'inclure aisément aux SI existants
5. S'assurer de la pérennité de la donnée et de l'industrialisation possible de son utilisation
6. Communiquer (dataviz, etc.) à destination des acteurs insitutionnels


## osmtogtfs

Cet outil permet de transformer les données géographiques (Arrêts, Lignes, nom..) à partir d'un fichier ou d'une url dans un format GTFS le format standard du transport en commun.

Ex au Nicaragua de la collecte de données à l'application de transport.

- [osmtogtfs](https://github.com/hiposfer/osmtogtfs) permet de créer un fichier GTFS de la donnée osm, le code permettrait d'adapter la transformation au contexte local
- Ils ont rajouté les informations d'horaires du transporteur local depuis un fichier .json (OSM collecte rarement des données chaudes c'est un sujet en discussion pour les horaires TC)
- Ils ont matché les données OSM ([validé via le plugin de josm](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/PT_Assistant)) et celles du transporteur par les noms des arrêts & lignes (pas d'id commun) et ont validé la donnée avec GTFS Feed Validator
- L'application utilisé pour la navigation TC [transportr github](https://github.com/grote/Transportr) [transportr](https://transportr.grobox.de/)
- Un autre outil mentionné dans une autre présentation [opentripplanner](http://www.opentripplanner.org/) avec calcul d'itinéraire piéton, voiture et TC voir de l'intermodal

# La donnée piéton
## Cartographier les déplacements en gares par SNCF et Carto cité

Produire des plans de déplacements piéton autour des gares : quelles questions se posent ?

Une difficulté : beaucoup d'objets sont représentés par des points (ascenseur) ou des lignes (escaliers) alors qu'ils représentent des espaces importants (escalier de plusieurs mètres de large), encombrants et non franchissables (cage d'ascenseur au milieu d'une plateforme).

Un critère pour mesure l'accessibilité d'un escalier : le nombre de marche.

Une information importante pour les déplacements dans une direction de donnée : le sens d'ouverture des portes à sens unique.

Des repères pratiques pour les voyageurs : les bâtiments remarquables, ponts, fontaines… enrichir OSM avec !

11 gares SNCF bretonnes ont été cartographiées avec précision par carto cité à partir d'images géolocalisées. Avec ces images les objets sont dessinés et renseignés sur JOSM afin d'être intégrés à OSM. Ensuite, la donnée OSM est traitée dans QGIS avec un style graphique SNCF puis sur Inskape afin de produire des cartes finales à destination des voyageurs.

Pour 11 gares :

- 1 semaine de terrain
- 3 semaines de JOSM
- 1 semaine de traitement final
- A priori 2 personnes

## Amélioration de l'itinéraire piéton au niveau d'une ville par Makina Corpus (Frederic Boniface)
- Arrivée du bon coté de la route
- Utilisation des landuse pour influencer le profil des vitesses (en l'absence de données traffic)
- La vitesse de chaque tronçon est pondérée en fonction du profil d'environnement dans lequel il s'inscrit : nature, urbain.
- Ces profils sont générés sous la forme de carroyage en amont, par croisement de plusieurs informations notamment les landuse/landcover.
- Un algorithme calcule la possibilité de traverser une place plus rapidement qu'en suivant ses contours, technique utilisée en général.
- OSM -&gt; traitement (création d'arrêtes pour traverser les places) -&gt; génération pbf + OSRM
- Croisement avec un MNT OSTRM afin d'exploiter l'information de dénivellé et pondérer la vitesse de marche en fonction de cette dénivellation. <br>
 - <a href="https://en.wikipedia.org/wiki/Tobler%27s_hiking_function">Tobler's hiking function</a> (temps de parcours en fonction de la pente)
- Pondération moindre lorsque le trajet emprunte un tronçon de trottoir et non de voie. Le temps de trajet en revanche ne doit pas être modifié. Cette donnée est encore trop partielle cependant.
 Possibilité de calculer des itinéraires "thématiques" du type "une balade culturelle". Des tuiles vectorielles T-rex sont prégénérées avec un filtre sur les éléments choisis : objets naturels, objets culturels etc. Les centroides de ces objets sont calculés, regroupés en cluster par distance.Puis un trajet reliant tous les points est calculé avec une direction donnée.
- Une autre possibilité mentionnée serait d'utiliser les données CORINE Land Cover (CLC)
- Rien sur comment traverser quand il n'y a pas de passage piéton

# La donnée routière / traffic

## Développement de la navigation chez Mapbox

Equipe dédiée au trafic chez Mapbox.

La constitution de la donnée trafic  à partir des traces GPS des utilisateurs :
- suppression de l'origine et de la destination de la trace
- tronconnement de la trace
- mélange de toute les traces sur un tronçon
- Ils ont des modèles pour qualifier la donnée GPS (Cycliste, Voiture..)

A la fin, on a une donnée sur la charge de trafic du tronçon sans avoir aucune information individuelle sur les traces de départs, totalement anonymisées.

### Algorithmes mentionnés
- En plus des contractions hiérarchiques
- [MultiLevel Dijkstra (mld)](https://github.com/Project-OSRM/osrm-backend/issues/4797)
pour réduire la complexite (utilisation pour l'intégration du temps réel
- Valhalla de mapzen repris par mapbox

### La cartographie du trafic

Un style de carte et des instructions de type feuille de route ont été créée.

La navigation est gérée en hors ligne.

### Identifier des points d'amélioration

Une carte des points d'instruction manquées, rassemblés en groupe, permet de voir les endroits où il y a clairement un problème : la donnée n'est peut être pas la même en réalité (on ne peut pas tourner à ce carrefour) ou l'instruction arrive trop tard / n'est pas comprise !

## L'initiative OpenTraffic porter par la world bank

[présentation](https://www.slideshare.net/FredericRodrigo/open-traffic)

- Une [archi](http://opentraffic.io/)
- besoin de data (faire une app ?)
- une [ML](https://listes.openstreetmap.fr/wws/info/opentraffic)
- https://github.com/opentraffic/osmlr un outil pour associer le trafic au réseau routier
- Une autre piste: https://sharedstreets.io/

# Cosmogony / Qwant

[Présentation](https://nextcloud.openstreetmap.fr/index.php/s/mZl1S5P4Rvx0tR9/download?path=%2F&amp;files=19_Cosmogony_QwantResearch.pdf)

Le but de Cosmogony est de reconstruire les relations d'inclusion entre les niveaux administratifs.

Pour se faire

- Reconstruit les géométries OSM (ne passe pas par imposm3)
    - [cosmogony.world](http://cosmogony.world/#/11.21/0.17/48.91)
    - [relation/3316328](https://www.openstreetmap.org/relation/3316328#map=14/48.9019/0.0748)
- Se base sur libpostal pour déterminer le mapping admin_level hiérarchie
    - [libpostal](https://github.com/openvenues/libpostal/blob/master/resources/boundaries/osm/de.yaml)
    - le fichier de config permet de spécifier les hiérarchies administratives dans certains pays (par exemple Berlin = ville-état en Allemagne)
- Bilan partiel
     - bonne courverture sur le 1er niveau administratif de chaque pays
     - résultat peu satisfaisant pour la zone hors Europe
- Remarque: la hiérarchie administrative en Europe a été faite dans le cadre du projet Inspire

Format de sortie : geojson

L'outil de visualisation intéressant (peut être lent en fonction de la donnée affichée)

# API Overpass
```
/*
This is an example Overpass query.
Try it out by pressing the Run button above!
You can find more examples with the Load tool.
*/
relation
[admin_level~"[4-8]"]
/*BBOX Saint Pierre et Miquelon*/
(46.679123371552315,-56.715545654296875,47.17197772313465,-56.01585388183594);
/*added by auto repair*/
node[place](r);
/*end of auto repair*/
out;
```
https://overpass-turbo.eu/

API destiné au&nbsp;**data consumers** comparable à SparkQL d’un point de vue carto.

ex de requête : “tous les bars à moins de 200 m d’une station de métro”, “trouve moi les nœuds communs à une route et une voie ferré”.

OverPass Turbo sur une ville OK, à l’échelle départementale ça commence à être limite.

Inconvénient (?) : apprendre le langage OverPass QL (ou faire des requêtes sans vraiment comprendre le langage).



# Évaluer la qualité de la donnée OSM à partir de l'historique des contributions ?

L’évaluation de la qualité des données se fait &nbsp;par l’identification et la classification non supervisée (sans connaissance a priori) des profils des contributeurs en fonction de leur niveau. Oslandia utilise des algorithmes de machine learning (K-means notamment) pour obtenir des clusters de contributeurs tels que&nbsp;: expert local, intermédiaire irrégulier, novice, contribution unique…

Ils utilisent les fichiers d'historique <code>osh.pbf </code>une des possibilités d'importer ce fichier est [OpenStreetMap History Renderer & Tools](https://github.com/MaZderMind/osm-history-renderer) 

Ils définissent eux-mêmes le nombre de classes (après une analyse en composante principale) et la nomenclature des classes.

<u>Spécification locale</u>: L’étude est faite à l’échelle locale, ainsi un contributeur régulier et expérimenté à Strasbourg pourra être identifié comme novice à Bordeaux (et vice versa, un nouveau contributeur qui a agit plusieurs fois à Bordeaux sera perçu comme expert local).

Ils s’intéressent également aux tags les plus souvent modifiés, études qu’ils associent avec la classification des profils. (Sous entendu, une modification d’un expert &gt; une modification d’un novice).

<u>Langage de programmation</u>&nbsp;: Python

[dépôt github](https://github.com/Oslandia/osm-data-classification) 

Une des conclusions, il y a population écrasante de faibles contributeurs, les 2, 5% restants traitent 80% de la donnée.

# Carto humanitaire

CaribeWave est une opération de sensibilisation à la vulnérabilité des populations (notamment insulaires) face à des catastrophes naturelles (ouragans, tsunami…). &nbsp;Présentation de cas concrets de situations (Irma/Maria) pour mettre en avant les besoins et les risques. Ce sont des évènements cycliques, il faut donc se préparer pour les futures catastrophes naturelles. L’association HAND (Hackers Against Natural Disasters)&nbsp; créée par Gaël MUSQUET rassemble des technophiles pour faire de la cartographie en urgence notamment grâce à l’imagerie aérienne par drone.

# L'usage d'OSM dans les pays du sud

Retour d'expérience avec Haïti ou Madagascar.

Il est difficile de construire des communautés qui durent : les gens sont habitués à être aidé et à venir pour une compensation (argent pour mapper / nourriture pour une formation à la journée).

Le simple fait de se déplacer pour venir à une formation est déjà compliqué: ça coûte et ce n'est clairement pas une priorité dans des pays où ils sont en mode survie.

L'usage des tags OSM est loin d'être évident dans des pays où la route principale, nationale est une piste régulièrement inondées avec des ornières de 1m. Depuis SOTM, il y a des échanges sur la ML talk-fr: l'usage/praticabilité est dissociée de l'information principale / secondaire avec d'autres infos comme le revêtement. En France, les arrêts de bus changent, là bas, ce sont les ponts, les routes qui peuvent avoir changer après une averse.

[cartong](http://www.cartong.org)
[mapathon-missing-maps](http://www.magellium.com/fr/blog/mapathon-missing-maps-2/)

# Contribuer

## Contribuer à Mapillary quand on est une entreprise, pourquoi ? Comment ?

SOGEFI contribue à Mapillary (plateforme collaborative d’imagerie street-level) avec l’équipement Imajbox de la société Imajing (système de capture d’image autonome qui peut se fixer sur voiture, camion, vélo, moto, train…).

Créer des bases de données d’images de la voierie (panneaux de signalisations, panneaux publicitaires…) localisées. Près de 10&nbsp;000&nbsp;000 images versées à Mapillary et plus de 30&nbsp;000 km de routes couvertes.

Pour réaliser les traitements d’images, SOGEFI utilise la suite logicielle de photogrammétrie Imajview.

- SOGEFI est le 1er contributeur à Mapillary
- Cette contribution est financée par la TLPE(Taxe Locale sur la Publicité Extérieure). A partir des images collectées, SOGEFI construit une base des affiches publicitaires par entreprise et la remet aux collectivités territoriales.&nbsp; Ces dernières peuvent récupérer la TLPE auprès des entreprises. Une partie de cette taxe permet de payer le service fourni par SOGEFI
- Suite à l'acquisition d'une caméra Insta 360 Prop, SOGEFI est agréé Google (Google Street View Trusted)
## Osmose-QA &amp; Validation commune avec JOSM

[osmose](http://osmose.openstreetmap.fr/) est un outil qui remonte les possibles anomalies sur une carte

Important travail fait pour rendre compatible les règles OSM avec JOSM et les styles&nbsp;[MapCSS](https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation) de JOSM avec Osmose.

Nouvelles fonctionnalités développées: par exemple la similarité de noms entre tronçons proches (rue Lacavé vs rue Lacabé) qui peut être une erreur.

Des warnings à partir de l'opendata sur des suggestion d'intégration.

[présentation](https://www.slideshare.net/FredericRodrigo/osmoseqa-qualit-et-intgration-de-donnes): 

Des jobs qui calculent les erreurs d'utilisation des tags à partir du planet, 2j pour traiter la donnée.

## Mapillary

La contribution / mapping en mode DIY.

Plusieurs présentations sur l'usage du balai de ménager comme monopode pour une [caméra 360](http://www.lg.com/fr/lg-friends/lg-360-CAM-lgr105).

Une perche de 12m pour faire des photos de monuments [exemple](https://www.mapillary.com/app/?lat=44.13803467000835&amp;lng=4.807303570051661&amp;z=17&amp;focus=photo&amp;pKey=ACrothbK7L1N0ZC4RmuAfA&amp;x=0.922026890521998&amp;y=0.4961013356349145&amp;zoom=0) [exemple](https://www.mapillary.com/app/user/zimmy?lat=44.141960833333314&amp;lng=4.804816944444383&amp;z=19.787149667364208&amp;focus=photo&amp;pKey=nzGRo2UFUGt3ZUY4KbyR5Q&amp;x=0.5920152535621718&amp;y=0.44476900377692474&amp;zoom=0&amp;username%5B%5D=zimmy).

La bonne tenue du smartphone et la scénarisation pour faire de bonnes séquences.

Comment utiliser mapillary pour l'acquisition à pied, à vélo, puis en voiture mapillary.

Le mat DIY qui tient bien mais bouge quand même au mistral.

![](https://farm2.staticflickr.com/1753/28655417828_cbbf46720d_h.jpg) ![](/images/28655417828_cbbf46720d_h.jpg)

## v4mbike
[stfmani](https://twitter.com/stfmani)

Un mat mis sur un vélo avec 1 raspberry, 4 action cam, arduino, gps … pleins d'électronique, photo 360 et un soft à fiabiliser.

<blockquote class="twitter-tweet" data-lang="fr"><p lang="fr" dir="ltr">Le nouveau <a href="https://twitter.com/hashtag/V4MBike?src=hash&amp;ref_src=twsrc%5Etfw">#V4MBike</a> est dans la place !! <a href="https://t.co/B9q534qSsh">pic.twitter.com/B9q534qSsh</a></p>&mdash; Stéphane Péneau (@stfmani) <a href="https://twitter.com/stfmani/status/1001130741978234881?ref_src=twsrc%5Etfw">28 mai 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## L'usage d'OSM pour une office du tourisme

La communauté de commune de [seignanx](https://seignanx.carto.guide/).

Le croisement entre des infos éditoriales des OT et la DB OSM.


# Le train
- [signal.eu.org](https://signal.eu.org/osm/)
- [openrailwaymap](https://www.openrailwaymap.org)
- [pkfieur](https://pkfieur.gares.io/)

# Découverte d'outils basés sur OSM
- [pic4review](http://pic4review.pavie.info/): bugfix sur photo, gamification, overpass, osmose
- [maproulette](http://maproulette.org/) : bugfix à partir de photo
- [VapourTrail](https://github.com/Jungle-Bus/VapourTrail) :bus en vecto
- [opendata navitia](https://navitia.opendatasoft.com/explore/?sort=modified)
- [brouter](http://brouter.de/brouter-web/): iti, une app android &amp; site web un peu roots mais top pour les iti vélo entre autre (18 profils)
- [OpenStreetCam](http://openstreetcam.org/map/): stocker en libre des photos pour contribuer
- [fieldpapers](http://fieldpapers.org/): imprimer la carte, aller sur le terrain, anoter, scaner, retravailler dans OSM
- [keepright](https://www..at/): osmose like

# D'autres liens
- [tutoriels-openstreetmap](https://cartocite.fr/tutoriels-openstreetmap/)
- [tutoqgis](http://ouvrir.passages.cnrs.fr/tutoqgis/)
- [openstreetmapdata](http://openstreetmapdata.com/)
- [Le programme](http://sotm2018.openstreetmap.fr/programme.html)
- [Les présentations (dépot)](https://nextcloud.openstreetmap.fr/index.php/s/mZl1S5P4Rvx0tR9)
- [Le pad des CR](https://annuel.framapad.org/p/sotmfr-2018)

# Enfin
Pour ceux qui sont arrivés jusque là, félicitations ! Comme vous pouvez le constater, c'était un cru extrémement riche et diversifié. Forcément, il n'y a ici qu'une partie de ce qui été présenté.
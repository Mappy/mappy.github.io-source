Title: Vues 360 en WebGL
Date: 2015-10-22
Slug: vues-360-en-webgl
Authors: Mappy
Tags: French,JavaScript,WebGL,three.js
Summary: Cet article présente la migration des vues 360 depuis Flash vers WebGL

Le site Mappy offre depuis 2011 des [vues 360°][1] des plus grandes villes de France.
La couverture est d’ajourd’hui 320 villes.

![Mappy 360 Web player](images/mappy_panorama_web_flash_player.png)

En effet, 2 "Mappy Car" ([@earthmine02][2], [@earthmine07][3]) et même un "Mappy Bike" parcourent les rues pour les prendre en photo sous tous les angles.

![Mappy Car](images/webgl/mappy-car.jpg)
![Mappy Bike](images/webgl/mappy-bike.jpg)

Historiquement, le composant chargé d’afficher les vues fût développé en Flash.

Il était grand temps de mettre ce composant à jour en adoptant des technologies modernes pour afficher de la 3d au sein du navigateur, j’ai nommé [WebGL][4].

Mais avant de nous plonger dans WebGL, une présentation des vues 360 s’impose.

# Prises de vue 360

Les "Mappy Car" sont équipées de plusieurs appareils photos orientés de chaque côté de la voiture et prennent des photos régulièrement de façon synchronisée pendant le déplacement.
Elles enregistrent également différents paramètres tels que les coordonnées GPS, l’altitude, le tangage (pitch), l’orientation (yaw) et le roulis (roll).

Les photos sont ensuites déformées et assemblées afin d'obtenir 6 images que l'on pourra projeter à l’intérieur d’un cube (on parle de "skybox" en anglais).

![Bitmap tile faces layout on a cube](images/panoramic_cube_01.png)
![Cube faces layout](images/panoramic_cube_02.png)
![Cube rotation angles names](images/panoramic_cube_04.png)

La caméra peut bouger à l’intérieur du cube sur 2 axes afin de pivoter horizontalement et verticalement et ainsi, de "bouger la tête".

Il y a plusieurs façon de se déplacer d'une vue à l'autre :
- En utilisant les flèches, on peut se déplacer vers la vue la plus proche dans la direction souhaitée.
- En cliquant sur le sol, on va chercher s'il existe une vue proche de ce point et l'afficher.
Le déplacement d'une vue à l'autre consiste simplement à charger les images formant la nouvelle skybox (le cube dans lequel se trouve la caméra) et à effacer les précédentes.

Il est possible de zoomer dans la vue. Pour cela, nous avons joué sur l'angle de vision (on l’appelle [field of view][5] en anglais). 

# Résolution progressive

Afin d'avoir un rendu le plus rapide possible et pour éviter à l'utilisateur de bloquer sur un fond noir lorsque sa connexion est lente, la vue charge d'abord un cube avec des images de basse qualité, donc très légères.
Lorsque cette première skybox est affichée, la vue va charger des images de meilleure qualité. En fonction de la taille d’écran ou de la résolution, chaque face du cube sera composé d'une ou de plusieurs images (1, 4 ou 16) afin d’avoir un rendu net sur tous les supports.

![différentes résolutions](images/panoramic_cube_03.png)

# Interaction avec les objets

TODO

# Three.js

Plutôt que de réinventer la roue, nous nous sommes rapidement orientés vers [three.js][6], une excellente librairie d’affichage 3d.
Three.js permet, en quelques lignes de code, d’afficher une vue 3d sans avoir à manipuler l’API WebGL de plus bas niveau.

# Support navigateurs

WebGL est supporté dans tous les [navigateurs modernes][7], y compris IE11.
Cependant, nous nous sommes rapidement rendus compte que certaines tablettes ou téléphones Android, bien que récents, ne supportent pas WebGL.
Par conséquent, nous avons également utilisé un 2ème système de rendu proposé par Three.js : CSS3d.
Ce dernier utilise les [transformations CSS 3d][8] qui sont elles [supportées de façon un peu plus large][8].
CSS3d est en pratique moins performant que WebGL mais permet d’offrir un support sur ces périphèriques ainsi que sur IE 10.

# Réalité augmentée et cardBoard

Nous n’avons pas pu résister à l'envie de connecter l’[API DeviceOrientations][11] à la vue pour la [piloter grâce aux capteurs d’orientation][12] d’un téléphone mobile ou d’une tablette.

Enfin, si vous disposez d’un [cardboard][13], vous pouvez chausser vos lunettes et [visualiser les vues 360 en réalité augmentée][14].
Three.js implémente déjà cette fonctionnalité via les objets StereoEffect et DeviceOrientationControls. Je vous invite à lire ce [très bon article][15] si le sujet vous intéresse.

  [1]: http://fr.mappy.com/#/1/M1/TSearch/Sparis/N511.00419,1.74393,2.35107,48.85683/Z7/
  [2]: https://twitter.com/earthmine02
  [3]: https://twitter.com/earthmine07
  [4]: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API
  [5]: https://en.wikipedia.org/wiki/Field_of_view
  [6]: http://threejs.org/
  [7]: http://caniuse.com/#search=webgl
  [8]: https://developer.mozilla.org/en-US/docs/Web/CSS/transform
  [9]: http://caniuse.com/#feat=transforms3d
  [11]: https://developer.mozilla.org/en-US/docs/Web/API/Detecting_device_orientation
  [12]: /resources/webgl/deviceorientation.html
  [13]: https://www.google.com/get/cardboard/
  [14]: /resources/webgl/cardboard.html
  [15]: http://www.sitepoint.com/bringing-vr-to-web-google-cardboard-three-js/

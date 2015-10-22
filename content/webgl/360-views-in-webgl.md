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

Les "Mappy Car" sont équipées de plusieurs appareils photos orientés de chaque côté de la voiture et prennent des photos régulièrement de façon synchronisé pendant le déplacement.
Elles enregistrent également différents paramètres tels que les coordonnées GPS, l’altitude, le tangage (pitch), l’orientation (yaw) et le roulis (roll).

Les images sont ensuites assemblés pour donner 6 images, de façon à ce qu’on puisse les projeter à l’intérieur d’un cube (on parle de "skybox" en anglais).

![Bitmap tile faces layout on a cube](images/panoramic_cube_01.png)
![Cube faces layout](images/panoramic_cube_02.png)
![Cube rotation angles names](images/panoramic_cube_04.png)

La caméra peut bouger à l’intérieur du cube sur 2 axes afin de se tourner horizontalement et verticalement et ainsi, de "bouger la tête".

Le déplacement dans la vue va charger de nouvelles images, prises à l’endroit le plus proche où l’utilisateur a cliqué.

Le zoom s’effectue simplement en jouant sur l’angle de vision (on l’appelle [field of view][5] en anglais).

# Résolution progressive

Á l’initialisation, seule une image par face est chargée.
Cette image est en basse qualité mais permet d’avoir un premier rendu rapide.
Par la suite et en fonction de la taille d’écran ou de la résolution, plusieurs images seront chargées (soit 4 par face, soit 8) afin d’améliorer la qualité d’image.

![différentes résolutions](images/panoramic_cube_03.png)

# Interaction avec les objets

TODO

# Three.js

Plutôt que de réinventer la roue, nous nous sommes rapidement orienté vers [three.js][6], une excellente librairie d’affichage 3d.
Three.js permet, en quelques lignes de code, d’afficher une vue 3d sans avoir à manipuler l’API WebGL de plus bas niveau.

# Support navigateurs

WebGL est supporté dans tous les [navigateurs modernes][7], y compris IE11.
Cependant, nous nous sommes rapidement rendu compte que certaines tablettes ou téléphones Android, bien que récente, ne supporte pas WebGL.
Par conséquent, nous avons également utiliser un 2ème système de rendu proposé par Three.js : CSS3d.
Ce dernier utilise les [transformations CSS 3d][8] qui sont elles [supportées de façon un peu plus large][8].
CSS3d est en pratique moins performant que WebGL mais permet d’offrir un support sur ces périphèriques ainsi que sur IE 10.

# Réalité augmenté et cardBoard

Nous n’avons pas pu résister à connecter l’[API DeviceOrientations][11] à la vue pour la [piloter grâce aux capteurs d’orientation][12] d’un téléphone mobile ou d’une tablette.

Enfin, si vous disposez d’un [cardboard][13], vous pouvez chaussez vos lunettes et [visualiser les vues 360 en réalité augmenté][14].
Cela est possible très facilement avec Three.js via les objets StereoEffect et DeviceOrientationControls. Je vous invite à lire ce très [bon article][15] si le sujet vous intéresse.

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

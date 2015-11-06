Title: Vues 360 en WebGL
Date: 2015-11-05
Slug: vues-360-en-webgl
Authors: Mappy
Tags: French,JavaScript,WebGL,three.js
Summary: Cet article présente la migration des vues 360 depuis Flash vers WebGL

Le site [Mappy][24] offre depuis 2011 des [vues 360°][1] des [320 villes][16] plus grandes villes de France :

<iframe src="http://widgets.mappy.com/360view?key=techblog&lat=48.85369&lng=2.34821" width="100%" height="400" scrolling="no"></iframe>

## MappyCar

En effet, 2 voitures surnommées "MappyCar" ([@earthmine02][2], [@earthmine07][3]) parcourent les rues des villes de France pour prendre des photos sous plusieurs angles.

![Mappy Car](images/webgl/mappy-car.jpg)

## Historiquement...

Historiquement, le composant chargé d’afficher les vues sur le site [fr.mappy.com][24] fût développé en Flash.

Il était grand temps de mettre ce composant à jour en adoptant des technologies modernes pour afficher de la 3d au sein du navigateur, j’ai nommé [WebGL][4].

Mais avant de nous plonger dans WebGL, une présentation des vues 360 s’impose.

## Explications des prises de vue 360

Les véhicules Mappy sont équipés de 8 appareils photos orientés de chaque côté de la voiture et prennent des photos régulièrement de façon synchronisée pendant le déplacement.
Ils enregistrent également différents paramètres tels que les coordonnées GPS, l’altitude, le tangage (pitch), l’orientation (yaw) et le roulis (roll).

Les photos sont ensuites assemblées afin d'obtenir 6 images.
Ces 6 images seront projetées à l’intérieur d’un cube. Ce cube est alors appelé "skybox".

![Bitmap tile faces layout on a cube](images/panoramic_cube_01.png)

## Scène 3d

L’astuce est alors de créer une scène 3d composée de ce cube et d’une caméra au centre.

![Cube faces layout](images/panoramic_cube_02.png)

La caméra peut bouger à l’intérieur du cube sur 2 axes afin de pivoter horizontalement et verticalement, donnant l’effet de regarder autour de soi.

## Déplacement

Il y a plusieurs façons de se déplacer d'une vue à l'autre :

 - En utilisant les flèches, on peut se déplacer vers la vue la plus proche dans la direction souhaitée.
 - En cliquant sur le sol, on va chercher s'il existe une vue proche à ce point et l'afficher.

Le déplacement d'une vue à l'autre consiste simplement à charger les images formant la nouvelle "skybox" (le cube dans lequel se trouve la caméra) et à effacer les précédentes.

Il est également possible de zoomer dans la vue. Pour cela, nous avons joué sur l'angle de vision (on l’appelle [field of view][5] en anglais).

## Chargement progressif

Afin d'avoir un rendu le plus rapide possible et pour éviter à l'utilisateur de bloquer sur un fond noir lorsque sa connexion est lente, la vue charge d'abord un cube avec des images de basse qualité, donc très légères.
Lorsque cette première "skybox" est affichée, la vue va charger des images de meilleure qualité. En fonction de la taille d’écran ou de la résolution, chaque face du cube sera composée d'une ou de plusieurs images (1, 4 ou 16 images par face) afin d’avoir un rendu net sur tous les supports.

![différentes résolutions](images/panoramic_cube_03.png)

## Three.js

Plutôt que de réinventer la roue, nous nous sommes rapidement orientés vers [three.js][6], une excellente librairie 3d.
Three.js permet, en quelques lignes de code, d’afficher une vue 3d sans avoir à manipuler l’API WebGL de plus bas niveau.

Voici un exemple de "skybox" basique où la caméra tourne sur elle-même :

<iframe width="100%" height="700" src="//jsfiddle.net/053ng6gm/2/embedded/" allowfullscreen="allowfullscreen" frameborder="0"></iframe>


## Interaction avec les objets

Savoir sur quel élément a cliqué l’utilisateur dans un moteur 3d est plus compliqué que simplement ajouter un "listener" sur un élément HTML.
En effet, lors d’un clic dans la scène 3d, nous récupèrons simplement un point (x,y) et il convient alors de trouver quel objet il croise (c’est le principe du [raycasting][21]).

Pour cela, nous allons d’abord trouver le vecteur 3d entre ce point et la position de la caméra.
Ensuite, Three.js nous propose le [Raycaster][22] qui permet ensuite de détecter une intersection avec un objet 3d.

    var vector = getVectorFromEvent(event);
    var raycaster = new THREE.Raycaster(this.camera.position, vector);
    var intersectedObjects = raycaster.intersectObjects(objectsIn3dScene);


## Support navigateurs

WebGL est supporté dans tous les [navigateurs modernes][7], y compris IE11.
Cependant, nous nous sommes rapidement rendus compte que certaines tablettes ou téléphones Android, bien que récents, ne supportent pas WebGL.
Par ailleurs, WebGL peut être désactivé en fonction des [pilotes installés (ou non) sur la machine][17].

Par conséquent, nous avons également utilisé un système de rendu alternatif proposé par Three.js, le [CSS3DRenderer.js][18].

Ce dernier utilise les [transformations CSS 3d][8] qui sont elles [supportées de façon un peu plus large][8].
CSS3DRenderer est en pratique moins performant que WebGL mais permet d’offrir un support minimal sur ces périphèriques ainsi que sur IE 10.

## Réalité augmentée et cardBoard

Les téléphones et tablettes modernes possèdent des capteurs d’orientations.
Ils sont accessibles en JavaScript via [API DeviceOrientations][11].
Nous n’avons pas pu résister à l'envie de [connecter cette API à la vue pour la piloter avec son téléphone][12].

Enfin, si vous disposez d’un [cardboard][13] (boîte en carton où l’on peut insérer son téléphone), vous pouvez chausser vos lunettes et [visualiser les vues 360 en réalité augmentée][14].

![virtual reality](images/webgl/virtual-reality.png)

Three.js implémente cette fonctionnalité via [StereoEffect][19] et [DeviceOrientationControls][20]. Je vous invite à lire ce [très bon article][15] si le sujet vous intéresse.

## Un dernier mot sur l’intégration des vues sur votre site

[Mappy][24] propose plusieurs [modes d’intégration][23] pour ses cartes ou sa vue 360.
L’un des modes se présente sous la forme d’un widget (tel que l’exemple en haut de cette page).
N’hésitez pas à nous contacter (deportalisation[AT]mappy.com) si une intégration sur votre site ou vos applications mobiles vous intéresse.


  [1]: http://fr.mappy.com/#/436/M1/TSearch/Sparis/N1090.14493,12.34393,2.34821,48.85369/Z7/
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
  [16]: http://widgets.mappy.com/360view/documentation/#coverage
  [17]: https://www.khronos.org/webgl/wiki/BlacklistsAndWhitelists
  [18]: https://github.com/mrdoob/three.js/blob/master/examples/js/renderers/CSS3DRenderer.js
  [19]: https://github.com/mrdoob/three.js/blob/master/examples/js/effects/StereoEffect.js
  [20]: https://github.com/mrdoob/three.js/blob/master/examples/js/controls/DeviceOrientationControls.js
  [21]: https://fr.wikipedia.org/wiki/Raycasting
  [22]: https://github.com/mrdoob/three.js/blob/master/src/core/Raycaster.js
  [23]: http://corporate.mappy.com/faq/integrez-mappy/
  [24]: http://fr.mappy.com


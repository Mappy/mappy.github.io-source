Title: Android StreetView-like 360 panorama with OpenGl
Date: 2014-08-04
Slug: Android StreetView-like 360 panorama
Author: JohnFromMappy
Tags: Android,panorama,360,ray-picking,OpenGL,English
Summary: Display StreetView-like panoramas on Android devices, with interactive arrows to move from a view to the next, based on 360 photos with cubic projection.

[Mappy][1] offers StreetView-like immersive experience to explore France cities. The web interface uses a [Flash player to display the cubic projections of "360" panorama images][2].

![Mappy 360 Web player](images/mappy_panorama_web_flash_player.png)

To provide the same feature on Android devices, we looked at existing solutions. Two we came accross were :

 - [krpano HTML5 Viewer][3] works in modern mobile browsers ([supported browsers, WebViews][4]).
 - [PanoramaGL][5] Android library handles many projections (spherical, cubic and cylindrical), JSON configuration, transitions, gyroscope and more.

Still, these two did not exactly match our needs :

 1. **Wide device support, starting with Android 2.3**, while [krpano][4] requires latest Android browsers or `WebViews`.
 2. **StreetView-like gesture control (rotate, zoom)**, while [PanoramaGL][5] handles "Pan-Rotate" as a speed vector we felt not as easy to control. It may be configurable but we didn't find out how.
 2. **Click on 3D way arrows**, while PanoramaGL provides hotspots with visual feedback on click. Still, these are 2D bitmap layers inside textures, as far as we understood.

![Mappy 360 Web player](images/mappy_panorama_android_01.png)
![Mappy 360 Web player](images/mappy_panorama_android_02.png)

> Available on Google Play, [Mappy for Android][11].

Let's describe the main technical aspects we implemented building our own *PanoramicLib*. 



# Cubic projection

To display 360 panoramas with cubic projection, we texture the inner faces of a simple cube mesh (6 square faces, 2 triangles each).

![Bitmap tile faces layout on a cube](images/panoramic_cube_01.png)
![Cube faces layout](images/panoramic_cube_02.png)
![Cube rotation angles names](images/panoramic_cube_04.png)

In the OpenGL 3D space, both cube and camera center are (x=0, y=0, z=0). The camera rotates on itself, using pitch and yaw angles. This is important because the cubic projected textures are valid only if seen from the cube center. Zoom is done just by changing the Field Of View angle (the cube mesh is not scaled).

![*PanoramicLib* sample using "target" textures](images/panoramic_cube_05.png)
![*PanoramicLib* sample using "target" textures](images/panoramic_cube_06.png)
> *PanoramicLib* sample using "target" textures for debugging

In *PanoramicLib* source :

- `PanoramicGestureListener` class handles scroll and fling gestures to set camera orientation.
- `PanoramicScaleGestureListener` class handles pinch to zoom gesture.



# Progressive resolution loading

Our panorama images are provided through Web services. For faster loading, low resolution bitmaps (128 * 128) are first downloaded. Higher resolutions are progressively downloaded, updating the cube faces to sharper textures. For high resolutions, faces are divided in multiple tiles of 512 * 512 pixels. 

![Multiple bitmap tiles per face possibilities](images/panoramic_cube_03.png)

Ideally, using tiles would lower the amount of downloaded data because client application could :

 - Download tiles only for visible faces,
 - Download max resolution tiles only for zoomed parts

... but we didn't push this far for now.

In *PanoramicLib* source, the `PanoramicTile` interface is responsible for handling a bitmap tile and a tiny `PanoramicTileIdentifier` structure describing which face of the cube the tile belongs. The "split factor" (`PanoramicTileIdentifier.getSplitFactor()`) is number of times the face is splitted.

 - splitFactor = 0 : 1 tile per face,
 - splitFactor = 1 : 4 tiles per face,
 - splitFactor = 2 : 16 tiles per face.

`PanoramicTileIdentifier.getPosition()` gives the position of tile inside the face (0 is top-left).

Tiles can be added any time during cube rendering. The `PanoramicCubeMesh` will consider face, splitfactor and position to add the bitmap on to the corresponding texture. A higher split factor is considered as a higher resolution. The cube will adapt to use the tiles with the highest split factor.

The face splits are not polygons. The cube mesh vertices never changes and  each face always uses only two triangles. The multiple tiles of a face are actually merged in a single texture. While resolution goes up, new texture buffers are allocated and tile bitmaps are progressively drawn inside (using `GLUtils.texSubImage2D()`).



# Interactive elements with ray-picking
To provide click-able 3D arrows as in Google StreetView and move from a panorama to a neighbor one, we needed to detect the click. In 3D space.

> *"Picking is the task of determining which screen-rendered object a user has clicked on."* [(Wikipedia)](http://en.wikipedia.org/wiki/Picking)

The idea with ray-picking is to compute a 3D ray between the camera and the point the user clicked. For each polygon in the scene, you test if the ray intersects it, resolving the ["line-plane intersection" equation](http://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection). The closest intersected polygon belongs to the clicked object.

![Ray picking diagram](images/ray_picking_01.png)
> Image from [VSG, Visualization Science Group - Open Inventor Mentor, 2nd Edition - Volume I](http://oivdoc90.vsg3d.com/content/88-picking)

The picking code comes from [Ivan Schuetz "Android OpenGL Picking"][6] GitHub project.
It refers to [Gregory Beauchamp "Ray picking on Android"][7] article.

We adaptated the code to take the picking out of the OpenGL thread. In `PanoramicLib`, we notify the `Activy` on way arrow click to load next panorama view. This has to run on the UI thread. 

In Ivan Schuetz example, ray intersect computing is done in `ExampleGLRenderer.onDrawFrame(GL10 gl)` [(source)][8], calling `ExampleGLObject.draw(GL10 gl, Ray ray)` on each scene object. Intersections are logged to Android LogCat from there [(source)][9]. It runs on the OpenGL thread because it requires the OpenGL context to grab projection and modelview matrixes to compute ray and projected objects coordinates.

To handle intersection computing on the UI thread, we saved the current OpenGL matrixes in a member of each `ArrowMesh` instance, on each draw, using `MatrixGrabber` class [(source)][10].


  [1]: http://mappy.com
  [2]: http://fr.mappy.com/#/40/M1/TSearch/Snotre+dame+paris/N42.63223,-2.96266,2.35218,48.85267/Z10/
  [3]: http://krpano.com/
  [4]: http://krpano.com/docu/html5/#supportedsystems
  [5]: https://github.com/zarelaky/panoramagl-android
  [6]: https://github.com/i-schuetz/Android_OpenGL_Picking
  [7]: http://android-raypick.blogspot.de/2012/04/first-i-want-to-state-this-is-my-first.html
  [8]: https://github.com/i-schuetz/Android_OpenGL_Picking/blob/master/glpicking/src/com/example/glpicking/ExampleGLRenderer.java
  [9]: https://github.com/i-schuetz/Android_OpenGL_Picking/blob/master/glpicking/src/com/example/glpicking/ExampleGLObject.java
  [10]: https://github.com/i-schuetz/Android_OpenGL_Picking/blob/master/glpicking/src/com/example/glpicking/MatrixGrabber.java
  [11]: https://play.google.com/store/apps/details?id=com.mappy.app

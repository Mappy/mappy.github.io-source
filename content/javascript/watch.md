Title: Javascript: la construction à la volée (watching) avec Browserify
Date: 2016-10-06
Slug: browerify-la-construction-a-la-volee
Authors: Mappy
Tags: French,JavaScript,watching,browerify,watchify,livereload
Summary: Article présentant la création du bundle à chaque modification des fichiers sources avec Browserify

# Browerify, c'est quoi déjà ?

De manière simple, [browserify](http://browserify.org/) permet d'avoir accès à l'écosystème de NodeJS (`NPM`, `CommonJS`) avec des scripts destinés au browser.<br />
Browswerify est lui même un écosystème à part entière car il s'accompagne de `plugins` et de `transforms` afin de pouvoir l'adapter à ses besoins.<br />
Après avoir installé le module via `NPM`, il peut s'utiliser directement en ligne de commande :

```
browserify main.js -o bundle.js
```

Mais est plus souvent utilisé en tant que librairie dans un script NodeJS :

```javascript
var fs          = require('fs');
var browserify  = require('browerify');
var bundleWS    = fs.createWriteStream(__dirname + '/bundle.js');

browserify({
    entries: "main.js"
}).bundle().pipe(bundleWS);
```

On remarque immédiatement que `browswerify` utilise des flux textes ou [text streams](http://www.sandersdenardi.com/readable-writable-transform-streams-node/) comme format de sortie via `bundle()`,
ce qui permet une grande souplesse mais ausi de  pouvoir l'utiliser avec d'autres outils utilisant les streams comme [gulp](http://gulpjs.com/) (attention car ce dernier utilise un format de stream bien à lui basé sur le file system [vinyl](https://github.com/gulpjs/vinyl), il faudra donc convertir le `text stream` en ce format avant d'utiliser des pipes `Gulp`).

Browserify propose des `transforms`, qui sont des tranformateurs de flux, comme la minification (`uglify`) ou l'ajout de scripts de librairies tiers comme `bower` ou `shim`.<br />
On peut aussi lui ajouter des greffons (plugins) afin d'ajouter à `browserify` d'autres capacités comme le `watching` avec Watchify.

# A quoi consiste de watching ?

Il s'agit littéralement de vérifier l'état d'un ensemble de fichiers et de décencher un processus à chaque modification.<br />
Par extention on appel `watching` également:

+ la construction d'un nouveau build à chaque modification
+ et dans le cas de scripts navigateurs, le reload de la page (`livereload`)

# Comment le met-on en place ?

## Watchify

[Watchify](https://github.com/substack/watchify) est un plugin `browerify`, il peut s'ajouter à la config grâce à l'attribut `plugins` ou via un `wrapper`:

```javascript
var fs          = require('fs');
var browserify  = require('browerify');
var watchify    = require('watchify');
var bundleWS    = fs.createWriteStream(__dirname + '/bundle.js');

//config
browserify(Object.assign({
    entries: "main.js",
    plugin: [watchify]
}, watchify.args)).bundle().pipe(bundleWS);
```
Ou

```javascript
var fs          = require('fs');
var browserify  = require('browerify');
var watchify    = require('watchify');
var bundleWS    = fs.createWriteStream(__dirname + '/bundle.js');

//wrapping
watchify(browserify(Object.assign({
    entries: "main.js",
}, watchify.args))).bundle().pipe(bundleWS);
```

Vous avez surement remarqué qu'on ajoute en plus des `watchify.args` à `browserify`, ces arguments sont:
```javascript
{
    cache: {},
    packageCache: {}
}
```
En fait ces options permetent d'activer le cache des sources et des modules `NPM` de `browserify`, ce qui permet à `watchify` de reconstruire les livrables de manière incrémetale.<br />
Il est évident que la création du livrable est nettement plus rapide de cette manière, d'ailleurs `watchify` impose ces options et ne surveille pas si elles ne sont pas positionnées.

Seulement quelques milisecondes sont nécessaires pour reconstruire les sources grâce à la construction incrémentale :

![Watchify](images/watchify.gif)

## Livereload

Une fois les sources construites, il est pratique de recharger la page immédiatement et automatiquement, `livereload` permet cela grâce aux [WebSockets](https://developer.mozilla.org/fr/docs/WebSockets).<br />
Nous allons utiliser `gulp-livereload` et voir ainsi comment on combine les différentes `streams` :

```javascript
var browserify  = require('browerify');
var watchify    = require('watchify');
var source      = require('vinyl-source-stream');
var livereload  = require('gulp-livereload');

browserify(Object.assign({
    entries: "main.js",
    plugins: [watchify]
}, watchify.args)).bundle()
    //Create Vinyl write streams from conventional write text streams
    .pipe(source(__dirname + '/bundle.js'));
    .pipe(livereload);
```

Et oui, `gulp-livereload` a juste besoin d'être "pipé" pour être fonctionnel, la puissance des `streams` et `gulp`...

L'appel au script `livereload.js` doit être ajouté dans la page HTML :

```html
<script src="http://localhost:35729/livereload.js"></script>
```
Il peut aussi être chargé via un plugin navigateur pour ne pas polluer la page.<br />
Si le HTTPS est nécessaire, comme sur le site Mappy, préferez le plugin [RemoteLivereload](https://chrome.google.com/webstore/detail/remotelivereload/jlppknnillhjgiengoigajegdpieppei) (Chrome/Chromium) à [Livereload](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei) (Chrome/Chromium).

Au sujet d'HTTPS, voici conmment on ajoute la clé et le certificat à `gulp-livereload` :
```javascript
...
var livereload  = require('gulp-livereload');

livereload.listen({
    key: fs.readFileSync(__dirname + '/private.key'),
    cert: fs.readFileSync(__dirname + '/public.pem')
});

browserify(Object.assign({
...
```

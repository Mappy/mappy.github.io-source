Title: Javascript: la construction à la volée (watching) avec Browserify
Date: 2016-10-06
Slug: browerify-la-construction-a-la-volee
Authors: Mappy
Tags: French,JavaScript,Watching,Browerify,Watchify,Livereload
Summary: Article présentant la création du bundle à chaque modification des fichiers sources avec Browserify

# Browerify, c'est quoi déjà ?

De manière simple, [Browserify](http://browserify.org/) permet d'avoir accès à l'écosystème de NodeJS (NPM, CommonJS) avec des scripts déstinés au browser.<br />
Browswerify est lui même un écosystème à part entière car il s'accompagne de plugins et de transforms afin de pouvoir l'adapter a ses besoins.<br />
Aprés avoir installé le Module via NPM, il peut s'utiliser directement en ligne de commande:

```
browserify main.js -o bundle.js
```

Mais est plus souvent utilisé en tant que librairie dans un script NodeJS:

```javascript
var fs          = require('fs');
var browserify  = require('browerify');
var bundleWS    = fs.createWriteStream(__dirname + '/bundle.js');

browserify({
    entries: "main.js"
}).bundle().pipe(bundleWS);
```

On remarque immédiatement que Browswerify utilise des flux textes ou [text streams](http://www.sandersdenardi.com/readable-writable-transform-streams-node/) comme format de sortie via bundle(), 
ce qui permet une grande souplesse mais ausi de  pouvoir l'utiliser avec d'autres outils basés utilisant les streams comme [Gulp](http://gulpjs.com/) (attention car ce dernier utilise un format de stream bien à lui basé sur le file system [Vinyl](https://github.com/gulpjs/vinyl), il faudra donc convertir le text stream en ce format avant d'utiliser des pipes Gulp).  

Browserify propose des transforms, qui sont des tranformateurs de flux, comme la minification (Uglifyfy) ou l'ajout de scripts de librairies triers comme Bower ou Shim.<br />
On peut aussi lui ajouter des gréffons (plugins) afin d'ajouter à Browserify d'autres capacités comme le watching avec Watchify.

# A quoi consiste de watching ?

Il s'agit litteralement de vérifier l'état d'un ensemble de fichiers et de décencher un processus à chaque modification.<br />
Par extention on appel watching également:

+ la construction d'un nouveau build à chaque modification
+ et dans le cas de scripts browsers, le reload de la page (Livereload)

# Comment le met-on en place ?

## Watchify

[Watchify](https://github.com/substack/watchify) est un plugin Browerify, il peut s'ajouter à la config grâce à l'attribut "plugins" ou se wrapper:

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

Vous avez surement remarqué qu'on ajoute en plus des watchify.args à Browserify, ces args sont:
```javascript
{
    cache: {},
    packageCache: {}
}
```
En fait ces options permetent d'activer le cache des sources et des NPM de Browserify, ce qui permet à Watchify de reconstruire les builds de manière incrémetale.<br />
Il est évident que la création du build est nettement plus rapide de cette manière, d'ailleurs watchify impose ces options et ne watche pas si elles ne sont pas positionnées.

Seulement quelques milisecondes sont nécessaires pour reconstruire les sources grâce au build incrémental:

![Watchify](images/watchify.gif)

## Livereload

Une fois les sources buildée il est pratique de recharger la page immédiatement et automatiquement, Livereload permet cela grâce aux [WebSockets](https://developer.mozilla.org/fr/docs/WebSockets).<br />
Nous allons utiliser gulp-livereload et voir ainsi comment on combine les différentes streams:

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

Et oui, gulp-livereload a juste besoin d'être pipé pour être fonctionnel, la puissance des streams et Gulp...

L'appel au script livereload.js doit être ajouté dans la page HTML 

```html
<script src="http://localhost:35729/livereload.js"></script>
```
Il peut aussi être chargé via un addon browser pour ne pas poluer la page.<br />
Si le HTTPS est nécessaire, comme pour Mappy afin de béneficier de la géolocalisation du broswer, préferez le plugin [RemoteLivereload](https://chrome.google.com/webstore/detail/remotelivereload/jlppknnillhjgiengoigajegdpieppei)(Chrome/Chromium) à [Livereload](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei)(Chrome/Chromium).

Au sujet d'HTTPS, voici conmment on ajoute clé et certificat à gulp-livereload:
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

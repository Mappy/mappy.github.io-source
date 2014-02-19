Title: Mappy et Oslandia vers l'OpenSource
Date: 2014-02-11
Slug: Mappy et Oslandia vers l'OpenSource
Author: Mappy
Tags: French,Mapnik,PostGIS,OpenSource
Summary: Depuis plus de deux ans, Oslandia accompagne Mappy dans sa transition vers l’OpenSource. La première étape est symbolisée par le projet de migration des bases de données Oracle du backoffice cartographique vers PostGIS.


Paris, le 11 février 2014. 

Depuis plus de deux ans, Oslandia accompagne Mappy dans sa transition vers l’OpenSource. La première étape est symbolisée par le projet de migration des bases de données Oracle du backoffice cartographique vers PostGIS. Celui-ci vient notamment d’être finalisé et fonctionne actuellement en production.

Mappy propose des services de calcul d’itinéraire et de cartographie. Supportant plusieurs milliards de requêtes par mois, la plateforme LBS (Location Based Services) est au cœur de l’activité de Mappy et sert de socle aux nouveaux produits tel que le Web To Store.

Oslandia travaille conjointement avec Mappy pour migrer cette plateforme cartographique d’une solution développée en interne, vers une solution basée entièrement sur des logiciels libres, afin de préparer les défis techniques et opérationnels à venir.

Les backoffices de préparation des données et de création du plan cartographique ont été entièrement migrés avec succès.

Cette pile applicative était initialement basée sur Oracle Spatial, SQL Server, et des outils internes non standards de création de carte. Elle n’utilise plus désormais que des composants OpenSource.

Oracle et SQL Server ont été entièrement remplacés par PostgreSQL et PostGIS, qui constitue le socle de base de données géographique pour le stockage et le prétraitement des données géographiques. Mapnik, Python, Tornado, Varnish, MemCached, Debian sont les autres composants OpenSource utilisés.

La migration vers ces composants OpenSource a permis de rationnaliser et d’optimiser l’architecture du composant « carte »:

* Temps de traitement des données réduit 
* Standardisation des formats et API
* Forte diminution de la dette technique
* Nombre de lignes de code optimisé
* Baisse du coût de la plateforme, et passage à l’échelle plus économique
* Montée en compétence et motivation des équipes
* Maîtrise complète des outils

Oslandia a permis à Mappy d’intégrer la culture et les méthodes de l’OpenSource dans ses équipes, et leur a fourni les compétences techniques nécessaires pour mettre en place cette architecture à forte charge. Les compétences d’Oslandia en systèmes d’information géographique, et son expertise unique en France sur PostGIS, ont permis de mener à bien ce projet.

Mappy a ainsi pu bénéficier des dernières technologies OpenSource à la pointe de l’état de l’art, et également pu contribuer à certains projets libres comme Mapnik.

PostGIS, la base de données géographique supportant toute l’infrastructure, a permis d’atteindre de très hautes performances et un niveau fonctionnel élevé.

La base de 75Go bénéficie des toutes dernières avancées de PostgreSQL et PostGIS, tels que la réplication au fil de l’eau, les nouvelles fonctions géographiques de PostGIS, les requêtes CTE récursives, le support de JSON et bien plus.

Audrey Malherbe, responsable du projet chez Mappy, souligne que le choix de PostgreSQL et de PostGIS était une évidence : 
>« Nous voulions basculer dans l’OpenSource en nous appuyant sur des technologies performantes et reconnues comme PostGIS. Il était important pour nous de contribuer à l’OpenSource et l’expertise technique d’Oslandia et son implication dans la communauté nous ont permis de nous lancer dans cette aventure en toute confiance. »

Mappy a l’intention de continuer ce virage vers l’OpenSource et d’étendre la méthode de migration aux autres services de la plateforme cartographique.



**À propos de Mappy**

Spécialiste du calcul d’itinéraire et des services de cartographie, Mappy est reconnu comme le leader français de la recherche locale par la carte, sur Internet, tablettes, mobiles et GPS.

Mappy propose à ses utilisateurs trois types de recherche : la recherche par le plan, qui permet de visualiser un quartier, de s’immerger dans la ville  grâce aux vues 360° dans 320 villes françaises, mais également de pousser la porte de plusieurs milliers de commerces ; la recherche d’itinéraires disponible pour les déplacements en voiture, en transports en commun, en vélo et en mode piéton ; enfin la recherche de produits, permettant de localiser un produit précis, dans une zone géographique donnée, de connaître son prix et sa disponibilité.

Acteur majeur du déplacement urbain, Mappy propose aux annonceurs une solution géolocalisée sur l’ensemble du territoire, facilitant les dispositifs web-to-store et la génération de trafic vers leurs points de vente.

Mappy compte aujourd’hui plus de 10 millions d’utilisateurs mensuels sur Internet, tablettes et mobiles (Mappy et MappyGPS Free).

Mappy est une filiale à 100% de Solocal Group. <http://www.mappy.com>

**À propos d’Oslandia**

Oslandia est une ENL (Entreprise du Numérique Libre) Française spécialisée en systèmes d’information géographique (SIG) Open Source, et particulièrement en bases de données spatiales, Web Services OGC et SIG bureautiques. Oslandia propose une offre de service complète : conseil, audit, développement, support, formation.

<http://www.oslandia.com> 

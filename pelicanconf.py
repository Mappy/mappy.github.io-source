#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mappy'
SITENAME = u'Mappy Labs'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'theme/mappy'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s/rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Mappy', 'https://www.mappy.com/'),
          ('Appli Android', 'https://play.google.com/store/apps/details?id=com.mappy.app'),
          ('Appli iOS', 'https://itunes.apple.com/fr/app/mappy-itineraire-et-recherche/id313834655?mt=8'),
          ('Blog Mappy', 'http://corporate.mappy.com'),
          ('API Mappy', 'http://corporate.mappy.com/faq/integrez-mappy/'),
         )

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/Mappy'),
#          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images','resources']

TWITTER_URL = 'https://twitter.com/Mappy'
GITHUB_URL = 'https://github.com/Mappy'
FACEBOOK_URL = 'https://www.facebook.com/MappyOnline'

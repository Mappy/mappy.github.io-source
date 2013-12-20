#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mappy'
SITENAME = u'Mappy Labs'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'theme/tuxlite_zf' 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s/rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Mappy', 'http://www.mappy.com/'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Mappy'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images',]

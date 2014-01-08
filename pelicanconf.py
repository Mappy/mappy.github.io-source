#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mappy'
SITENAME = u'Mappy Labs'
SITEURL = 'labs.mappy.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'theme/gum' 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s/rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Mappy', 'http://www.mappy.com/'),
          ('Blog Mappy', 'corporate.mappy.com'),
          ('API Mappy', 'http://corporate.mappy.com/faq/integrez-mappy/'),
         )

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/Mappy'),
#          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images',]

TWITTER_URL = 'https://twitter.com/Mappy'
GITHUB_URL = 'https://github.com/Mappy'
FACEBOOK_URL = 'https://www.facebook.com/MappyOnline'

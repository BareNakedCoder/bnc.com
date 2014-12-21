#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time, os, binascii

#-----------------------------------------------------------------------
# BareNakedCoder Settings
#-----------------------------------------------------------------------

CACHE_UNIQUE_ID = binascii.hexlify(os.urandom(4))
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

#-----------------------------------------------------------------------
# Pelican Settings
#-----------------------------------------------------------------------
AUTHOR = u'Don Parakin'
SITENAME = u'BareNakedCoder'
SITEURL = 'http://dev.barenakedcoder.com'
TYPOGRIFY = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL




PATH = 'content'

TIMEZONE = 'UTC'   # 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#---------------- Removed Settings


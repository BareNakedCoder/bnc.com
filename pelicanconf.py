#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time, os, binascii

#-----------------------------------------------------------------------
# BareNakedCoder Settings
#-----------------------------------------------------------------------

CACHE_UNIQUE_ID = binascii.hexlify(os.urandom(4))

#---- Pelican Settings
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_PAGINATION = 8
DEFAULT_ORPHANS = 3

SLUGIFY_SOURCE = 'basename'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL
DRAFT_URL = 'bnc-drafts/{slug}.html'   # a little harder to find
DRAFT_SAVE_AS = DRAFT_URL

AUTHOR = u'Don Parakin'
SITENAME = u'BareNakedCoder'
SITEURL = 'http://dev.barenakedcoder.com'
TYPOGRIFY = True

PATH = 'content'
TIMEZONE = 'UTC'   # 'America/Toronto'
DEFAULT_LANG = u'en'

#---- Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

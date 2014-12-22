#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#-------- Inherit from Main Settings
from pelicanconf import *

#-------- Set or Override
SITEURL = 'http://www.barenakedcoder.com'     # needed for feeds
GOOGLE_ANALYTICS = 'UA-46111043-4'
DISQUS_SITENAME = 'barenakedcoder'

DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = False
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

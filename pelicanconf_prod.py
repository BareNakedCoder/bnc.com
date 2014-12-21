#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#-------- Inherit from Main Settings
from pelicanconf import *

#-------- Set or Override
GOOGLE_ANALYTICS = 'UA-46111043-4'
SITEURL = 'http://www.barenakedcoder.com'     # needed for feeds







import os
import sys

sys.path.append(os.curdir)

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

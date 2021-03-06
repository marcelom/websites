#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcelo Moreira'
SITENAME = u'Marcelo @ Stanford'
SITEURL = 'http://www.stanford.edu'  # *NO* trailing slash
SITEURL_SUFFIX = '/~marcelom/blog'  # *NO* trailing slash

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISQUS_SHORTNAME = 'marceloatstanford'
GITHUB_URL = "https://github.com/marcelom/marceloatstanford"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Copy some files over...
FILES_TO_COPY = (('favicon.ico', 'favicon.ico'),)

# Wed 24 Dec 2013, for example
# DEFAULT_DATE_FORMAT = '%a %d %b %Y'
DEFAULT_DATE_FORMAT = '%d %b %Y'

# Filename Metadata: YYYY-MM-DD-the-rest-before-the-dot-is-the-slug.md, for example
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

# Had to do this because the README.md was confusing Pelican...
PAGE_DIR = ('pages')
ARTICLE_DIR = ('posts')
ARTICLE_EXCLUDES = ('pages', '.')

# My theme ignores some templates, so here they are...
DIRECT_TEMPLATES = ('index',)  # Just index, nothing else...
ARTICLE_URL = '%s/posts/{date:%%Y}-{date:%%m}-{date:%%d}-{slug}.html' % SITEURL_SUFFIX
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_LANG_SAVE_AS = False  # Dsiables LANG processing, all site is in English...
PAGE_URL = '%s/pages/{slug}.html' % SITEURL_SUFFIX
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_SAVE_AS = False
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
# TAG_URL = '%s/tags/{slug}.html' % SITEURL_SUFFIX
# TAG_SAVE_AS = 'tags/{slug}.html'
TAG_SAVE_AS = False
YEAR_ARCHIVE_SAVE_AS = False
MONTH_ARCHIVE_SAVE_AS = False
DAY_ARCHIVE_SAVE_AS = False

# Themes
THEME = 'themes/marcelo'

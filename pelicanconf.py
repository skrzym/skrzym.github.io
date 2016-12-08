#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Skrzypiec'
SITENAME = "Michael Skrzypiec"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Pagination
DEFAULT_PAGINATION = 5
#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')
TEMPLATE_PAGES = {'blog_index.html': 'blog_index.html'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme Directory
THEME = 'theme'

# Theme Settings
#FAVICON = 'url-to-favicon'
AVATAR = "/theme/images/me_small.jpg"
SIDEBAR_DIGEST = 'Engineer/Analyst'
TWITTER_USERNAME = 'skrzym'
MENUITEMS = (('Blog', '/blog_index.html'),
             ('About Me', '/#aboutme'),
             ('Contact', '/#contact'),)
#DISPLAY_PAGES_ON_MENU = True
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/michaelskrzypiec'),
          ('github', 'https://github.com/skrzym'),
          ('twitter', 'https://twitter.com/skrzym'),
          )
DISPLAY_CATEGORIES_ON_MENU = False
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
DISPLAY_SUMMARY = True


# Plugin config
MARKUP = ('md', 'ipynb')
#IPYNB_IGNORE_CSS=True
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

#Jinja Extensions
JINJA_EXTENSIONS =['jinja2.ext.loopcontrols',]
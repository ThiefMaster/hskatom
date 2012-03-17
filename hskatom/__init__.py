# vim: fileencoding=utf8

import re
from flask import Flask, render_template, request
from flask.ext.cache import Cache
from werkzeug.contrib.atom import AtomFeed
from werkzeug.routing import BaseConverter

# Initialize application
app = Flask(__name__)
app.config.from_pyfile('hskatom.cfg')
cache = Cache(app)

# Config vars
NEWS_URLS = app.config.setdefault('NEWS_URLS', {})
FEED_TITLE = app.config.setdefault('FEED_TITLE', 'Hochschule Karlsruhe - News')
NEWS_CACHE_DURATION = app.config.setdefault('NEWS_CACHE_DURATION', 3600)

# Url argument converter
class NewsKeyConverter(BaseConverter):
    """Matches a news key"""

    def __init__(self, map):
        BaseConverter.__init__(self, map)
        self.regex = '(?:%s)' % '|'.join([re.escape(x) for x in NEWS_URLS])
app.url_map.converters['newskey'] = NewsKeyConverter

# Utility functions
@cache.memoize(NEWS_CACHE_DURATION)
def retrieve_news(key):
    url = NEWS_URLS[key]
    return None

# View functions
@app.route('/')
def index():
    return render_template('index.html', newskeys=NEWS_URLS.keys())

@app.route('/<newskey:key>.atom')
def atom(key):
    retrieve_news(key)
    feed = AtomFeed(FEED_TITLE, feed_url=request.url, url=request.host_url,
        subtitle=key)
    return feed.get_response()

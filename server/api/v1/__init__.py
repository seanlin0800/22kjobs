from flask.ext.restful.representations import json

from .views import blueprint


json.settings['ensure_ascii'] = False

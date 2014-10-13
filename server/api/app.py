from flask import Flask

from .v1 import blueprint
from .models import db


def req_end(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE')
    return response


def create_app():
    app = Flask(__name__, static_url_path='')
    app.config.from_object('config')
    app.after_request(req_end)
    db.init_app(app)
    app.register_blueprint(blueprint, url_prefix='/api/v1')
    return app

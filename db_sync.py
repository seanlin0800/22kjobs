from server.api import create_app
from server import config
from server.db import api as db_api

app = create_app(config.get_config())


with app.app_context():
    db_api.create_all()

from server.api import create_app
from server import config


if __name__ == '__main__':
    app = create_app(config.get_config())
    app.run()

from flask import Flask

from app.ping import ping

ACTIVE_ENDPOINTS = (("/", ping),)


def create_app():
    app = Flask(__name__)

    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_refix=url)

    return app

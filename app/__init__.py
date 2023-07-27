import os

from flask import Flask

from app.api import user_bp
from app.ping import ping
from app.utils.db_manager import db

ACTIVE_ENDPOINTS = (
    ("/", ping),
    ("/leasing/v1", user_bp),
)


def create_app():
    """Create Flask app."""
    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://{}:{}@{}/{}".format(
        os.getenv("DB_USER", "flask"),
        os.getenv("DB_PASSWORD", ""),
        os.getenv("DB_HOST", "mysql"),
        os.getenv("DB_NAME", "flask"),
    )
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = True

    db.init_app(app)

    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    with app.app_context():
        db.create_all()

    return app

import os

from db import db
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_smorest import Api
from resources.note import blp as NoteBlueprint
from resources.tag import blp as TagBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "The Note REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/doc"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.getenv(
            "DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)

    api.register_blueprint(NoteBlueprint)
    api.register_blueprint(TagBlueprint)

    return app

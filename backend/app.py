import os

from db import db
from flask import Flask, jsonify
from flask.views import MethodView
from flask_migrate import Migrate
from flask_smorest import Api, Blueprint, abort

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "The Note REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/\
                                        npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

api = Api(app)


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'test route'})

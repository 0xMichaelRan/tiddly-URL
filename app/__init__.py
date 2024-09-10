from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import ReadConfig

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    config = ReadConfig.readconfig("./local_config.json")

    app.secret_key = config["key_secret"]

    app.config["SQLALCHEMY_DATABASE_URI"] = config["databaseAddr"]
    app.config["SQLALCHEMY_COMMIT_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    from .main import main as blueprint_main
    from .api import api as blueprint_api

    app.register_blueprint(blueprint_api)
    app.register_blueprint(blueprint_main)
    db.init_app(app)
    jwt = JWTManager(app)

    return app

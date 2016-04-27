import os
from flask import Flask
from config import config
from app.main.bot import main as main_blueprint
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)


def create_app(config_name):
    app.config.from_object(config[config_name])
    return app

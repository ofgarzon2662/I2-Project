import os

from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy

from .blueprints.controller import controller_blueprint
from .errors.errors import ApiException
from .models.model import db

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')
db_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_SQLITE', db_uri)
app.register_blueprint(controller_blueprint)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


@app.errorhandler(ApiException)
def handle_exception(exception):
    return make_response(''), exception.code

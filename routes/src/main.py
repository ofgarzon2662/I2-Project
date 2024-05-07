from flask import Flask, make_response, jsonify
from .models.model import db
from .blueprints.routes import routes_blueprint
from .errors.errors import ApiException
import os

db_user = os.environ.get('DB_ROUTE', "postgres")
db_password = os.environ.get('DB_PASSWORD', "postgres")
db_host = os.environ.get('DB_HOST', "127.0.0.1")
db_port = os.environ.get('DB_PORT', "5432")
db_name = os.environ.get('DB_NAME', "monitor_routes")
db_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_SQLITE', db_uri)
app.register_blueprint(routes_blueprint)

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


@app.errorhandler(ApiException)
def handle_exception(exception):
    if exception.description is not None:
        response = {
            "msg": exception.description
        }
        return jsonify(response), exception.code
    
    return make_response(''), exception.code



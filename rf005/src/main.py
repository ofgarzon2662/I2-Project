from flask import Flask, make_response

from .blueprints.rf005 import rf005_blueprint
from .errors.api_exception import ApiException

app = Flask(__name__)
app.register_blueprint(rf005_blueprint)

app_context = app.app_context()
app_context.push()


@app.errorhandler(ApiException)
def handle_exception(exception):
    return make_response({'msg': exception.message}), exception.code

from dotenv import load_dotenv
loaded = load_dotenv('.env.development')

from flask import Flask, jsonify
from .blueprints.operations import operations_blueprint
from .errors.errors import ApiError
import os

app = Flask(__name__)
app.register_blueprint(operations_blueprint)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description,
      "version": os.environ["VERSION"]
    }
    return jsonify(response), err.code

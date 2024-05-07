from flask import Flask, jsonify, request, Blueprint
from ..commands.sum import Sum
from ..commands.divide import Divide
from ..commands.multiply import Multiply
import os

operations_blueprint = Blueprint('operations', __name__)

@operations_blueprint.route('/sum', methods = ['POST'])
def sum():
    json = request.get_json()
    result = Sum(json['x'], json['y']).execute()
    return jsonify({ 'sum': str(result), 'version': os.environ["VERSION"] })

@operations_blueprint.route('/multiply', methods = ['POST'])
def multiply():
    json = request.get_json()
    result = Multiply(json['x'], json['y']).execute()
    return jsonify({ 'multiplication': str(result), 'version': os.environ["VERSION"] })

@operations_blueprint.route('/divide', methods = ['POST'])
def divide():
    json = request.get_json()
    result = Divide(json['x'], json['y']).execute()
    return jsonify({ 'division': str(result), 'version': os.environ["VERSION"] })

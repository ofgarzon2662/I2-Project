from flask import Blueprint, jsonify, request

from ..commands.auth import Auth
from ..commands.create import Create
from ..commands.get_by_token import GetByToken
from ..commands.reset import Reset
from ..commands.update import Update

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/users', methods=['POST'])
def create_user():
    request_json = request.get_json()
    result = Create(request_json.get('username', None), request_json.get('password', None),
                    request_json.get('email', None), request_json.get('dni', None),
                    request_json.get('fullName', None), request_json.get('phoneNumber', None)).execute()
    return jsonify({'id': result['id'], 'createdAt': result['createdAt']}), 201


@controller_blueprint.route('/users/<string:id>', methods=['PATCH'])
def update_user(id):
    request_json = request.get_json()
    Update(id, request_json.get('status', None), request_json.get('dni', None),
           request_json.get('fullName', None), request_json.get('phoneNumber', None)).execute()
    return jsonify({'msg': 'el usuario ha sido actualizado'})


@controller_blueprint.route('/users/auth', methods=['POST'])
def auth_user():
    request_json = request.get_json()
    result = Auth(request_json.get('username', None), request_json.get('password', None)).execute()
    return jsonify({'id': result['id'], 'token': result['token'], 'expireAt': result['expireAt']})


@controller_blueprint.route("/users/me", methods=['GET'])
def get_user_by_token():
    result = GetByToken(request.headers.get('Authorization', None)).execute()
    return jsonify(
        {"id": result['id'], "username": result['username'], "email": result['email'], "fullName": result['fullName'],
         "dni": result['dni'], "phoneNumber": result['phoneNumber'], "status": result['status']})


@controller_blueprint.route("/users/ping", methods=['GET'])
def healthcheck():
    return jsonify('pong'), 200


@controller_blueprint.route("/users/reset", methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"})

from ..errors.errors import PreconditionFailedException
from flask import Flask, jsonify, request, Blueprint
from ..commands.consultar import Consultar
from ..commands.eliminar import Eliminar
from ..commands.filtrar import Filtrar
from ..commands.reset import Reset
from ..commands.create import Create
from flask import current_app as app

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/posts', methods=['POST'])
def create_post():
    request_json = request.get_json()
    try:
        result = Create(
                request.headers.get('Authorization', None),
                request_json.get('routeId', None),
                request_json.get('expireAt', None)
            ).execute()
        return jsonify({'id': result['id'], 'userId': result['userId'], 'createdAt': result['createdAt']}), 201
    except Exception as e:
        if e.code == 412:
            return jsonify(
                {
                    'msg': PreconditionFailedException.msg
                    }
                ), 412
        raise e

    



@controller_blueprint.route('/posts', methods=['GET'])
def filtrar_post():
    token = request.headers.get('Authorization', None)
    expire = request.args.get('expire', default=None)  # Example default=None, you can set it to 'true' or 'false' as needed
    route = request.args.get('route', default=None)  # Default is None or provide a default routeId
    owner = request.args.get('owner', default=None)  # Default is None or provide a default userId (or 'me' for the current user
    result = Filtrar(
        token,
        expire,
        route,
        owner
    ).execute()
    return jsonify(result), 200


@controller_blueprint.route('/posts/<string:id>', methods=['GET'])
def consultar_post(id):
    result = Consultar(request.headers.get('Authorization', None), id).execute()
    return jsonify(
        {
            'id': result['id'],
            'routeId': result['routeId'], 
            'expireAt': result['expireAt'],
            'userId': result['userId'],
            'createdAt': result['createdAt']}
    ), 200

@controller_blueprint.route('/posts/<string:id>', methods=['DELETE'])
def eliminar_post(id):
    Eliminar(request.headers.get('Authorization', None), id).execute()
    return jsonify(
        {'msg': 'la publicación fue eliminada'}
    ), 200

@controller_blueprint.route("/posts/ping", methods=['GET'])
def healthcheck():
    return jsonify('pong'), 200

@controller_blueprint.route("/posts/reset", methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({"msg": "Todos los datos fueron eliminados"}), 200

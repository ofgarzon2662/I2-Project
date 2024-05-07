from flask import Blueprint, request

from ..commands.get import Get

rf005_blueprint = Blueprint('controller', __name__)


@rf005_blueprint.route('/rf005/posts/<string:id>', methods=['GET'])
def get_post(id):
    result = Get(
        request.headers.get('Authorization', None),
        id).execute()
    return result, 200


@rf005_blueprint.route("/rf005/posts/ping", methods=['GET'])
def healthcheck():
    return 'pong', 200

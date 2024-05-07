from flask import Blueprint, request

from ..commands.create import Create

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/rf004/posts/<string:id>/offers', methods=['POST'])
def create_post(id):
    request_json = request.get_json()
    result = Create(
        request.headers.get('Authorization', None),
        id,
        request_json.get("description", None),
        request_json.get("size", None),
        request_json.get("fragile", None),
        request_json.get("offer", None)).execute()
    return result, 201


@controller_blueprint.route("/rf004/posts/ping", methods=['GET'])
def healthcheck():
    return 'pong', 200
from flask import Blueprint, request

from ..commands.create import Create

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/rf003/posts', methods=['POST'])
def create_post():
    request_json = request.get_json()
    result = Create(
        request.headers.get('Authorization', None),
        request_json.get("flightId", None),
        request_json.get("plannedStartDate", None),
        request_json.get("plannedEndDate", None),
        request_json.get("origin", {}).get("airportCode", None),
        request_json.get("origin", {}).get("country", None),
        request_json.get("destiny", {}).get("airportCode", None),
        request_json.get("destiny", {}).get("country", None),
        request_json.get("bagCost", None),
        request_json.get("expireAt", None)).execute()
    return result, 201


@controller_blueprint.route("/rf003/posts/ping", methods=['GET'])
def healthcheck():
    return 'pong', 200

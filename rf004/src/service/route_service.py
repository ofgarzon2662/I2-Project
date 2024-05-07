import os

import requests

from ..errors.api_exception import ApiException


def get_route_by_id(
        token,
        routeId):
    response = requests.get(
        os.environ.get('ROUTES_PATH') + "/routes/" + routeId,
        headers={"Authorization": token})
    if response.status_code == 200:
        return response.json()
    raise ApiException(response.status_code, response.json().get("msg") if response.text else None)
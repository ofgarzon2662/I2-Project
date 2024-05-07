import requests
import os

from ..errors.api_exception import ApiException


def get_user(token):
    response = requests.get(
        os.environ.get('USERS_PATH') + "/users/me",
        headers={"Authorization": token})
    if response.status_code == 200:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)

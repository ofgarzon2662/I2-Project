import requests
import os

from ..errors.api_exception import ApiException


def get_post_by_route_id(
        token,
        routeId):
    response = requests.get(
        os.environ.get('POSTS_PATH') + "/posts?route=" + routeId,
        headers={"Authorization": token})
    if response.status_code == 200:
        json = response.json()
        return json
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)


def create_post(
        token,
        routeId,
        expiredAt):
    response = requests.post(
        os.environ.get('POSTS_PATH') + "/posts",
        json={
            'routeId': routeId,
            'expireAt': expiredAt},
        headers={"Authorization": token})
    if response.status_code == 201:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)


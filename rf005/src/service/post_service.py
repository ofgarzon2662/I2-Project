import requests
import os

from ..errors.api_exception import ApiException


def get_post_by_id(
        token,
        postId):
    response = requests.get(
        os.environ.get('POSTS_PATH') + "/posts/" + postId,
        headers={"Authorization": token})
    if response.status_code == 200:
        return response.json()
    raise ApiException(response.status_code, response.json().get("msg") if response.text else None)

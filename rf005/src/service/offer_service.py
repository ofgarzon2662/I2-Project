import requests
import os

from ..errors.api_exception import ApiException


def get_offer_by_post_id(
        token,
        postId):
    response = requests.get(
        os.environ.get('OFFERS_PATH') + "/offers?post=" + postId,
        headers={"Authorization": token})
    if response.status_code == 200:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)

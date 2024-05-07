import requests
import os

from ..errors.api_exception import ApiException


def create_offer(
        token,
        postId,
        description,
        size,
        fragile,
        offer):
    response = requests.post(
        os.environ.get('OFFERS_PATH') + "/offers",
        json={
            'postId': postId,
            'description': description,
            'size': size,
            'fragile': fragile,
            'offer': offer},
        headers={"Authorization": token})
    if response.status_code == 201:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)

def delete_offer(
        token,
        offerId):
    response = requests.delete(
        os.environ.get('OFFERS_PATH') + "/offers/" + offerId,
        headers={"Authorization": token})
    if response.status_code == 200:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)
import requests
import os

from ..errors.api_exception import ApiException


def create_score(
        idOffer,
        idPost,
        idUserPost,
        idUser,
        size,
        bagCost,
        offer):
    response = requests.post(
        os.environ.get('SCORE_PATH') + "/scores",
        json={
            'idOffer': idOffer,
            'idPost': idPost,
            'idUserPosting': idUserPost,
            'idUserOffering': idUser,
            'ocupancy': size,
            'bagCost': bagCost,
            'offer': offer
        })
    if response.status_code == 201:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)


def delete_score(
        idScore):
    response = requests.delete(
        os.environ.get('SCORE_PATH') + "/scores/" + idScore)
    if response.status_code == 200:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)

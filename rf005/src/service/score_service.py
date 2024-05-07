import requests
import os

from ..errors.api_exception import ApiException

def calculate_score(offerId):
    response = requests.get(
        os.environ.get('SCORE_PATH') + "/scores/offers/" + offerId)
    if response.status_code == 200:
        return response.json()
    raise ApiException(
        response.status_code,
        response.json().get("msg") if response.text else None)
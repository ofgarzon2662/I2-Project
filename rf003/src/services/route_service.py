import os

import requests

from ..errors.api_exception import ApiException


def get_route_by_flight_id(
        token,
        flightId):
    response = requests.get(
        os.environ.get('ROUTES_PATH') + "/routes?flight=" + (flightId if flightId else "None"),
        headers={"Authorization": token})
    if response.status_code == 200:
        return response.json()
    raise ApiException(response.status_code, response.json().get("msg") if response.text else None)


def create_route(
        token,
        flightId,
        plannedStartDate,
        plannedEndDate,
        sourceAirportCode,
        sourceCountry,
        destinyAirportCode,
        destinyCountry,
        bagCost):
    response = requests.post(
        os.environ.get('ROUTES_PATH') + "/routes",
        json={
            'flightId': flightId,
            'plannedStartDate': plannedStartDate,
            'plannedEndDate': plannedEndDate,
            'sourceAirportCode': sourceAirportCode,
            'sourceCountry': sourceCountry,
            'destinyAirportCode': destinyAirportCode,
            'destinyCountry': destinyCountry,
            'bagCost': bagCost},
        headers={"Authorization": token})
    if response.status_code == 201:
        return response.json()
    raise ApiException(response.status_code, response.json().get("msg") if response.text else None)


def delete_route(
        token,
        routeId):
    response = requests.delete(
        os.environ.get('ROUTES_PATH') + "/routes/" + routeId,
        headers={"Authorization": token})
    if response.status_code != 200:
        raise ApiException(response.status_code, response.json().get("msg") if response.text else None)

from src.errors.errors import BadRequestException, FlightIdAlreadyExits, InvalidDate, TokenInvalid, NotToken
from ..models.model import db
from ..models.route import Route
from datetime import datetime, date
import uuid
import requests
import os


def validate_not_blank(*fields):
    for field in fields:
        if field is None:
            raise BadRequestException


def validate_at_least_one_not_blank(*fields):
    for field in fields:
        if field is not None:
            return
    raise BadRequestException

def validate_flightId_not_exits(flightId):
    route = Route.query.filter(Route.flightId == flightId).first()
    if route is not None:
        raise FlightIdAlreadyExits
    
def validate_iso8601_datetime_not_past(*fields):
    for field in fields:
        try:
            parsed_date = datetime.fromisoformat(field.replace('Z', '+00:00'))
            if parsed_date.date() < date.today():
                raise InvalidDate
        except ValueError:
            raise InvalidDate

def validate_date_range(startdate, enddate):
    try:
        startdate = datetime.fromisoformat(startdate.replace('Z', '+00:00'))
        enddate = datetime.fromisoformat(enddate.replace('Z', '+00:00'))
        if enddate < startdate:
            raise InvalidDate
    except ValueError:
        raise InvalidDate

def validate_user_identity(token):
    response = requests.get(os.environ.get('USERS_PATH', "http://localhost:3000") + "/users/me", headers={"Authorization":token})
    if response.status_code == 401:
        raise TokenInvalid
    if response.status_code == 403:
        raise NotToken
    
def validate_values_UUID(variable):
    try:
        uuid_obj = uuid.UUID(str(variable))
        return str(uuid_obj) == variable
    except ValueError:
        raise BadRequestException    
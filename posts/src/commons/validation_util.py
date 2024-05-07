from datetime import datetime

from src.errors.errors import ExpireAtPreconditionFailedException
from ..errors.errors import BadRequestException



def validate_not_blank(*fields):
    for field in fields:
        if field is None or len(field) == 0:
            raise BadRequestException


def validate_at_least_one_not_blank(*fields):
    for field in fields:
        if field is not None:
            return
    raise BadRequestException

def validate_date_greater_than_now(date):
    if date <= datetime.now():
        raise ExpireAtPreconditionFailedException

def validate_date_is_valid_iso_format(date):
    try:
        
        datetime.fromisoformat(date)
    except ValueError:
        raise ExpireAtPreconditionFailedException

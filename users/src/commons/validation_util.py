from src.errors.errors import BadRequestException


def validate_not_blank(*fields):
    for field in fields:
        if field is None or len(field) == 0:
            raise BadRequestException


def validate_at_least_one_not_blank(*fields):
    for field in fields:
        if field is not None:
            return
    raise BadRequestException

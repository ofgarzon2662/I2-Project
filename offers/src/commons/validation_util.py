from ..errors.errors import NotAttributes
from ..errors.errors import AttributeInvalid
from ..errors.errors import InvalidUUID
import uuid

def validate_not_blank(*fields):
    for field in fields:
        if field is None or len(str(field)) == 0:
            raise NotAttributes

def validate_values_size(size):
    if size != "LARGE" and size != "MEDIUM" and size != "SMALL":
        raise AttributeInvalid
    
def validate_values_fragile(fragile):
    if fragile != True and fragile != False:
        raise AttributeInvalid

def validate_values_UUID(variable):
    try:
        uuid_obj = uuid.UUID(str(variable))
        return str(uuid_obj) == variable
    except ValueError:
        raise InvalidUUID

def validate_offer_negative(offer):
    if offer < 0:
        raise AttributeInvalid
    
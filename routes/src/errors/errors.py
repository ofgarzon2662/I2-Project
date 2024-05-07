class ApiException(Exception):
    code = 500
    description = None

class BadRequestException(ApiException):
    code = 400
    description = None

class NotFoundException(ApiException):
    code = 404
    description = None

class TokenInvalid(ApiException):
    code = 401
    description = None

class NotToken(ApiException):
    code = 403
    description = None

class FlightIdAlreadyExits(ApiException):
    code = 412
    description = None

class InvalidDate(ApiException):
    code = 412   
    description = "Las fechas del trayecto no son válidas"    
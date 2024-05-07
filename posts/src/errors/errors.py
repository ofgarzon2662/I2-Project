class ApiException(Exception):
    code = 500


class BadRequestException(ApiException):
    code = 400
    msg = "Campo Vacio o formato no valido"


class PreconditionFailedException(ApiException):
    code = 412
    msg = "La fecha expiración no es válida"


class NotFoundException(ApiException):
    code = 404


class UnauthorizedException(ApiException):
    code = 401
    msg = "El token no es válido o está vencido."


class ForbiddenException(ApiException):
    code = 403
    msg = "No hay token en la solicitud"

class ExpireAtPreconditionFailedException(ApiException):
    code = 412
    msg = "La fecha expiración no es válida"
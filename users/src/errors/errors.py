class ApiException(Exception):
    code = 500


class BadRequestException(ApiException):
    code = 400


class PreconditionFailedException(ApiException):
    code = 412


class NotFoundException(ApiException):
    code = 404


class UnauthorizedException(ApiException):
    code = 401


class ForbiddenException(ApiException):
    code = 403

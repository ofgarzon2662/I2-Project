class ApiError(Exception):
    code = 422
    description = "Default message"

class CantDivideByZero(ApiError):
    code = 400
    description = "Cant divide by zero"

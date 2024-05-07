class ApiException(Exception):
    code = 500

class TokenInvalid(ApiException):
    code = 401
    description = "El token no es válido o está vencido"

class NotToken(ApiException):
    code = 403
    description = "No hay token en la solicitud"

class NotAttributes(ApiException):
    code = 400
    description = "Alguno de los campos no está presente en la solicitudo no tienen el formato esperado"

class AttributeInvalid(ApiException):
    code = 412
    description = "Los valores no están entre lo esperado o la oferta es negativa"

class InvalidUUID(ApiException):
    code = 400
    description = "El id no es un valor string con formato uuid."

class offerNotexists(ApiException):
    code = 404
    description = "La oferta con ese id no existe."
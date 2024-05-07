from abc import ABC
import uuid
from .base_command import BaseCommannd
from ..errors.errors import BadRequestException, ForbiddenException
from ..models.score import Score, ScoreSchema
from ..commons.validation_util import validate_not_blank

# Metodo para retornar el score de una sola OfferID
class GetByOfferID(BaseCommannd, ABC):
    def __init__(self, idOffer):
        self.idOffer = idOffer
    def execute(self):
        # verificamos que idOffer no esta vacio
        validate_not_blank(self.idOffer)
         # Verificamos que el id sea un valor válido
        try:
            uuid.UUID(self.idOffer, version=4)
        except ValueError:
            raise BadRequestException # 400
        # Buscamos el score que tenga el idOffer
        score = Score.query.filter_by(idOffer=self.idOffer).all()
        # verificamos que score sea len = 1
        if len(score) != 1:
            raise ForbiddenException
        # retornamos el score
        return ScoreSchema().dump(score[0])
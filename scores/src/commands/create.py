import uuid
from abc import ABC

from .base_command import BaseCommannd
from ..commons.validation_util import validate_not_blank
from ..errors.errors import BadRequestException
from ..models.model import db
from ..models.score import Score, ScoreSchema


# Create a new Score instance
class Create(BaseCommannd, ABC):

    def __init__(self, idOffer, idPost, idUserPosting, idUserOffering, ocupancy, bagCost, offer):
        self.idOffer = idOffer
        self.idPost = idPost
        self.idUserPosting = idUserPosting
        self.idUserOffering = idUserOffering
        self.ocupancy = ocupancy
        self.bagCost = bagCost
        self.offer = offer

    def execute(self):
        # Verificamos que ninguno de los campos esta vacio
        validate_not_blank(self.idOffer, self.idPost, self.idUserPosting, self.idUserOffering, self.ocupancy,
                           self.bagCost, self.offer)
        # Verificamos que idOffer, idPost, idUserPosting, idUserOffering sean uuid
        try:
            uuid.UUID(self.idOffer, version=4)
            uuid.UUID(self.idPost, version=4)
            uuid.UUID(self.idUserPosting, version=4)
            uuid.UUID(self.idUserOffering, version=4)
        except ValueError:
            raise BadRequestException
        # verificamos que ocupancy sea un string
        if not isinstance(self.ocupancy, str):
            raise BadRequestException
        # verificamos que bagCost y offer sean numeros
        if not isinstance(self.bagCost, (int, float)) or not isinstance(self.offer, (int, float)):
            raise BadRequestException
        # Creamos el nuevo Score
        score = Score(idOffer=self.idOffer,
                      idPost=self.idPost,
                      idUserOffering=self.idUserOffering,
                      idUserPosting=self.idUserPosting,
                      ocupancy=self.ocupancy,
                      bagCost=self.bagCost,
                      offer=self.offer,
                      score=self.calculate_score())
        db.session.add(score)
        db.session.commit()
        return ScoreSchema().dump(score)

    def calculate_score(self):
        validate_not_blank(self.ocupancy, self.bagCost, self.offer)
        if not isinstance(self.ocupancy, str):
            raise BadRequestException
        if not isinstance(self.bagCost, (int, float)) or not isinstance(self.offer, (int, float)):
            raise BadRequestException
        if self.ocupancy == "LARGE":
            ocupacion = 100
        elif self.ocupancy == "MEDIUM":
            ocupacion = 50
        else:
            ocupacion = 25
        score = self.offer - (ocupacion * self.bagCost) / 100
        return score

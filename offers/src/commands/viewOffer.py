from abc import ABC

from .base_command import BaseCommannd
from .token import Token
from ..commons.validation_util import validate_values_UUID
from ..errors.errors import offerNotexists
from ..models.offer import Offer, OfferSchema


class viewOffer(BaseCommannd, ABC, Token):
    def __init__(self, id, token):
        self.id = id
        self.token = token

    def execute(self):
        self.verify_token(self.token)

        validate_values_UUID(self.id)

        offer = Offer.query.filter(Offer.id == self.id).first()
        if not offer:
            raise offerNotexists
        else:
            return OfferSchema().dump(offer)

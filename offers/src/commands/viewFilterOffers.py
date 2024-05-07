import json
from abc import ABC

from .base_command import BaseCommannd
from .token import Token
from ..commons.validation_util import validate_values_UUID
from ..models.model import db
from ..models.offer import Offer, OfferSchema


class viewFilterOffers(BaseCommannd, ABC, Token):

    def __init__(self, postId, owner, token):
        self.postId = postId
        self.owner = owner
        self.token = token

    def execute(self):
        response = self.verify_token(self.token)
        query = db.session.query(Offer)
        if self.postId:
            query = query.filter(Offer.postId == self.postId)
        if self.owner:
            if self.owner == 'me':
                query = query.filter(Offer.userId == response.json().get('id'))
            else:
                validate_values_UUID(self.owner)
                query = query.filter(Offer.userId == self.owner)
        offers = query.all()
        if not offers:
            return []
        else:
            return [OfferSchema().dump(offer) for offer in offers]

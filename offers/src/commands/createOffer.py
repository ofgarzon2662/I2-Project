import json
from abc import ABC

from .base_command import BaseCommannd
from .token import Token
from ..commons.validation_util import validate_not_blank, validate_values_size, validate_values_fragile, validate_offer_negative
from ..models.offer import Offer, OfferSchema, db


class createOffer(BaseCommannd, ABC, Token):
    def __init__(self, postId, description, size, fragile, offer, token):
        self.postId = postId
        self.description = description
        self.size = size
        self.fragile = fragile
        self.offer = offer
        self.token = token

    def execute(self):
        response = self.verify_token(self.token)
        user_id = json.loads(response.text)['id']

        validate_not_blank(self.postId, self.description, self.size, self.fragile, self.offer)
        validate_values_size(self.size)
        validate_values_fragile(self.fragile)
        validate_offer_negative(self.offer)

        offer = Offer(postId=self.postId, userId=user_id, description=self.description,
                      size=self.size, fragile=self.fragile, offer=self.offer)
        db.session.add(offer)
        db.session.commit()
        return OfferSchema().dump(offer)
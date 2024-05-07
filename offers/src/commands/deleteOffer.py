from .base_command import BaseCommannd
from ..commons.validation_util import validate_values_UUID
from ..models.offer import Offer, db
from ..errors.errors import NotToken, offerNotexists, TokenInvalid
from datetime import datetime
import requests, os
from .token import Token
from abc import ABC

class deleteOffer(BaseCommannd, ABC, Token):
  def __init__(self, id, token):
    self.id = id
    self.token = token
  
  def execute(self):
    response = self.verify_token(self.token)
    
    validate_values_UUID(self.id)

    offer = Offer.query.filter(Offer.id == self.id).all()
    if not offer:
      raise offerNotexists
    
    offer = Offer.query.filter(Offer.id == self.id).delete()
    db.session.commit()
    
    return {"msg":"la oferta fue eliminada"}

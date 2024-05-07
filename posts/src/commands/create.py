from datetime import datetime
from abc import ABC
import json

from .token import Token
from .base_command import BaseCommannd
from ..models.post import Post, PostSchema
from ..models.model import db
from ..commons.validation_util import validate_not_blank, validate_date_greater_than_now, validate_date_is_valid_iso_format


class Create(BaseCommannd, ABC, Token):

  def __init__(self, token, routeId, expireAt):
    self.token = token
    self.routeId = routeId
    self.expireAt = expireAt

  def execute(self):
    response = self.verify_token(self.token)
    user_id = json.loads(response.text)['id']
    validate_not_blank(self.routeId, self.expireAt)
    validate_date_is_valid_iso_format(self.expireAt[:-1])
    expire_at_datetime = datetime.fromisoformat(self.expireAt[:-1])
    # Verificamos campos no nulos
    validate_date_greater_than_now(expire_at_datetime)
   # Creamos la publicación
    post = Post(
      routeId = self.routeId, 
      userId = user_id,
      expireAt=expire_at_datetime,
      createdAt = datetime.now()
      )
    db.session.add(post)
    db.session.commit()
    return PostSchema().dump(post)

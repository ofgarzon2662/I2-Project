import datetime
from abc import ABC
import uuid
from .base_command import BaseCommannd
from ..models.post import Post, PostSchema
from .token import Token
from ..models.model import db
from ..errors.errors import BadRequestException, NotFoundException

class Eliminar(BaseCommannd, ABC, Token):
    def __init__(self, token, id):
        self.id = id
        self.token = token

    def execute(self):
        # Validamos el token
        self.verify_token(self.token)
        # Verificamos que el id sea un valor válido
        try:
            uuid.UUID(self.id, version=4)
        except ValueError:
            raise BadRequestException # 400
        
        post = Post.query.get(self.id)
        if post is None:
            raise NotFoundException # 404
        
        # Eliminar la publicación
        db.session.delete(post)
        db.session.commit()

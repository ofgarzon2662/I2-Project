import uuid
from abc import ABC

from .base_command import BaseCommannd
from .token import Token
from ..errors.errors import BadRequestException, NotFoundException
from ..models.post import Post, PostSchema

class Consultar(BaseCommannd, ABC,Token):
    def __init__(self, token, id):
        self.token = token
        self.id = id

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
        return PostSchema().dump(post)
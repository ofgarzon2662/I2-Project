import datetime
import json
from abc import ABC
from .token import Token
from .base_command import BaseCommannd
from ..models.post import Post, PostSchema
from ..errors.errors import BadRequestException


class Filtrar(BaseCommannd, ABC, Token):

    def __init__(self, token, expire, route, owner):
        self.token = token
        self.expire = expire
        self.route = route
        self.owner = owner

    def execute(self):
        # Validamos el Token:
        response = self.verify_token(self.token)
        user_id = json.loads(response.text)['id']
        # Validamos que expire sea booleano
        if self.expire:
            if self.expire != 'true' and self.expire != 'false':
                raise BadRequestException # 400
        # Validamos que route sea una cadena de caracteres
        if self.route:
            if not isinstance(self.route, str):
                raise BadRequestException # 400
        # Validamos que owner sea una cadena de caracteres, o la cadena 'me'
        if self.owner:
            if not isinstance(self.owner, str):
                raise BadRequestException # 400
        # Si los tres campos están vacíos, se retornan todas las publicaciones
        query = Post.query
        #result =  PostSchema(many=True).dump(Post.query.all())
        if not self.expire and not self.route and not self.owner:
            return PostSchema(many=True).dump(query.all())
        # Si expire es true, se retornan las publicaciones que no han expirado
        if self.expire is not None:
            if self.expire == 'true':
                query = query.filter(Post.expireAt < datetime.datetime.now()) 
                # Si expire es false, se retornan las publicaciones que han expirado
            else:
                query = query.filter(Post.expireAt > datetime.datetime.now())
        # Si route está definido, se retornan las publicaciones con ese routeId
        if self.route:
            query = query.filter(Post.routeId == self.route)
        # Si owner está definido, se retornan las publicaciones con ese userId
        if self.owner:
            if self.owner == 'me':
                query = query.filter(Post.userId == user_id)
            else:
                query = query.filter(Post.userId == self.owner)
        return PostSchema(many=True).dump(query.all())
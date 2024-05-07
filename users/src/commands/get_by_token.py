from abc import ABC
from datetime import datetime

from ..commands.base_command import BaseCommand
from ..errors.errors import ForbiddenException, UnauthorizedException
from ..models.user import User, UserSchema


class GetByToken(BaseCommand, ABC):

    def __init__(self, token):
        self.token = token

    def execute(self):
        if self.token is None:
            raise ForbiddenException
        user = User.query.filter(User.token == self.token.replace('Bearer ', ''),
                                 datetime.now() <= User.expireAt).first()
        if not user:
            raise UnauthorizedException
        return UserSchema().dump(user)

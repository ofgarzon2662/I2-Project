import hashlib
import uuid
from abc import ABC
from datetime import datetime, timedelta

from ..commands.base_command import BaseCommand
from ..commons.validation_util import validate_not_blank
from ..errors.errors import NotFoundException
from ..models.model import db
from ..models.user import User, UserSchema


class Auth(BaseCommand, ABC):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def execute(self):
        validate_not_blank(self.username, self.password)
        user = User.query.filter(User.username == self.username).first()
        if not user:
            raise NotFoundException
        salted_password = user.salt + self.password
        hashed_password = hashlib.md5(salted_password.encode('utf-8')).hexdigest()
        if user.password != hashed_password:
            raise NotFoundException
        user.token = str(uuid.uuid4())
        user.expireAt = datetime.now() + timedelta(hours=1)
        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user)

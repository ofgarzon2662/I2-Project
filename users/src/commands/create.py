import hashlib
import uuid
from abc import ABC

from sqlalchemy import or_

from ..commands.base_command import BaseCommand
from ..commons.validation_util import validate_not_blank
from ..errors.errors import PreconditionFailedException
from ..models.model import db
from ..models.user import User, UserSchema


class Create(BaseCommand, ABC):

    def __init__(self, username, password, email, dni, full_name, phone_number):
        self.username = username
        self.password = password
        self.email = email
        self.dni = dni
        self.full_name = full_name
        self.phone_number = phone_number

    def execute(self):
        validate_not_blank(self.username, self.password, self.email)
        if User.query.filter(or_(User.username == self.username, User.email == self.email)).first():
            raise PreconditionFailedException
        salt = str(uuid.uuid4())
        salted_password = salt + self.password
        hashed_password = hashlib.md5(salted_password.encode('utf-8')).hexdigest()
        user = User(username=self.username, password=hashed_password, email=self.email, salt=salt)
        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user)

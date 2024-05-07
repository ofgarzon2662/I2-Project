from abc import ABC

from ..commands.base_command import BaseCommand
from ..commons.validation_util import validate_at_least_one_not_blank
from ..errors.errors import NotFoundException
from ..models.model import db
from ..models.user import UserSchema, User


class Update(BaseCommand, ABC):

    def __init__(self, id, status, dni, full_name, phone_number):
        self.id = id
        self.status = status
        self.dni = dni
        self.full_name = full_name
        self.phone_number = phone_number

    def execute(self):
        validate_at_least_one_not_blank(self.status, self.dni, self.full_name, self.phone_number)
        user = User.query.filter(User.id == self.id).first()
        if not user:
            raise NotFoundException
        if self.status is not None:
            user.status = self.status
        if self.dni is not None:
            user.dni = self.dni
        if self.full_name is not None:
            user.fullName = self.full_name
        if self.phone_number is not None:
            user.phoneNumber = self.phone_number
        db.session.add(user)
        db.session.commit()

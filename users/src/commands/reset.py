from abc import ABC

from ..commands.base_command import BaseCommand
from ..models.model import db
from ..models.user import User


class Reset(BaseCommand, ABC):

    def execute(self):
        db.session.query(User).delete()
        db.session.commit()

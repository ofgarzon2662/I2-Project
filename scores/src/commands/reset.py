from abc import ABC

from ..commands.base_command import BaseCommannd
from ..models.model import db
from ..models.score import Score


class Reset(BaseCommannd, ABC):

    def execute(self):
        db.session.query(Score).delete()
        db.session.commit()

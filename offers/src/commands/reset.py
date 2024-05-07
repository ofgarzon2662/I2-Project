from abc import ABC

from .base_command import BaseCommannd
from ..models.model import db
from ..models.offer import Offer


class Reset(BaseCommannd, ABC):

    def execute(self):
        db.session.query(Offer).delete()
        db.session.commit()
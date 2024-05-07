from abc import ABC

from .base_command import BaseCommannd
from ..models.model import db
from ..models.post import Post


class Reset(BaseCommannd, ABC):

    def execute(self):
        db.session.query(Post).delete()
        db.session.commit()
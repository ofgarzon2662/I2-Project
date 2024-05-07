from ..commands.base_command import BaseCommand
from ..models.model import db
from ..models.route import Route


class Reset(BaseCommand):

    def execute(self):
        db.session.query(Route).delete()
        db.session.commit()
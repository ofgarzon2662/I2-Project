import uuid
import json
from abc import ABC
from ..models.model import db
from ..errors.errors import BadRequestException, NotFoundException


from ..models.score import Score

from ..commands.base_command import BaseCommannd
from ..errors.errors import PreconditionFailedException
from ..models.model import db

# Delete a  Score instance by score id.
class Delete(BaseCommannd, ABC):
    def __init__(self, id):
        self.id = id
    
    def execute(self):

        # Verificamos que el id sea un valor válido
        try:
            uuid.UUID(self.id, version=4)
        except ValueError:
            raise BadRequestException # 400
        
        # Buscamos el Score
        score = Score.query.filter_by(id=self.id).first()
        if score is None:
            raise NotFoundException #404
        # Borramos el Score
        db.session.delete(score)
        db.session.commit()
    
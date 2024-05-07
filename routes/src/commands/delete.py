from .base_command  import  BaseCommand
from ..models.model import db
from ..models.route import Route
from ..commons.validation_util import validate_values_UUID, validate_user_identity
from src.errors.errors import NotFoundException

class Delete(BaseCommand):
  def __init__(self, id, token):
    self.id = id
    self.token = token
  
  def execute(self):
    
    validate_user_identity(self.token)
    validate_values_UUID(self.id)

    route = Route.query.filter(Route.id == self.id).all()
    if not route:
      raise NotFoundException
    
    route = Route.query.filter(Route.id == self.id).delete()
    db.session.commit()

    return {"msg":"el trayecto fue eliminado"}
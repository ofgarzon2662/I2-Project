from .base_command  import  BaseCommand
from ..models.model import db
from ..models.route import Route, ModelSchema
from ..commons.validation_util import validate_values_UUID, validate_user_identity
from src.errors.errors import NotFoundException

class Detail(BaseCommand):
  def __init__(self, id, token):
    self.id = id
    self.token = token
  
  def execute(self):
    
    validate_user_identity(self.token)
    validate_values_UUID(self.id)

    routes = Route.query.filter(Route.id == self.id).all()
    if not routes:
      raise NotFoundException
    else:
      return ModelSchema().dump(routes[0])
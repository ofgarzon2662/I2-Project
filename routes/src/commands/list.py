from .base_command  import  BaseCommand
from ..models.model import db
from ..models.route import Route, ModelSchema
from ..commons.validation_util import validate_values_UUID, validate_user_identity

class List(BaseCommand):
  def __init__(self, flightId, token):
    self.flightId = flightId
    self.token = token
  
  def execute(self):
    
    validate_user_identity(self.token)
    
    if not self.flightId:
      routes = Route.query.all()
    else:
      routes = Route.query.filter(Route.flightId == self.flightId).all()

    if not routes:
      return ModelSchema().dump([], many=True)
    else:
      return [ModelSchema().dump(route) for route in routes]
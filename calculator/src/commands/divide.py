from .base_command import BaseCommannd
from ..errors.errors import CantDivideByZero

class Divide(BaseCommannd):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def execute(self):
    if(self.y == 0):
      raise CantDivideByZero

    return self.x / self.y

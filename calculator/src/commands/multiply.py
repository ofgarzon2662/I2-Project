from .base_command import BaseCommannd

class Multiply(BaseCommannd):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def execute(self):
    return self.x * self.y

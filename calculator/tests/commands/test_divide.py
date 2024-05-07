from src.commands.divide import Divide
from src.errors.errors import CantDivideByZero

class TestDivide():
  def test_divide_two_number(self):
    result = Divide(5,5).execute()
    assert result == 1

  def test_divide_by_zero(self):
    try:
      Divide(5,0).execute()
    except CantDivideByZero:
      assert True
from src.commands.multiply import Multiply

class TestMultiply():
  def test_multiply_two_number(self):
    result = Multiply(5,6).execute()
    assert result == 30
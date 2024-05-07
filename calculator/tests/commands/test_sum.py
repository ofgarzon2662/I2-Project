from src.commands.sum import Sum

class TestSum():
  def test_sum_two_number(self):
    result = Sum(5,6).execute()
    assert result == 11
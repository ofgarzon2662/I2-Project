from src.main import app
import json
import os

class TestOperations():
  def test_sum_two_number(self):
    with app.test_client() as test_client:
      response = test_client.post(
        '/sum', json={
          'x': 5,
          'y': 6
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 200
      assert 'sum' in response_json
      assert 'version' in response_json

  def test_multiply_two_number(self):
    with app.test_client() as test_client:
      response = test_client.post(
        '/multiply', json={
          'x': 5,
          'y': 6
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 200
      assert 'multiplication' in response_json
      assert 'version' in response_json

  def test_divide_two_number(self):
    with app.test_client() as test_client:
      response = test_client.post(
        '/divide', json={
          'x': 5,
          'y': 6
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 200
      assert 'division' in response_json
      assert 'version' in response_json

  def test_divide_by_zero(self):
    with app.test_client() as test_client:
      response = test_client.post(
        '/divide', json={
          'x': 5,
          'y': 0
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 400
      assert 'mssg' in response_json
      assert 'version' in response_json
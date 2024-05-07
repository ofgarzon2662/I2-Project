import json
from unittest import TestCase
from unittest.mock import patch, Mock

from faker import Faker

from src.main import app


class ControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create_post_1(self):
        request = {
            "flightId": "475",
            "expireAt": "2024-02-28T03:03:41.411Z",
            "plannedStartDate": "2024-02-29T01:18:45.343Z",
            "plannedEndDate": "2024-03-08T01:18:45.343Z",
            "origin": {
                "airportCode": "BOG",
                "country": "Colombia"
            },
            "destiny": {
                "airportCode": "LGW",
                "country": "Inglaterra"
            },
            "bagCost": 463
        }
        user_response = Mock()
        user_response.status_code = 200
        with patch('requests.get', return_value=user_response):
            route_response = Mock()
            route_response.status_code = 200
            route_response.json.return_value = []
            with patch('requests.get', return_value=route_response):
                created_route_response = Mock()
                created_route_response.status_code = 201
                created_route_response.json.return_value = {'id': "caf8959a-fd13-4c0f-916d-4dab479384a3"}
                with patch('requests.post', return_value=created_route_response):
                    post_response = Mock()
                    post_response.status_code = 200
                    post_response.json.return_value = []
                    with patch('requests.get', return_value=post_response):
                        created_post_response = Mock()
                        created_post_response.status_code = 201
                        created_post_response.json.return_value = {'id': "caf8959a-fd13-4c0f-916d-4dab479384a3"}
                        with patch('requests.post', return_value=created_post_response):
                            result = self.test_client.post('/rf003/posts', data=json.dumps(request),
                                                           headers={'Content-Type': 'application/json',
                                                                    'Authorization': 'Bearer token'})
                            self.assertEqual(result.status_code, 201)

    def test_create_post_2(self):
        request = {
            "flightId": "475",
            "expireAt": "2024-02-28T03:03:41.411Z",
            "plannedStartDate": "2024-02-29T01:18:45.343Z",
            "plannedEndDate": "2024-03-08T01:18:45.343Z",
            "origin": {
                "airportCode": "BOG",
                "country": "Colombia"
            },
            "destiny": {
                "airportCode": "LGW",
                "country": "Inglaterra"
            },
            "bagCost": 463
        }
        user_response = Mock()
        user_response.status_code = 200
        with patch('requests.get', return_value=user_response):
            route_response = Mock()
            route_response.status_code = 200
            route_response.json.return_value = [{'id': "caf8959a-fd13-4c0f-916d-4dab479384a3"}]
            with patch('requests.get', return_value=route_response):
                post_response = Mock()
                post_response.status_code = 200
                post_response.json.return_value = []
                with patch('requests.get', return_value=post_response):
                    created_post_response = Mock()
                    created_post_response.status_code = 201
                    created_post_response.json.return_value = {'id': "caf8959a-fd13-4c0f-916d-4dab479384a3"}
                    with patch('requests.post', return_value=created_post_response):
                        result = self.test_client.post('/rf003/posts', data=json.dumps(request),
                                                       headers={'Content-Type': 'application/json',
                                                                'Authorization': 'Bearer token'})
                        self.assertEqual(result.status_code, 201)

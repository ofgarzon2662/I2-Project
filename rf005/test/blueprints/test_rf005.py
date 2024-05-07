import json
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from faker import Faker
import uuid
import random
import os
import pytest

from src.main import app
from src.service.user_service import get_user
from src.service.post_service import get_post_by_id
from src.service.route_service import get_route_by_id
from src.service.offer_service import get_offer_by_post_id
from src.service.score_service import calculate_score
from src.errors.api_exception import ApiException


class TestRf005(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_bad_user_get_offer(self):
        success_response = Mock()
        success_response.status_code = 500
        success_response.text = json.dumps({'msg': "Internal server error"})
        with patch('requests.get', return_value=success_response):
            with pytest.raises(ApiException) as exception:
                get_user('token')
            self.assertEqual(exception.value.code, 500)

    def test_get_offer_post_no_exits(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"})
        with patch('requests.get', return_value=success_response):
            success_response1 = Mock()
            success_response1.status_code = 500
            success_response1.text = json.dumps({'msg': "Internal server error"})
            with patch('requests.get', return_value=success_response1):
                with pytest.raises(ApiException) as exception:
                    get_post_by_id('token', '5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f788')
                self.assertEqual(exception.value.code, 500)

    def test_get_offer_route_no_exits(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.json.return_value = {'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
        with patch('requests.get', return_value=success_response):
            success_response1 = Mock()
            success_response1.status_code = 200
            success_response1.json.return_value =  {'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722", 'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726", 'expireAt': "2024-10-28T03:03:41.411", 'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
            with patch('requests.get', return_value=success_response1):
                success_response2 = Mock()
                success_response2.status_code = 500
                success_response2.text = json.dumps({'msg': "Internal server error"})
                with patch('requests.get', return_value=success_response2):
                    with pytest.raises(ApiException) as exception:
                        get_route_by_id('token', '5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726')
                    self.assertEqual(exception.value.code, 500)

    def test_get_offer_no_exits(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.json.return_value = {'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
        with patch('requests.get', return_value=success_response):
            success_response1 = Mock()
            success_response1.status_code = 200
            success_response1.json.return_value = {'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722", 'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726", 'expireAt': "2024-10-28T03:03:41.411", 'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
            with patch('requests.get', return_value=success_response1):
                success_response2 = Mock()
                success_response2.status_code = 500
                success_response2.text = json.dumps({'msg': "Internal server error"})
                with patch('requests.get', return_value=success_response2):
                    with pytest.raises(ApiException) as exception:
                        get_offer_by_post_id('token', '5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726')
                    self.assertEqual(exception.value.code, 500)

    def test_get_offer(self):

        user_id = "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"
        route_id = "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722"
        post_id = "aeea7fd8-04cc-449b-a163-20864fa5243e"
        createdAt = "2024-01-29T20:25:30.623672"
        expireAt = "2025-03-01T20:25:30.540000"
        flightId = "226"
        sourceAirportCode = "BOG"
        sourceCountry = "Colombia"
        destinyAirportCode = "LGW"
        destinyCountry = "Inglaterra"
        bagCost = 640
        plannedStartDate = "2024-08-02T21:08:21.427000"
        plannedEndDate = "2024-09-10T21:08:21.427000"
        offer1 = {
            'createdAt': createdAt,
            'description': "non nam ut",
            'fragile': False,
            'id': "9d149574-6f4f-48fd-8501-e748fbdb0302",
            'offer': "655.00",
            'postId': "aeea7fd8-04cc-449b-a163-20864fa5243e",
            'score': 0,
            'size': "MEDIUM",
            'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"
        }
        offer_list = [offer1]
        score = 477.0

        # Mock the requests.get method
        with patch('requests.get') as mock_get:
            # Define the side effect to return different responses for different calls
            mock_get.side_effect = [
                MagicMock(status_code=200, json=lambda: {'id': user_id}),
                MagicMock(status_code=200, json=lambda: {'routeId': route_id,
                                                         'id': post_id,
                                                         'createdAt': createdAt,
                                                         'expireAt': expireAt,
                                                         'userId': user_id}),
                MagicMock(status_code=200, json=lambda: {'id': route_id, 'flightId': flightId,
                                                         'sourceAirportCode': sourceAirportCode, 'sourceCountry': sourceCountry,
                                                         'destinyAirportCode': destinyAirportCode, 'destinyCountry': destinyCountry,
                                                         'bagCost': bagCost, 'plannedStartDate': plannedStartDate, 'plannedEndDate': plannedEndDate}),
                MagicMock(status_code=200, json=lambda: offer_list),
                MagicMock(status_code=200, json=lambda: {'score': score})
            ]

            response = self.test_client.get('/rf005/posts/'+str(uuid.uuid4()),
                                                    headers={'Content-Type': 'application/json',
                                                            "Authorization": 'Valid Token'})
                        
            self.assertIn('msg', response.data.decode('utf-8'))
                    

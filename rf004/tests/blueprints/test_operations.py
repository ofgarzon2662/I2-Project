import json
from unittest import TestCase
from unittest.mock import Mock, patch
from faker import Faker
import uuid, random
import os
import pytest

from src.main import app
from src.service.user_service import get_user
from src.service.post_service import get_post_by_id
from src.service.offer_service import create_offer
from src.errors.api_exception import ApiException


class TestOperation(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_bad_user_offer(self):
        success_response = Mock()
        success_response.status_code = 500
        success_response.text = json.dumps({'msg': "Internal server error"})
        with patch('requests.get', return_value=success_response):
            with pytest.raises(ApiException) as exception:
                get_user('token')
            self.assertEqual(exception.value.code, 500)
    
    def test_bad_post_offer(self):
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
    
    def test_bad_expireat_offer(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"})
        with patch('requests.get', return_value=success_response):
            success_response1 = Mock()
            success_response1.status_code = 200
            success_response1.json.return_value = {'expireAt': "1992-09-08T03:03:41.411", 'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722"}
            with patch('requests.get', return_value=success_response1):
                success_response2 = Mock()
                success_response2.status_code = 200
                success_response2.json.return_value = {'expireAt': "1992-09-08T03:03:41.411", 'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722"}
                with patch('requests.get', return_value=success_response2):
                    offer = {
                    "description": self.faker.text(),
                    "size": random.choice(palabras),
                    "fragile": random.choice([True, False]),
                    "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
                    }
                    response = self.test_client.post('/rf004/posts/'+str(uuid.uuid4())+'/offers', data=json.dumps(offer),
                                                headers={'Content-Type': 'application/json',
                                                        "Authorization": 'Valid Token'})
                self.assertEqual(response.status_code, 412)
    
    def test_bad_owner_post(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.json.return_value = {'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
        with patch('requests.get', return_value=success_response):
            success_response1 = Mock()
            success_response1.status_code = 200
            success_response1.json.return_value = {'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722", 'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726", 'expireAt': "2024-10-28T03:03:41.411", 'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
            with patch('requests.get', return_value=success_response1):
                success_response2 = Mock()
                success_response2.status_code = 200
                success_response2.json.return_value = {'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722", 'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726", 'expireAt': "2024-10-28T03:03:41.411", 'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
                with patch('requests.get', return_value=success_response2):
                    offer = {
                    "description": self.faker.text(),
                    "size": random.choice(palabras),
                    "fragile": random.choice([True, False]),
                    "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
                    }
                    response = self.test_client.post('/rf004/posts/'+str(uuid.uuid4())+'/offers', data=json.dumps(offer),
                                                headers={'Content-Type': 'application/json',
                                                        "Authorization": 'Valid Token'})
                self.assertEqual(response.status_code, 412)
    
    def test_bad_create_offer(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 500
        success_response.text = json.dumps({'msg': "Internal server error"})
        with patch('requests.post', return_value=success_response):
            with pytest.raises(ApiException) as exception:
                create_offer('token', '5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726', self.faker.text(), random.choice(palabras), random.choice([True, False]), float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)))
            self.assertEqual(exception.value.code, 500)
    
    def test_succes_create_offer(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 201
        success_response.json.return_value = {'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
        with patch('requests.post', return_value=success_response):
            result = create_offer('token', '5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726', self.faker.text(), random.choice(palabras), random.choice([True, False]), float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)))
        
        self.assertEqual(result.get('id'), "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726")
    
    def test_success_create_offer_api(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.json.return_value = {'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f788"}
        with patch('requests.get', return_value=success_response):
            success_response1 = Mock()
            success_response1.status_code = 200
            success_response1.json.return_value = {'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722", 'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f788", 'expireAt': "2024-10-28T03:03:41.411", 'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
            with patch('requests.get', return_value=success_response1):
                success_response3 = Mock()
                success_response3.status_code = 200
                success_response3.json.return_value = {'routeId':"5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f722", 'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f788", 'expireAt': "2024-10-28T03:03:41.411", 'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726"}
                with patch('requests.get', return_value=success_response3):
                    success_response2 = Mock()
                    success_response2.status_code = 201
                    success_response2.json.return_value = {'msg': '', 'data':{'id': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f799",
                    'userId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f726",
                    'createdAt': "2024-10-28T03:03:41.411",
                    'postId': "5eb5b1c0-8f4d-4e4a-9e7d-7a8df151f788"}}
                    with patch('requests.post', return_value=success_response2):
                        offer = {
                        "description": self.faker.text(),
                        "size": random.choice(palabras),
                        "fragile": random.choice([True, False]),
                        "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
                        }
                        response = self.test_client.post('/rf004/posts/'+str(uuid.uuid4())+'/offers', data=json.dumps(offer),
                                                    headers={'Content-Type': 'application/json',
                                                            "Authorization": 'Valid Token'})
                        
                    self.assertIn('msg', response.data.decode('utf-8'))
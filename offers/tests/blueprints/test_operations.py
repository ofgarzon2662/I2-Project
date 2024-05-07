import json
from unittest import TestCase
from unittest.mock import Mock, patch
from faker import Faker
import uuid, random

from src.main import app


class TestOperation(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create_offer(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": self.faker.text(),
                "size": random.choice(palabras),
                "fragile": random.choice([True, False]),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
    
    def test_postid_blank(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": "",
                "description": self.faker.text(),
                "size": random.choice(palabras),
                "fragile": random.choice([True, False]),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 400)
    
    def test_description_blank(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": "",
                "size": random.choice(palabras),
                "fragile": random.choice([True, False]),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 400)
    
    def test_size_blank(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": self.faker.text(),
                "size": "",
                "fragile": random.choice([True, False]),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 400)
    
    def test_fragile_blank(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": self.faker.text(),
                "size": random.choice(palabras),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 400)
    
    def test_offer_blank(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": self.faker.text(),
                "size": random.choice(palabras),
                "fragile": random.choice([True, False]),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 400)
    
    def test_size_values_bad(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": self.faker.text(),
                "size": self.faker.text(),
                "fragile": random.choice([True, False]),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 412)
    
    def test_fragile_values_bad(self):
        palabras = ["LARGE", "MEDIUM", "SMALL"]
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            offer = {
                "postId": str(uuid.uuid4()),
                "description": self.faker.text(),
                "size": random.choice(palabras),
                "fragile": self.faker.text(),
                "offer": float(self.faker.pydecimal(left_digits=10, right_digits=2, positive=True)),
            }
            response = self.test_client.post('/offers', data=json.dumps(offer),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 412)
    
    def test_validate_uuid_delete(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            response = self.test_client.delete('/offers/'+'1', data=json.dumps(None),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 400)
    
    def test_delete_id_notexist(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': str(uuid.uuid4())})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            response = self.test_client.delete('/offers/'+str(uuid.uuid4()), data=json.dumps(None),
                                             headers={'Content-Type': 'application/json',
                                                      "Authorization": 'Valid Token'})
            self.assertEqual(response.status_code, 404)

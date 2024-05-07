import json
from unittest import TestCase

from faker import Faker

from src.main import app


class ControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create_user(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail'],
            "dni": self.faker.passport_number(),
            "fullName": self.faker.profile()['name'],
            "phoneNumber": self.faker.phone_number()
        }
        response = self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['createdAt'])

    def test_create_user_already_exist(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail']
        }
        self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        response = self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 412)

    def test_create_user_without_mandatory_fields(self):
        user = {
            "fullName": self.faker.profile()['name'],
        }
        response = self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_update_user(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail']
        }
        response = self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        user = {
            "status": "VERIFICADO",
            "dni": self.faker.passport_number(),
            "fullName": self.faker.profile()['name'],
            "phoneNumber": self.faker.phone_number()
        }
        response = self.test_client.patch('/users/' + json.loads(response.get_data())['id'], data=json.dumps(user),
                                          headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data())['msg'], 'el usuario ha sido actualizado')

    def test_update_user_without_fields(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail']
        }
        response = self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        user = {}
        response = self.test_client.patch('/users/' + json.loads(response.get_data())['id'], data=json.dumps(user),
                                          headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_update_user_wit_invalid_fields(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail']
        }
        response = self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        user = {
            "email": self.faker.profile()['mail']
        }
        response = self.test_client.patch('/users/' + json.loads(response.get_data())['id'], data=json.dumps(user),
                                          headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_update_user_not_exists(self):
        user = {
            "status": "VERIFICADO",
            "dni": self.faker.passport_number(),
            "fullName": self.faker.profile()['name'],
            "phoneNumber": self.faker.phone_number()
        }
        response = self.test_client.patch('/users/' + 'NIT-EXISTS', data=json.dumps(user),
                                          headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_auth_user(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail']
        }
        self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        response = self.test_client.post('/users/auth', data=json.dumps(user),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['token'])
        self.assertIsNotNone(json.loads(response.get_data())['expireAt'])

    def test_auth_user_invalid_credentials(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail']
        }
        self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        user = {
            "username": user['username'],
            "password": self.faker.password(length=12)
        }
        response = self.test_client.post('/users/auth', data=json.dumps(user),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_auth_user_not_exists(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12)
        }
        response = self.test_client.post('/users/auth', data=json.dumps(user),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)

    def test_auth_user_without_mandatory_fields(self):
        user = {}
        response = self.test_client.post('/users/auth', data=json.dumps(user),
                                         headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_get_user_by_token(self):
        user = {
            "username": self.faker.profile()['username'],
            "password": self.faker.password(length=12),
            "email": self.faker.profile()['mail'],
            "dni": self.faker.passport_number(),
            "fullName": self.faker.profile()['name'],
            "phoneNumber": self.faker.phone_number()
        }
        self.test_client.post('/users', data=json.dumps(user), headers={'Content-Type': 'application/json'})
        response = self.test_client.post('/users/auth', data=json.dumps(user),
                                         headers={'Content-Type': 'application/json'})
        response = self.test_client.get('/users/me', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer ' +
                                                                               json.loads(response.get_data())[
                                                                                   'token']})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.get_data())['username'])
        self.assertIsNotNone(json.loads(response.get_data())['email'])

    def test_get_user_by_token_without_token(self):
        response = self.test_client.get('/users/me', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 403)

    def test_get_user_by_token_invalid_token(self):
        response = self.test_client.get('/users/me', headers={'Content-Type': 'application/json',
                                                              'Authorization': 'Bearer INVALID'})
        self.assertEqual(response.status_code, 401)

    def test_ping(self):
        response = self.test_client.get('/users/ping', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_reset(self):
        response = self.test_client.post('/users/reset', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

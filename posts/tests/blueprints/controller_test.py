import json
from unittest import TestCase
from unittest.mock import patch, Mock

from faker import Faker

from src.main import app


class ControllerTest(TestCase):
    
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create_post(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
    
    def test_create_post_without_token(self):
        error_response = Mock()
        error_response.status_code = 403
        with patch('requests.get', return_value=error_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 403)
    
    def test_create_post_with_invalid_token(self):
        error_response = Mock()
        error_response.status_code = 401
        with patch('requests.get', return_value=error_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 401)

    def test_create_post_without_mandatory_fields(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            post = {

            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 400)

    def test_create_post_with_expire_at_past(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2020-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 412)
    
    def test_create_post_with_expire_at_invalid_iso(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '12-FEB-2100'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 412)

    def test_search_post_without_filter(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response = self.test_client.get('/posts', headers={'Content-Type': 'application/json',
                                                               'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 200)

    def test_search_post_not_expired(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response = self.test_client.get('/posts?expire=false', headers={'Content-Type': 'application/json',
                                                                            'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 200)

    def test_search_post_invalid_expired(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response = self.test_client.get('/posts?expire=invalid', headers={'Content-Type': 'application/json',
                                                                              'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 400)

    def test_search_post_with_route(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        route = self.faker.uuid4()
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": route,
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response = self.test_client.get('/posts?route=' + route, headers={'Content-Type': 'application/json',
                                                                              'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 200)

    def test_search_post_with_me(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response = self.test_client.get('/posts?owner=me', headers={'Content-Type': 'application/json',
                                                                        'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 200)

    def test_search_post_with_other_owner(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": self.faker.uuid4(),
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        success_response_other = Mock()
        success_response_other.status_code = 200
        success_response_other.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a5"})
        with patch('requests.get', return_value=success_response_other):
            response = self.test_client.get('/posts?owner=caf8959a-fd13-4c0f-916d-4dab479384a4',
                                            headers={'Content-Type': 'application/json',
                                                     'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 200)

    def test_search_post_without_token(self):
        success_response_other = Mock()
        success_response_other.status_code = 403
        with patch('requests.get', return_value=success_response_other):
            response = self.test_client.get('/posts?owner=me', headers={'Content-Type': 'application/json',
                                                                        'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 403)

    def test_search_post_with_invalid_token(self):
        success_response_other = Mock()
        success_response_other.status_code = 401
        with patch('requests.get', return_value=success_response_other):
            response = self.test_client.get('/posts?owner=me', headers={'Content-Type': 'application/json',
                                                                        'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 401)

    def test_ping(self):
        response = self.test_client.get('/posts/ping', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_reset(self):
        response = self.test_client.post('/posts/reset', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_get_post_by_id(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        route = self.faker.uuid4()
        response = None
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": route,
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response_get = self.test_client.get('/posts/' + json.loads(response.get_data())['id'],
                                                headers={'Content-Type': 'application/json',
                                                         'Authorization': 'Bearer token'})
            self.assertEqual(response_get.status_code, 200)

    def test_get_post_by_id_non_uuid(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            response_get = self.test_client.get('/posts/1',
                                                headers={'Content-Type': 'application/json',
                                                         'Authorization': 'Bearer token'})
            self.assertEqual(response_get.status_code, 400)

    def test_get_post_by_id_not_found(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            response_get = self.test_client.get('/posts/' + self.faker.uuid4(),
                                                headers={'Content-Type': 'application/json',
                                                         'Authorization': 'Bearer token'})
            self.assertEqual(response_get.status_code, 404)

    def test_delete_post_non_uuid(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            response_get = self.test_client.delete('/posts/1',
                                                   headers={'Content-Type': 'application/json',
                                                            'Authorization': 'Bearer token'})
            self.assertEqual(response_get.status_code, 400)

    def test_delete_post(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        route = self.faker.uuid4()
        response = None
        with patch('src.commands.token.Token.verify_token', return_value=success_response):
            post = {
                "routeId": route,
                "expireAt": '2025-02-10T00:10:55.222Z'
            }
            response = self.test_client.post('/posts', data=json.dumps(post),
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Bearer token'})
            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(json.loads(response.get_data())['id'])
            self.assertIsNotNone(json.loads(response.get_data())['userId'])
            self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
        with patch('requests.get', return_value=success_response):
            response_delete = self.test_client.delete('/posts/' + json.loads(response.get_data())['id'],
                                                      headers={'Content-Type': 'application/json',
                                                               'Authorization': 'Bearer token'})
            self.assertEqual(response_delete.status_code, 200)

    def test_delete_post_not_found(self):
        success_response = Mock()
        success_response.status_code = 200
        success_response.text = json.dumps({'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"})
        with patch('requests.get', return_value=success_response):
            response_get = self.test_client.delete('/posts/' + self.faker.uuid4(),
                                                   headers={'Content-Type': 'application/json',
                                                            'Authorization': 'Bearer token'})
            self.assertEqual(response_get.status_code, 404)


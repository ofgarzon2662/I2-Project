import json
from unittest import TestCase
from unittest.mock import patch
from faker import Faker
import uuid
from src.main import app
from datetime import datetime, timedelta


class Routes_Test(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    @patch('src.commons.validation_util.requests.get')
    def test_create(self, mocked_get):
        mocked_get.return_value.status_code = 200
        route = {
            'flightId': str(uuid.uuid4()),
            'sourceAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'sourceCountry': self.faker.country(),
            'destinyAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'destinyCountry': self.faker.country(),
            'bagCost': self.faker.random_int(min=1, max=999),
            'plannedStartDate': datetime.now().isoformat(),
            'plannedEndDate': (datetime.now() + timedelta(days=self.faker.random_int(min=1, max=180))).isoformat()
        }
        response = self.test_client.post('/routes', data=json.dumps(route),
                                         headers={'Content-Type': 'application/json',
                                                  "Authorization": 'Valid Token'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['createdAt'])

    @patch('src.commons.validation_util.requests.get')
    def test_delte(self, mocked_get):
        mocked_get.return_value.status_code = 200
        route = {
            'flightId': str(uuid.uuid4()),
            'sourceAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'sourceCountry': self.faker.country(),
            'destinyAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'destinyCountry': self.faker.country(),
            'bagCost': self.faker.random_int(min=1, max=999),
            'plannedStartDate': datetime.now().isoformat(),
            'plannedEndDate': (datetime.now() + timedelta(days=self.faker.random_int(min=1, max=180))).isoformat()
        }
        responseCreate = self.test_client.post('/routes', data=json.dumps(route),
                                               headers={'Content-Type': 'application/json',
                                                        "Authorization": 'Valid Token'})
        self.assertEqual(responseCreate.status_code, 201)
        self.assertIsNotNone(json.loads(responseCreate.get_data())['id'])
        self.assertIsNotNone(json.loads(
            responseCreate.get_data())['createdAt'])

        responseDelete = self.test_client.delete('/routes/' + json.loads(responseCreate.get_data())['id'],
                                                 headers={'Content-Type': 'application/json',
                                                          "Authorization": 'Valid Token'})
        self.assertEqual(responseDelete.status_code, 200)
        self.assertEqual(json.loads(responseDelete.get_data())['msg'], "el trayecto fue eliminado")

    @patch('src.commons.validation_util.requests.get')
    def test_detail(self, mocked_get):
        mocked_get.return_value.status_code = 200
        route = {
            'flightId': str(uuid.uuid4()),
            'sourceAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'sourceCountry': self.faker.country(),
            'destinyAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'destinyCountry': self.faker.country(),
            'bagCost': self.faker.random_int(min=1, max=999),
            'plannedStartDate': datetime.now().isoformat(),
            'plannedEndDate': (datetime.now() + timedelta(days=self.faker.random_int(min=1, max=180))).isoformat()
        }
        responseCreate = self.test_client.post('/routes', data=json.dumps(route),
                                               headers={'Content-Type': 'application/json',
                                                        "Authorization": 'Valid Token'})
        self.assertEqual(responseCreate.status_code, 201)
        self.assertIsNotNone(json.loads(responseCreate.get_data())['id'])
        self.assertIsNotNone(json.loads(
            responseCreate.get_data())['createdAt'])

        responseDetail = self.test_client.get('/routes/' + json.loads(responseCreate.get_data())['id'],
                                                 headers={'Content-Type': 'application/json',
                                                          "Authorization": 'Valid Token'})
        self.assertEqual(json.loads(responseDetail.get_data())['id'], json.loads(responseCreate.get_data())['id'])
        self.assertEqual(json.loads(responseDetail.get_data())['flightId'], route['flightId'])   
        self.assertEqual(json.loads(responseDetail.get_data())['sourceAirportCode'], route['sourceAirportCode'])   
        self.assertEqual(json.loads(responseDetail.get_data())['sourceCountry'], route['sourceCountry'])   
        self.assertEqual(json.loads(responseDetail.get_data())['destinyAirportCode'], route['destinyAirportCode'])   
        self.assertEqual(json.loads(responseDetail.get_data())['destinyCountry'], route['destinyCountry'])   
        self.assertEqual(json.loads(responseDetail.get_data())['bagCost'], route['bagCost'])   
        self.assertEqual(json.loads(responseDetail.get_data())['plannedStartDate'], route['plannedStartDate'])   
        self.assertEqual(json.loads(responseDetail.get_data())['plannedEndDate'], route['plannedEndDate'])  

    @patch('src.commons.validation_util.requests.get')
    def test_list(self, mocked_get):
        mocked_get.return_value.status_code = 200
        route = {
            'flightId': str(uuid.uuid4()),
            'sourceAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'sourceCountry': self.faker.country(),
            'destinyAirportCode': self.faker.pystr(min_chars=3, max_chars=3),
            'destinyCountry': self.faker.country(),
            'bagCost': self.faker.random_int(min=1, max=999),
            'plannedStartDate': datetime.now().isoformat(),
            'plannedEndDate': (datetime.now() + timedelta(days=self.faker.random_int(min=1, max=180))).isoformat()
        }
        responseCreate = self.test_client.post('/routes', data=json.dumps(route),
                                               headers={'Content-Type': 'application/json',
                                                        "Authorization": 'Valid Token'})
        self.assertEqual(responseCreate.status_code, 201)
        self.assertIsNotNone(json.loads(responseCreate.get_data())['id'])
        self.assertIsNotNone(json.loads(
            responseCreate.get_data())['createdAt'])

        responseDetail = self.test_client.get('/routes',
                                                 headers={'Content-Type': 'application/json',
                                                          "Authorization": 'Valid Token'})
             
        exist = False

        for item in json.loads(responseDetail.get_data()):
            if(item['id'] == json.loads(responseCreate.get_data())['id']):
                self.assertEqual(item['id'], json.loads(responseCreate.get_data())['id'])
                self.assertEqual(item['flightId'], route['flightId'])   
                self.assertEqual(item['sourceAirportCode'], route['sourceAirportCode'])   
                self.assertEqual(item['sourceCountry'], route['sourceCountry'])   
                self.assertEqual(item['destinyAirportCode'], route['destinyAirportCode'])   
                self.assertEqual(item['destinyCountry'], route['destinyCountry'])   
                self.assertEqual(item['bagCost'], route['bagCost'])   
                self.assertEqual(item['plannedStartDate'], route['plannedStartDate'])   
                self.assertEqual(item['plannedEndDate'], route['plannedEndDate'])
                exist = True
                break

        self.assertEqual(exist, True)
        
                

    def test_ping(self):
        response = self.test_client.get('/routes/ping', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_reset(self):
        response = self.test_client.post('/routes/reset', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)    

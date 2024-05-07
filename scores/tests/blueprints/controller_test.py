import json
from unittest import TestCase

from faker import Faker

from src.main import app


class ControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create_score(self):
        bagCost = self.faker.random_number()
        offer = bagCost + 1
        score = {
            "idOffer": self.faker.uuid4(),
            "idPost": self.faker.uuid4(),
            "idUserPosting": self.faker.uuid4(),
            "idUserOffering": self.faker.uuid4(),
            "ocupancy": self.faker.random_element(elements=("LARGE", "MEDIUM", "SMALL")),
            "bagCost": bagCost,
            "offer": offer
        }
        response = self.test_client.post('/scores', data=json.dumps(score), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['score'])

    def test_get_scores_by_offer_id(self):
        # Creamos un Score en la db
        bagCost = self.faker.random_number()
        offer = bagCost + 1
        idOffer = self.faker.uuid4()
        score = {
            "idOffer": idOffer,
            "idPost": self.faker.uuid4(),
            "idUserPosting": self.faker.uuid4(),
            "idUserOffering": self.faker.uuid4(),
            "ocupancy": self.faker.random_element(elements=("LARGE", "MEDIUM", "SMALL")),
            "bagCost": bagCost,
            "offer": offer,
            "score": 1
        }


        self.test_client.post('/scores', data=json.dumps(score), headers={'Content-Type': 'application/json'})
        # Obtenemos el Score por el idOffer
        score_offer = self.test_client.get('/scores/offers/' + idOffer, headers={'Content-Type': 'application/json'})
        self.assertEqual(score_offer.status_code, 200)
        self.assertIsNotNone(json.loads(score_offer.get_data()))
       
        # Assert the OfferID is the same as the one we created
        self.assertEqual(json.loads(score_offer.get_data())['idOffer'], idOffer)

    def test_delete_score(self):
        # Creamos un Score en la db
        bagCost = self.faker.random_number()
        offer = bagCost + 1
        score = {
            "idOffer": self.faker.uuid4(),
            "idPost": self.faker.uuid4(),
            "idUserPosting": self.faker.uuid4(),
            "idUserOffering": self.faker.uuid4(),
            "ocupancy": self.faker.random_element(elements=("LARGE", "MEDIUM", "SMALL")),
            "bagCost": bagCost,
            "offer": offer,
            "score": 1
        }
        response = self.test_client.post('/scores', data=json.dumps(score), headers={'Content-Type': 'application/json'})
        # Eliminamos el Score
        response = self.test_client.delete('/scores/' + json.loads(response.get_data())['id'], headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data())['msg'], 'Score eliminado')

    def test_ping(self):
        response = self.test_client.get('/scores/ping', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), 'pong')

    def test_reset(self):
        #Creamos varios scores aleatorios
        for i in range(10):
            bagCost = self.faker.random_number()
            offer = bagCost + 1
            score = {
                "idOffer": self.faker.uuid4(),
                "idPost": self.faker.uuid4(),
                "idUserPosting": self.faker.uuid4(),
                "idUserOffering": self.faker.uuid4(),
                "ocupancy": self.faker.random_element(elements=("LARGE", "MEDIUM", "SMALL")),
                "bagCost": bagCost,
                "offer": offer,
                "score": self.faker.random_number()
            }
            self.test_client.post('/scores', data=json.dumps(score), headers={'Content-Type': 'application/json'})
        response = self.test_client.post('/scores/reset', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data())['msg'], 'Todos los datos fueron eliminados')

    def tearDown(self):
        pass
    
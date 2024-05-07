from unittest import TestCase
from unittest.mock import Mock, patch

import pytest

from src.errors.api_exception import ApiException
from src.services.route_service import get_route_by_flight_id, create_route, delete_route


class RouteServiceTest(TestCase):
    def test__get_route_by_flight_id__success(self):
        response_body = {'id': "caf8959a-fd13-4c4f-916d-4dab479384a4"}
        response = Mock()
        response.status_code = 200
        response.json.return_value = response_body
        with patch('requests.get', return_value=response):
            result = get_route_by_flight_id('token', 'flightId')
            self.assertEqual(response_body.get('id'), result.get('id'))

    def test__get_post_by_route_id__error(self):
        response = Mock()
        response.status_code = 404
        with patch('requests.get', return_value=response):
            with pytest.raises(ApiException) as exception:
                get_route_by_flight_id('token', 'flightId')
            self.assertEqual(exception.value.code, 404)

    def test__create_route__success(self):
        response_body = {'id': "caf8949a-fd13-4c0f-916d-4dab479384a4"}
        response = Mock()
        response.status_code = 201
        response.json.return_value = response_body
        with patch('requests.post', return_value=response):
            result = create_route('token', 'flightId', 'plannedStartDate', 'plannedEndDate', 'sourceAirportCode',
                                  'sourceCountry', 'destinyAirportCode', 'destinyCountry', 'bagCost')
            self.assertEqual(response_body.get('id'), result.get('id'))

    def test__create_route__error(self):
        response = Mock()
        response.status_code = 400
        with patch('requests.post', return_value=response):
            with pytest.raises(ApiException) as exception:
                create_route('token', 'flightId', 'plannedStartDate', 'plannedEndDate', 'sourceAirportCode',
                             'sourceCountry', 'destinyAirportCode', 'destinyCountry', 'bagCost')
            self.assertEqual(exception.value.code, 400)

    def test__delete_route__error(self):
        response = Mock()
        response.status_code = 404
        with patch('requests.delete', return_value=response):
            with pytest.raises(ApiException) as exception:
                delete_route('token', 'routeId')
            self.assertEqual(exception.value.code, 404)

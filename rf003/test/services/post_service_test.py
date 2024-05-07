from unittest import TestCase
from unittest.mock import patch, Mock

import pytest

from src.errors.api_exception import ApiException
from src.services.post_service import get_post_by_route_id, create_post


class PostServiceTest(TestCase):
    def test__get_post_by_route_id__success(self):
        response_body = {'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"}
        response = Mock()
        response.status_code = 200
        response.json.return_value = response_body
        with patch('requests.get', return_value=response):
            result = get_post_by_route_id('token', 'routeId')
            self.assertEqual(response_body.get('id'), result.get('id'))

    def test__get_post_by_route_id__error(self):
        response = Mock()
        response.status_code = 404
        with patch('requests.get', return_value=response):
            with pytest.raises(ApiException) as exception:
                get_post_by_route_id('token', 'routeId')
            self.assertEqual(exception.value.code, 404)

    def test__create_post__success(self):
        response_body = {'id': "caf8959a-fd13-4c0f-916d-4dab479384a4"}
        response = Mock()
        response.status_code = 201
        response.json.return_value = response_body
        with patch('requests.post', return_value=response):
            result = create_post('token', 'routeId', 'expireAt')
            self.assertEqual(response_body.get('id'), result.get('id'))

    def test__create_post__error(self):
        response = Mock()
        response.status_code = 400
        with patch('requests.post', return_value=response):
            with pytest.raises(ApiException) as exception:
                create_post('token', 'routeId', 'expireAt')
            self.assertEqual(exception.value.code, 400)

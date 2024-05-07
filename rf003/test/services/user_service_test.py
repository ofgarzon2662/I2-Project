from unittest import TestCase
from unittest.mock import Mock, patch

import pytest

from src.errors.api_exception import ApiException
from src.services.user_service import get_user


class UserServiceTest(TestCase):

    def test__get_user__error(self):
        response = Mock()
        response.status_code = 401
        with patch('requests.get', return_value=response):
            with pytest.raises(ApiException) as exception:
                get_user('token')
            self.assertEqual(exception.value.code, 401)

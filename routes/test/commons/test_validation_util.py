from unittest import TestCase
from unittest.mock import patch
import src.commons.validation_util as validation_util
from src.errors.errors import BadRequestException, TokenInvalid, NotToken

class Validation_Util_Test(TestCase):

    @patch('src.commons.validation_util.requests.get')
    def test_validate_user_identity_ok(self, mocked_get):
        mocked_get.return_value.status_code = 200
        response = validation_util.validate_user_identity('test')
        self.assertIsNone(response)

    @patch('src.commons.validation_util.requests.get')
    def test_validate_user_identity_token_invalid(self, mocked_get):
        mocked_get.return_value.status_code = 401
        with self.assertRaises(TokenInvalid):
            validation_util.validate_user_identity('test')

    @patch('src.commons.validation_util.requests.get')
    def test_validate_user_identity_no_token(self, mocked_get):
        mocked_get.return_value.status_code = 403
        with self.assertRaises(NotToken):
            validation_util.validate_user_identity('test')

    def test_validate_not_blank_ok(self):
        response = validation_util.validate_not_blank(['test','demo'])
        self.assertIsNone(response)

    def test_validate_not_blank_fail(self):
        with self.assertRaises(BadRequestException):
            validation_util.validate_not_blank(None)
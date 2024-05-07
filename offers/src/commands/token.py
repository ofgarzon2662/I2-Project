import requests, os
from ..errors.errors import TokenInvalid
from ..errors.errors import NotToken


class Token:

    def verify_token(self, token):
        response = requests.get(os.environ.get('USERS_PATH', "http://localhost:3000") + "/users/me",
                                headers={"Authorization": token})
        if response.status_code == 401:
            raise TokenInvalid
        if response.status_code == 403:
            raise NotToken
        return response
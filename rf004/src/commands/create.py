from datetime import datetime
from abc import ABC

from ..commands.base_command import BaseCommand
from ..errors.api_exception import ApiException
from ..service.offer_service import create_offer, delete_offer
from ..service.post_service import get_post_by_id
from ..service.score_service import create_score
from ..service.user_service import get_user
from ..service.route_service import get_route_by_id


class Create(BaseCommand, ABC):
    def __init__(self,
                 token,
                 postId,
                 description,
                 size,
                 fragile,
                 offer):
        self.token = token
        self.postId = postId
        self.description = description
        self.size = size
        self.fragile = fragile
        self.offer = offer

    def execute(self):
        user = get_user(self.token)
        post = get_post_by_id(
            self.token,
            self.postId)
        route = get_route_by_id(self.token, post.get('routeId'))
        expireAt = datetime.strptime(post.get('expireAt'), "%Y-%m-%dT%H:%M:%S.%f")
        if expireAt < datetime.now():
            raise ApiException(
                412,
                'Publicación expirada'
            )
        if user.get('id') == post.get('userId'):
            raise ApiException(
                412,
                'No puede ofertar sobre sus propias publicaciones')

        
        offer = create_offer(
            self.token,
            self.postId,
            self.description,
            self.size,
            self.fragile,
            self.offer)
        try:
            score = create_score(offer.get('id'), self.postId, post.get('userId'), user.get('id'), self.size, route.get('bagCost'), self.offer)
        except ApiException as exception:
                delete_offer(self.token, offer.get('id'))
                raise ApiException(
                    exception.code,
                    exception.message)
        return {
            'msg': '',
            'data': {
                'id': offer.get('id'),
                'userId': offer.get('userId'),
                'createdAt': offer.get('createdAt'),
                'postId': self.postId,
                'scoreId': score.get('id'),
                'score': score.get('score')}}
from abc import ABC

from ..commands.base_command import BaseCommand
from ..errors.api_exception import ApiException
from ..service.offer_service import get_offer_by_post_id
from ..service.post_service import get_post_by_id
from ..service.route_service import get_route_by_id
from ..service.user_service import get_user
from ..service.score_service import calculate_score


def calculate_score_test(offer):
    percentage = 1
    if offer.get('size') == 'SMALL':
        percentage = 0.25
    if offer.get('size') == 'MEDIUM':
        percentage = 0.50
    return float(offer.get('offer')) - (percentage * float(offer.get('offer')))


class Get(BaseCommand, ABC):
    def __init__(self,
                 token,
                 postId):
        self.token = token
        self.postId = postId

    def execute(self):
        print('Si +++++++++++++++++++++++++++++------------------- 0')
        user = get_user(self.token)
        print('Si +++++++++++++++++++++++++++++------------------- 1')
        post = get_post_by_id(
            self.token,
            self.postId)
        print('Si +++++++++++++++++++++++++++++------------------- 2')
        print(post)
        if user.get('id') != post.get('userId'):
            print('Si +++++++++++++++++++++++++++++------------------- 2.1')
            raise ApiException(
                403,
                'La publicación no le pertenece')
        print('Si +++++++++++++++++++++++++++++------------------- 3')
        route = get_route_by_id(self.token, post.get('routeId'))
        print('Si +++++++++++++++++++++++++++++------------------- 4')
        offers = get_offer_by_post_id(self.token, post.get('id'))
        print('Si +++++++++++++++++++++++++++++------------------- 5')
        print(offers)
        print('Si +++++++++++++++++++++++++++++------------------- 6')
        calculated_offers = []
        for offer in offers:
            score = calculate_score(offer.get('id'))
            offer['score'] = score.get('score')
            calculated_offers.append(offer)
        sorted_offers = sorted(calculated_offers, key=lambda x: x['score'], reverse=True)
        return {
            'msg': '',
            'data': {
                'id': post.get('id'),
                'route': {
                    'id': route.get('id'),
                    'flightId': route.get('flightId'),
                    'origin': {
                        'airportCode': route.get('sourceAirportCode'),
                        'country': route.get('sourceCountry')},
                    'destiny': {
                        'airportCode': route.get('destinyAirportCode'),
                        'country': route.get('destinyCountry')},
                    'bagCost': route.get('bagCost')},
                'expireAt': post.get('expireAt'),
                'plannedStartDate': route.get('plannedStartDate'),
                'plannedEndDate': route.get('plannedEndDate'),
                'createdAt': post.get('createdAt'),
                'offers': sorted_offers}}

from abc import ABC

from ..commands.base_command import BaseCommand
from ..errors.api_exception import ApiException
from ..services.post_service import get_post_by_route_id, create_post
from ..services.route_service import get_route_by_flight_id, create_route, delete_route
from ..services.user_service import get_user


class Create(BaseCommand, ABC):
    def __init__(self,
                 token,
                 flightId,
                 plannedStartDate,
                 plannedEndDate,
                 sourceAirportCode,
                 sourceCountry,
                 destinyAirportCode,
                 destinyCountry,
                 bagCost,
                 expireAt):
        self.token = token
        self.flightId = flightId
        self.expireAt = expireAt
        self.plannedStartDate = plannedStartDate
        self.plannedEndDate = plannedEndDate
        self.sourceAirportCode = sourceAirportCode
        self.sourceCountry = sourceCountry
        self.destinyAirportCode = destinyAirportCode
        self.destinyCountry = destinyCountry
        self.bagCost = bagCost

    def execute(self):
        get_user(self.token)
        route = get_route_by_flight_id(
            self.token,
            self.flightId)
        if len(route) == 0:
            execute_rollback_on_error = True
            route = create_route(
                self.token,
                self.flightId,
                self.plannedStartDate,
                self.plannedEndDate,
                self.sourceAirportCode,
                self.sourceCountry,
                self.destinyAirportCode,
                self.destinyCountry,
                self.bagCost)
        else:
            execute_rollback_on_error = False
            route = route[0]
        post = get_post_by_route_id(
            self.token,
            route.get('id'))
        if len(post) > 0:
            if execute_rollback_on_error is True:
                delete_route(self.token, route.get('id'))
            raise ApiException(
                412,
                'El usuario ya tiene una publicación para la misma fecha')
        else:
            try:
                post = create_post(
                    self.token,
                    route.get('id'),
                    self.expireAt)
            except ApiException as exception:
                if execute_rollback_on_error is True:
                    delete_route(self.token, route.get('id'))
                raise ApiException(
                    exception.code,
                    exception.message)
        return {
            'msg': '',
            'data': {
                'id': post.get('id'),
                'userId': post.get('userId'),
                'createdAt': post.get('createdAt'),
                'route': {
                    'id': route.get('id'),
                    'createdAt': route.get('createdAt')}}}

from .base_command  import  BaseCommand
from ..models.model import db
from ..models.route import Route, ModelSchema
from ..commons.validation_util import validate_not_blank, validate_flightId_not_exits, validate_iso8601_datetime_not_past, validate_date_range, validate_user_identity
from datetime import datetime

class  Create(BaseCommand):
	def  __init__(self, flightId, sourceAirportCode, sourceCountry, destinyAirportCode, destinyCountry, bagCost, plannedStartDate, plannedEndDate, token):
		self.flightId  =  flightId
		self.sourceAirportCode  =  sourceAirportCode
		self.sourceCountry = sourceCountry
		self.destinyAirportCode = destinyAirportCode
		self.destinyCountry = destinyCountry
		self.bagCost = bagCost
		self.plannedStartDate = plannedStartDate
		self.plannedEndDate = plannedEndDate
		self.token = token

	def  execute(self):
		print(self.plannedStartDate)
		print(self.plannedEndDate)
		validate_user_identity(self.token)
		validate_not_blank(self.flightId, self.sourceAirportCode, self.sourceCountry, self.destinyAirportCode, 
				self.destinyCountry, self.bagCost, self.plannedStartDate, self.plannedEndDate)		
		validate_flightId_not_exits(self.flightId)
		validate_iso8601_datetime_not_past(self.plannedStartDate, self.plannedEndDate)
		validate_date_range(self.plannedStartDate, self.plannedEndDate)
		route = Route(flightId=self.flightId, sourceAirportCode=self.sourceAirportCode, sourceCountry=self.sourceCountry, destinyAirportCode=self.destinyAirportCode, 
				destinyCountry=self.destinyCountry, bagCost=self.bagCost, plannedStartDate=datetime.fromisoformat(self.plannedStartDate.replace('Z', '+00:00')) , plannedEndDate=datetime.fromisoformat(self.plannedEndDate.replace('Z', '+00:00')))
		db.session.add(route)
		db.session.commit()
		return ModelSchema().dump(route)
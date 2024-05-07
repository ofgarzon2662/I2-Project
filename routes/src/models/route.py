from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Integer, String, DateTime

from ..models.model import Model, db

# Extender la clase Model proporcionada
class Route(db.Model, Model):
	__tablename__  =  'routes'
	flightId  =  db.Column(String)
	sourceAirportCode  =  db.Column(String)
	sourceCountry  =  db.Column(String)
	destinyAirportCode  =  db.Column(String)
	destinyCountry  =  db.Column(String)
	bagCost  =  db.Column(Integer)
	plannedStartDate  =  db.Column(DateTime)
	plannedEndDate  =  db.Column(DateTime)

# Constructor
def  __init__(self, flightId=None, sourceAirportCode=None, sourceCountry=None, destinyAirportCode=None, destinyCountry=None, bagCost=None, plannedStartDate=None, plannedEndDate=None):
	Model.__init__(self)
	self.flightId  =  flightId
	self.sourceAirportCode  =  sourceAirportCode
	self.sourceCountry = sourceCountry
	self.destinyAirportCode = destinyAirportCode
	self.destinyCountry = destinyCountry
	self.bagCost = bagCost
	self.plannedStartDate = plannedStartDate
	self.plannedEndDate = plannedEndDate

# Especificar los campos que estarán presentes al serializar el objeto como JSON.
class ModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Route
        load_instance = True
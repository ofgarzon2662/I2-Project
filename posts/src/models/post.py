# models/post.py
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from  sqlalchemy  import  Column, String, Integer
from .model  import  Model, Base, db

# Extender la clase Model proporcionada
class Post(db.Model, Model):
	__tablename__  =  'posts'
	routeId  =  db.Column(String) # identificador del trayecto
	userId =  db.Column(String) # identificador del usuario dueño de la publicación

# Constructor
def  __init__(self, routeId = None, userId = None):
	Model.__init__(self)
	self.routeId  =  routeId
	self.userId  =  userId

# Especificar los campos que estarán presentes al serializar el objeto como JSON.
class  PostSchema(SQLAlchemyAutoSchema):
	class Meta:
		model  =  Post
		load_instance  =  True
		include_relationships  =  True
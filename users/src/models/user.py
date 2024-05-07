from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import String, DateTime

from ..models.model import Model, db


class User(db.Model, Model):
    __tablename__ = 'users'
    username = db.Column(String(50))
    email = db.Column(String(100))
    phoneNumber = db.Column(String(15))
    dni = db.Column(String(15))
    fullName = db.Column(String(200))
    password = db.Column(String(2000))
    salt = db.Column(String(36))
    token = db.Column(String(36))
    status = db.Column(String(15))
    expireAt = db.Column(DateTime)

    def __init__(self, username=None, email=None, phoneNumber=None, dni=None, fullName=None, password=None, salt=None,
                 token=None, status=None, expireAt=None):
        super().__init__()
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.dni = dni
        self.fullName = fullName
        self.password = password
        self.salt = salt
        self.token = token
        self.status = status
        self.expireAt = expireAt


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

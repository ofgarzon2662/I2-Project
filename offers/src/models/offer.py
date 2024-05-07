from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.model import Model, db

class Offer(db.Model, Model):
    __tablename__ = 'offers'
    postId = db.Column(db.String(1000))
    userId = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    size = db.Column(db.String(200))
    fragile = db.Column(db.Boolean)
    offer = db.Column(db.Numeric(10,2))

    def __init__(self, postId=None, userId=None, description=None, size=None, fragile=None, offer=None):
        super().__init__()
        self.postId = postId
        self.userId = userId
        self.description = description
        self.size = size
        self.fragile = fragile
        self.offer = offer


class OfferSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Offer
        load_instance = True
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import String 

from .model import Model, db


class Score(db.Model, Model):
    __tablename__ = 'scores'
    idOffer = db.Column(String)
    idPost = db.Column(String)
    idUserOffering = db.Column(String)
    idUserPosting = db.Column(String)
    # Add ocupancy attribute that is a enum of 3 values: "LARGE", "MEDIUM", "SMALL"
    ocupancy = db.Column(String)
    bagCost = db.Column(db.Float)
    offer = db.Column(db.Float)
    #Add score, which is a non integer number
    score = db.Column(db.Float)
    

    def __init__(self, idOffer = None, idPost = None, idUserOffering = None, idUserPosting = None, ocupancy = None, bagCost = None, offer = None, score = None):
        self.idOffer = idOffer
        self.idPost = idPost
        self.idUserOffering = idUserOffering
        self.idUserPosting = idUserPosting
        self.ocupancy = ocupancy
        self.bagCost = bagCost
        self.offer = offer
        self.score = score


class ScoreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Score
        load_instance = True

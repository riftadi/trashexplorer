from run import db
from models.basedb import BaseDBClass

class TrashbinModel(db.Model, BaseDBClass):
    __tablename__ = "trashbins"
    id = db.Column(db.Integer, primary_key = True)
    isVerified = db.Column(db.Boolean)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

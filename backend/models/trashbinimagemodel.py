from run import db
from models.basedb import BaseDBClass

class TrashbinImageModel(db.Model, BaseDBClass):
    __tablename__ = "trashbin_images"
    id = db.Column(db.Integer, primary_key = True)
    trashbinId = db.Column(db.Integer, db.ForeignKey("trashbins.id"))
    userId = db.Column(db.Integer, db.ForeignKey("users.id"),
        nullable=False)
    isVerified = db.Column(db.Boolean)
    pano = db.Column(db.String(32))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    fov = db.Column(db.Integer)
    heading = db.Column(db.Integer)
    pitch = db.Column(db.Integer)
    isAnnotated = db.Column(db.Boolean)
    topLeftPixel = db.Column(db.Integer)
    bottomRightPixel = db.Column(db.Integer)
    createdOn = db.Column(db.DateTime, server_default=db.func.now())
    updatedOn = db.Column(db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())

    def to_json(x):
        return {
            "id" : x.id,
            "trashbinId": x.trashbinId,
            "userId": x.userId,
            "pano": x.pano,
            "longitude": x.longitude,
            "latitude": x.latitude,
            "fov": x.fov,
            "heading": x.heading,
            "pitch": x.pitch,
            "isAnnotated": x.isAnnotated,
            "topLeftPixel": x.topLeftPixel,
            "bottomRightPixel": x.bottomRightPixel,
            "createdOn" : str(x.createdOn),
            "updatedOn" : str(x.updatedOn)
        }

    @classmethod
    def return_all(cls):
        return {"Trophies": list(map(lambda x: self.to_json(x), TrashbinImageModel.query.all()))}

    @classmethod
    def return_all_from_userid(cls, userid):
        return {"Trophies": list(map(lambda x: self.to_json(x), TrashbinImageModel.query.filter_by(userId=userid)))}


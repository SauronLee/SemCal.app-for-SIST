from App.ext import db
from App.models import BaseModel


class SemCal(BaseModel):
    __tablename__ = 'SemCals'
    showname_model_str = db.Column(db.String(64))
    showname_model_en = db.Column(db.String(128))
    autor = db.Column(db.String(64))
    references = db.Column(db.String(256))
    type = db.Column(db.String(64))
    ist = db.Column(db.String(64))
    language = db.Column(db.String(64))
    accuracy_rate = db.Column(db.Integer, default=0)
    country = db.Column(db.String(64))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(256))
    flag = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)
import datetime
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship
from bitching import (
    db
)

from bitching.mod_account.models import(
    User
)

class Bitch(db.Model):
    __tablename__ = 'bitch'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    message = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    user = relationship("User", backref="Bitch")

    def __init__(self,userId, message):
        self.userId = userId
        self.message = message

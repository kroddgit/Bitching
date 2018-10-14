from bitching import (
    db,
    login_manager
)
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    _is_active = db.Column(db.Boolean)
    _is_authenticated = db.Column(db.Boolean, default=False)
    profilepicUrl = db.Column(db.String(32), index=True, unique=True)

    def __init__(self,username,email,password, is_active):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active

    @property
    def is_authenticated(self):
        return self._is_authenticated

    def is_authenticated(self, value):
        self._is_authenticated = value;

    @property
    def is_active(self):
        return True

    @is_active.setter
    def is_active(self, value):
        self._is_active = value

    @property
    def is_anonymous(self):
        return not self.is_authenticated

    def get_id(self):
        return self.id

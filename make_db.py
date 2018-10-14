import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from bitching.mod_account.models import(
    User
)
from bitching.mod_bitch.models import(
    Bitch
)
from werkzeug.security import (
    generate_password_hash
)
from bitching import db

engine = create_engine('sqlite:///bitching.db')
Base = declarative_base()
Base.metadata.reflect(bind=engine)
db.create_all()

hash = generate_password_hash("password")
newUser = User("krodd", "krodd@tcservices.biz", hash, True)
newUser.is_authenticated(True)
db.session.add(newUser)
db.session.commit()

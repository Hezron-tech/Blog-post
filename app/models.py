
from .import db

class User(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    quotes = db.relationship("Quote", backref="user", lazy="dynamic")
    comment = db.relationship("Comments", backref="user", lazy="dynamic")
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))









    

    
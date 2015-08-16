from app import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email    = db.Column(db.String(120))
    password = db.Column(db.String(50))
    about    = db.Column(db.String(120))
    backgroundImage = db.Column(db.Integer)
    apartment       = db.Column(db.Integer)
    inbox           = db.relationship('Message', backref='user', lazy="dynamic")
    def __init__(self, username, email, password, about=None, backgroundImage=None, apartment=None):
        self.username = username 
        self.email    = email
        self.password = password
        self.about    = about
        self.backgroundImage = backgroundImage
        self.apartment       = apartment
    def __repr__(self):
        return '<User %r>' % (self.username)

class Image(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120))
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'))
    def __init__(self, filename):
        self.filename = filename


import datetime
class Apartment(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    poster      = db.Column(db.Integer)
    images      = db.relationship('Image', backref='apartment', lazy="dynamic")
    created_at  = db.DateTime()
    def __init__(self, description, poster):
        self.description = description
        self.poster      = poster
        self.created_at  = datetime.datetime.now()

class Message(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    text    = db.Column(db.String(140))
    owner   = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __init__(self, text, owner):
        self.text  = text
        self.owner = owner

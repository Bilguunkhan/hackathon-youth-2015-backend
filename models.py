from app import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email    = db.Column(db.String(120))
    password = db.Column(db.String(50))
    about    = db.Column(db.String(120))
    backgroundImage = db.Column(db.Integer)
    def __init__(self, username, email, password, about=None, backgroundImage=None):
        self.username = username 
        self.email    = email
        self.password = password
        self.about    = about
        self.backgroundImage = backgroundImage
    def __repr__(self):
        return '<User %r>' % (self.username)

class Image(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120))
    def __init__(self, filename):
        self.filename = filename


class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

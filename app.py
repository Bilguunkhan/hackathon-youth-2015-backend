from flask import Flask, request 
from flask_jwt import JWT, jwt_required 
from flask.ext.cors import CORS 
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
#cors = CORS(app, resources={r"/*": {"origins": "*", "methods": "*"}})
cors = CORS(app)
app.debug = True
app.config.from_object('config')
app.config['SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
from models import *
db.create_all()


jwt = JWT(app)

@jwt.authentication_handler
def authenticate(username, password):
    if username == 'joe' and password == 'pass':
        return User(id=1, username='joe')

@jwt.user_handler
def load_user(payload):
    if payload['user_id'] ==1:
        return User(id=1, username='joe')

@app.route('/protected')
@jwt_required()
def protected():
    return 'Success!'

@app.route('/api/v1/users', methods=['POST'])
#@jwt_required()
def register():
    user = request.get_json()['user']
    username = user['username']
    email    = user['email']
    password = user['password']
    u = User(username=username, email=email, password=password)
    db.session.add(u)
    db.session.commit()
    result = {}
    result['username'] = username
    result['email']    = username
    result['password'] = username
    return Flask.jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

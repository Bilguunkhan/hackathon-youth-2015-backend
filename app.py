from flask import Flask, request, jsonify, send_from_directory
from flask_jwt import JWT, jwt_required, current_user
from flask.ext.cors import CORS 
from flask.ext.sqlalchemy import SQLAlchemy
import json, os, uuid


app = Flask(__name__)
#cors = CORS(app, resources={r"/*": {"origins": "*", "methods": "*"}})
#cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.debug = True
app.config.from_object('config')
app.config['SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
from models import *
db.create_all()

jwt = JWT(app)

@jwt.authentication_handler
def authenticate(username, password):
    u = User.query.filter_by(username=username, password=password).first()
    if u:
        return u

@jwt.user_handler
def load_user(payload):
    u = User.query.get(payload['user_id'])
    return u

@app.route('/protected')
@jwt_required()
def protected():
    return 'Success! current user id is '+str(current_user.id)

# Registration
@app.route('/api/v1/users', methods=['POST'])
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
    result['email']    = email
    result['password'] = password
    return json.dumps(result)

@app.route('/current_user_id')
@jwt_required()
def get_current_user_id():
    return str(current_user.id)

# File upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        return f_name

# User resource
@app.route('/api/v1/users/<int:user_id>')
@jwt_required()
def get_user(user_id):
    u = User.query.get(user_id)
    result = {}
    result['id'      ] = u.id
    result['username'] = u.username
    result['email'   ] = u.email
    result['password'] = ""
    result['about'   ] = u.about
    result['backgroundImage'] = u.backgroundImage
    return json.dumps({"user": result})

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = request.get_json()['user']
    about           = user['about']
    backgroundImage = user['backgroundImage']
    u = User.query.get(user_id)
    u.about = about
    u.backgroundImage = backgroundImage
    db.session.commit()
    result = {}
    result['id'      ] = u.id
    result['username'] = u.username
    result['email'   ] = u.email
    result['password'] = ""
    result['about'   ] = u.about
    result['backgroundImage'] = u.backgroundImage
    return json.dumps({"user": result})



# Image resource
@app.route('/api/v1/images', methods=['POST'])
@jwt_required()
def create_image():
    image    = request.get_json()['image']
    filename = image['filename']
    image = Image(filename = filename)
    db.session.add(image)
    db.session.commit()
    result = {}
    result['id'      ] = image.id
    result['filename'] = filename
    return json.dumps({"image": result})
@app.route('/api/v1/images/<int:image_id>', methods=['GET'])
@jwt_required()
def get_image(image_id):
    image = Image.query.get(image_id)
    result = {}
    result['id'      ] = image.id
    result['filename'] = image.filename
    return json.dumps({"image": result})

@app.route('/images/<path:path>', methods=['GET'])
def get_image_file(path):
    return send_from_directory('uploads', path)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


#import gevent.wsgi
#import werkzeug.serving
#@werkzeug.serving.run_with_reloader
#def runServer():
#    app.debug = True
#    ws = gevent.wsgi.WSGIServer(('0.0.0.0', 5001), app)
#    ws.serve_forever()


import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql://root:pass@localhost/hackathon_youth'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

UPLOAD_FOLDER=os.path.join(basedir, 'uploads')

# it represents how seconds later toke will be expired
JWT_EXPIRATION_DELTA = 3600 # about 1 hour

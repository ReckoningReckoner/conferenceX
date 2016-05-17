from flask import Flask
from secrets import SECRET_KEY, DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import conferenceX.views

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='9a166ff6e2c60eb0f0504329'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes
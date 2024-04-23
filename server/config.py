from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
load_dotenv()




app = Flask(__name__,
             static_url_path='',
            static_folder='../client/build',
            template_folder='../client/build')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') 
print("Database URI:", os.environ.get('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production!

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
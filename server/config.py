# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_restful import Api
# from flask_cors import CORS
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
# import os
# from dotenv import load_dotenv
# load_dotenv()




# app = Flask(__name__,
#              static_url_path='',
#             static_folder='../client/build',
#             template_folder='../client/build')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') 
# print("Database URI:", os.environ.get('DATABASE_URI'))
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production!

# db = SQLAlchemy(app)
# api = Api(app)
# migrate = Migrate(app, db)
# CORS(app)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)

from flask import Flask, send_from_directory
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

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
print("Database URI:", os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')  # Fallback to 'super-secret' if not set

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Ensure the Flask server hands over handling to React Router for undefined routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.template_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)  # Use host='0.0.0.0' to make server available on your network
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

import models, resources

if __name__ == '__main__':
    app.run(debug=True)


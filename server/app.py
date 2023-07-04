from flask import Flask, request, make_response, jsonify
from datetime import datetime
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


from models import db, User, Admin, Property, PropertyCategory, BoughtProperty
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555)
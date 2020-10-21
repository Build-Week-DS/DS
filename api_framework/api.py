from flask import Flask, render_template, request
import jinja2
from flask_sqlalchemy import SQLAlchemy
from .models import DB
from os import getenv
from .predict import predict_price
# from .airbnb import 
import requests


def create_app():
    APP = Flask(__name__)

    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    DB.__init(app)

@APP.route('/')

def root():
    list_of_tuples = []

    for i in range(0, 10):
        list_of_tuples.append(("DUMMY AIRBNB", 1000000.00))
    
    return str(list_of_tuples)

class Airbnb(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(25))
    predicted_price = DB.Column(DB.Float)

    def __repr__(self):
        return f'< Name {self.name} --- Value {self.predicted_price} >'

@APP.route('/refresh')
def refresh():
    DB.drop_all()
    DB.create_all()
    DB.session.commit()
    return 'Data refreshed!'

if __name__ == '__main__':
     APP.run()
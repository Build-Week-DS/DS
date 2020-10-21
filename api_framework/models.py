"""
api_framework/models.py
model rons from this page
"""

import joblib
from flask_sqlalchemy import SQLAlchemy
# deserializing model to run
def  run_Model (model):
    model = joblib.load('*/erg_bryce_model01.jolib')



DB = flask_sqlalchemy()


class airbib(DB.Model):
    """
    creatinf the aibnb fuvtionality
    """
    def __repr__(self):
        pass
    

class prediction(DB.Model):
    """
    prediction button
    """
    def __repr__(self):
        pass
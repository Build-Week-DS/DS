from flask import Flask

from joblib import load

import pandas as pd

APP = Flask(__name__)

with open("../marcos_model.joblib", "rb") as file:
    model = load(file)

sfairbnb_df = pd.read_csv("../data/cleaned_data.csv")
sfairbnb_df = sfairbnb_df.drop(columns='Unnamed: 0', axis=1)
        
@APP.route('/')

def root():
    return str(model.predict(sfairbnb_df.iloc[:10]))
    
@APP.route('/about')

def about_page():
    return "Dataset selected and first model created in notebook by Bryce Natale and Erle Granger. Model tuned by Marcos Morales. API supplied by Eli Fulton."
    
if __name__ == '__main__':
     APP.run()
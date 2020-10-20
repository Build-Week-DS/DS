from flask import Flask

from flask_sqlalchemy import SQLAlchemy

import requests

APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

DB = SQLAlchemy(APP)

@APP.route('/')

def root():
  return "Ah ah ah! YOU DIDN'T SAY THE MAGIC WORD."


if __name__ == '__main__':
     APP.run()
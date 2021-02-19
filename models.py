from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(120), nullable=False)
    host_name = db.Column(db.String(120), nullable=False)
    period = db.Column(db.String(120), nullable=False)
    episodes = db.Column(db.Integer, nullable=False)
    about = db.Column(db.String, nullable=False)
    image_link = db.Column(db.String(500))

from flask import Flask, request,redirect,url_for, render_template, flash,session
# import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app=Flask(__name__)

# configuration
app.secret_key='this_is_my_secret_key'


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


# connection au base de donnée
db=SQLAlchemy()

migrate=Migrate(app, db)

# declaration du base de donnée au flask
db.db.init_app(app)





# creation du table 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password=db.Column(db.String(200), nullable=False)

    def __init__(self, Nom, email,password ):
        self.Nom = Nom
        self.email=email
        self.password = password


# appelez pour créer Schéma de table dans la base de données.
   
with app.app_context():
    db.create_all()







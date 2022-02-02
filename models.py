from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from flask_login import UserMixin
import os


database_path = os.environ["DATABASE_URL"]
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "postgresql://postgres:zaidwawi056@localhost:5432/data"
    app.config["SECRET_KEY"] = "#$%kekslonf@!3A"
    db.app = app
    db.init_app(app)


def rollback():
    db.session.rollback()


################### User model ##########
class data(db.Model):
    id = Column(Integer , primary_key= True)
    name = Column(String())

################### total model #######################

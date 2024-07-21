from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import json


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(10280), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    parent_email = db.Column(db.Text, unique=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, username, password, email, parent_email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.parent_email = parent_email


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    child_emails = db.Column(db.Text, unique=False, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email


class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2000), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    perpetrator = db.Column(db.Text, nullable=False)
from flask import Flask, request, jsonify, render_template, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
import os
from werkzeug.utils import secure_filename
import random

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='/static')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.secret_key = os.environ.get('SECRET_KEY')

    from .routes import bp  # Assuming you have a 'routes.py' file
    app.register_blueprint(bp)

    # from .models import db
    # db.init_app(app)
    return app
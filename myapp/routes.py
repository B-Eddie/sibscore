import werkzeug
from flask import Blueprint, request, render_template, session, flash, redirect, url_for, current_app, \
    send_from_directory, jsonify
from myapp import db, create_app
# from .models import ShiftCalendar, Employee, Supervisor, Requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import os
from werkzeug.utils import secure_filename
import random
import json
from datetime import timedelta, datetime

bp = Blueprint('bp', __name__, static_folder='',
               static_url_path='/static')  # bp = Blueprint('bp', __name__, static_folder='static',

@bp.route('/')
def index():
    return 'hello world'
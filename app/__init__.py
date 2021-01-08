from flask import Flask, request, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import json
import os
import sys

print("test")

app = Flask(__name__)
cors = CORS(app)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from app import routes, models
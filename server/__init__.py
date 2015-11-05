from flask import Flask
from flask.ext.pymongo import PyMongo

# Define the WSGI application object
app = Flask(__name__)
mongo = PyMongo(app)

import server.views
from server.commands import ping_pong

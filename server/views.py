from flask import Flask
from server import app

@app.route('/')
def hello():
    return 'Hello World!'

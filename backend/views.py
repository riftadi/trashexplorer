from run import app, db
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message': 'Hello world!'})


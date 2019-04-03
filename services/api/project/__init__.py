# services/users/project/__init__.py


import os
from flask import Flask, jsonify, request
# from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
import sys


# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
mongo = PyMongo(app)  # new


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@app.route('/add/user', methods=['POST'])
def add_user():

    user = mongo.db.users
    post_data = request.get_json('user')
    print(post_data, file=sys.stderr)
    # print(post_data['name'], file=sys.stderr)
    user.insert({'name': post_data['name']})
    return jsonify({
        'status': 'ok'
    })


@app.route('/user/<user>', methods=['GET'])
def find_user(user):

    user = mongo.db.users.find_one_or_404({'name': user})
    return 'ok'

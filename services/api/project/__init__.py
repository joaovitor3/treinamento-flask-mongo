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


@app.route('/user/create', methods=['POST'])
def requestUser():
    post_data = request.get_json('user')
    user = mongo.db.users
    user.insert({'user': post_data['user']})
    print(post_data['user'], file=sys.stderr)
    return jsonify({
        "user": "sucess"
    })


@app.route("/api/find/<username>", methods=['GET'])
def user_profile(username):
    mongo.db.users.find_one_or_404({"user": username})
    return "Deu certo"

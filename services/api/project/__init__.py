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

@app.route("/create/user", methods=['POST'])
def createUser():
    user = mongo.db.users
    post_data = request.get_json()
    user.insert({'name': post_data['name']})
    print(post_data['name'], file=sys.stderr)
    return jsonify({
        'status': 'user cadastrado!'
    })

@app.route("/find/<user>", methods=['GET'])
def findUser(user):
    mongo.db.users.find_one_or_404({'name': user})
    return "user encontrado!"



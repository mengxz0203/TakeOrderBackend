import json

import flask
from flask import jsonify, request
from flask_cors import CORS

from app_util import app
from config.db_config import db
from model.dish import Dish

dish = flask.Blueprint('dish', __name__)
CORS(dish, supports_credentials=True)


@dish.route('/')
def hello_world():  # put application's code here

    return 'Hello World!'


@dish.route('/get_dish', methods=['GET'])
def get_dish():
    dish_query = Dish.query.all()
    res = [item.to_dict() for item in dish_query]
    return res


@dish.route('/create_dish', methods=['POST'])
def create_dish():
    data = json.loads(request.data)
    new_dish = Dish()
    new_dish.name = data['name']
    db.session.add(new_dish)
    db.session.commit()
    return data

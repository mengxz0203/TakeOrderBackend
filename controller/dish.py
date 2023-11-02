import flask
from flask_cors import CORS

from app_util import app
from config.db_config import db
from model.dish import Dish

dish = flask.Blueprint('dish', __name__)
CORS(dish, supports_credentials=True)


@dish.route('/')
def hello_world():  # put application's code here

    return 'Hello World!'


@dish.route('/get_dish')
def get_dish():
    dish_query = Dish.query.all()
    res = [item.to_dict() for item in dish_query]
    return res


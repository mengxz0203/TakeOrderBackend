from config.db_config import db
from sqlalchemy_serializer import SerializerMixin


class Dish(db.Model, SerializerMixin):
    __tablename__ = 'dish'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, default='', doc='菜名')
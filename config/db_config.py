from flask_sqlalchemy import SQLAlchemy

from app_util import app

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mxz970203@localhost/take_order'

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
db = SQLAlchemy(app)


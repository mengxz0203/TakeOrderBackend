from app_util import app
from controller.dish import dish


app.register_blueprint(dish)

if __name__ == '__main__':
    app.run(debug=True)

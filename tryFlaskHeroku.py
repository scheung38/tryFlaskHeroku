from flask import Flask
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route('/')
def hello_world():
    return 'Hello World this is tryFlaskHeroku!'


if __name__ == '__main__':
    heroku.init_app(app)
    app.run()

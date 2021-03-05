from flask import Flask
from flask_restful import Resource, Api
from resources.user import User, UserList, UserRegister
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, '/user/<string:_id>')  # 127.0.0.1:5000/user/1
api.add_resource(UserRegister, '/user')
api.add_resource(UserList, '/users/')

if __name__ == '__main__':
    app.run(port=4000, debug=True)

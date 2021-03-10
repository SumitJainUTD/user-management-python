from flask import Flask
from flask_restful import Api
from resources.user import User, UserList, UserRegister
from resources.profile import Profile
from resources.role import Role, RoleAdd, RoleList
from flask_login import LoginManager
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret"
api = Api(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/home")
def home():
    return "<h1> This is a home page </h1>"


api.add_resource(User, '/user/<string:_id>')  # 127.0.0.1:5000/user/1
api.add_resource(UserRegister, '/user')
api.add_resource(UserList, '/users/')
api.add_resource(Profile, '/profile')
api.add_resource(Role, '/role/<string:_id>')  # 127.0.0.1:5000/role/1
api.add_resource(RoleAdd, '/role')
api.add_resource(RoleList, '/roles/')

if __name__ == '__main__':
    app.run(port=4000, debug=True)

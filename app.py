from flask import Flask
from flask_restful import Api
from resources.user import User, UserList, UserRegister, UserLogin, MakeUserAdmin
from resources.role import Role, RoleAdd, RoleList
from flask_jwt_extended import JWTManager
from models.user import UserModel
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret"
api = Api(app)
db.init_app(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    print(identity)
    is_admin = UserModel.check_if_user_is_admin(identity)
    print("is_admin  " + str(is_admin))
    return {
        'is_admin': is_admin
    }


@app.route("/home")
def home():
    return "<h1> This is a home page </h1>"


api.add_resource(User, '/user/<string:id>')  # 127.0.0.1:5000/user/1
api.add_resource(UserRegister, '/user')
api.add_resource(UserList, '/users/')
api.add_resource(Role, '/role/<string:id>')  # 127.0.0.1:5000/role/1
api.add_resource(RoleAdd, '/role')
api.add_resource(RoleList, '/roles/')
api.add_resource(UserLogin, '/login')
api.add_resource(MakeUserAdmin, '/make-user-admin/<string:id>')  # 127.0.0.1:5000/user/1

if __name__ == '__main__':
    app.run(port=4000, debug=True)

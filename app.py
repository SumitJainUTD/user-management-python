from flask import Flask
from flask_restful import Resource, Api
from resources.user import User, UserList, UserRegister

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user/<string:_id>')  # 127.0.0.1:5000/user/1
api.add_resource(UserRegister, '/user')
api.add_resource(UserList, '/users/')

app.run(port=4000, debug=True)

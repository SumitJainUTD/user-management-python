import datetime
from flask_restful import Resource
from flask import request
from models.user import UserModel
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


class User(Resource):

    def get(self, _id):
        user = UserModel.find_by_user_id(_id)
        if user:
            return user.json(), 200
        else:
            return {'user': None}, 404

    def delete(self, _id):
        print("deleting")
        user = UserModel.find_by_user_id(_id)
        if user:
            UserModel.delete_from_db(user)
            return {'message': "user successfully deleted"}, 200
        else:
            return {'message': "user not found"}, 200


class UserRegister(Resource):

    def post(self):
        data = request.get_json()
        if UserModel.find_by_user_name(data['user_name']):
            return {"message": "user name already taken"}, 400

        if UserModel.find_by_email_id(data['email']):
            return {"message": data['email'] + "email is already registered"}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')

        public_id = str(uuid.uuid4())

        dt = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        user = UserModel(public_id=public_id, user_name=data['user_name'], password=hashed_password, email=data['email'],
                         created_at=dt, updated_at=dt, role_id=3)
        user.save_to_db()
        return {"message": user.user_name + " is created"}, 201


class UserList(Resource):

    def get(self):
        temp_users = []
        for u in UserModel.get_all_users():
            temp_users.append(u.json())
        return {'users': temp_users}

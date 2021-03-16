import datetime
from flask_restful import Resource, reqparse
from flask import request
from models.user import UserModel, RoleModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, decode_token, get_jwt

import uuid

parser = reqparse.RequestParser()


def validate_admin(token):
    x = token.split()
    claims = decode_token(x[1])
    print(claims)
    if not claims['is_admin']:
        return True
    else:
        return False


class User(Resource):

    def get(self, id):
        user = UserModel.find_by_user_id(id)
        if user:
            return user.json(), 200
        else:
            return {'user': None}, 404

    @jwt_required()
    def delete(self, id):
        token = request.headers.get('Authorization')
        # x = token.split()
        # claims = decode_token(x[1])
        # print(claims)
        # if not claims['is_admin']:
        #     return {
        #                'message': 'Unauthorized - Need admin privileges'
        #            }, 401;
        # print("deleting")
        result = validate_admin(token)
        if result:
            return {
                       'message': 'Unauthorized - Need admin privileges'
                   }, 401
        user = UserModel.find_by_user_id(id)
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

        # role = RoleModel.find_by_role_id(data['role_id'])
        # if role:
        #     pass
        #     # check for admin
        # else:
        #     return {"message": data['role_id'] + "role_id is does not exist"}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')

        public_id = str(uuid.uuid4())

        dt = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        user = UserModel(public_id=public_id, user_name=data['user_name'], password=hashed_password,
                         email=data['email'],
                         created_at=dt, updated_at=dt,
                         role_id=2)
                         # role_id=2)
        user.save_to_db()
        return {"message": user.user_name + " is created"}, 201


class UserList(Resource):

    def get(self):
        temp_users = []
        for u in UserModel.get_all_users():
            temp_users.append(u.json())
        return {'users': temp_users}


class UserLogin(Resource):

    def post(self):
        # get data from parser
        print("test sumit")
        # data = parser.parse_args()
        data = request.get_json()
        # find user in database
        print(data)
        user = UserModel.find_by_user_name(data['user_name'])
        # check check_password_hash()
        if user and check_password_hash(user.password, data['password']):
            token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': token,
                       'refresh_token': refresh_token
                   }, 200
        return {'message': "Unauthorized"}, 401


class MakeUserAdmin(Resource):
    @jwt_required()
    def put(self, id):
        token = request.headers.get('Authorization')
        result = validate_admin(token)
        if result:
            return {
                       'message': 'Unauthorized - Need admin privileges'
                   }, 401
        user = UserModel.find_by_user_id(id)
        if user:
            role = RoleModel.find_by_role_name("root")
            role_id = role.id
            user.role_id = role_id
            user.save_to_db()
            return {'message': "user successfully upgraded to have admin privileges"}, 202
        else:
            return {'message': "user not found"}, 200

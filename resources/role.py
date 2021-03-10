from flask_restful import Resource
from flask import request
from models.role import RoleModel
import datetime


class Role(Resource):

    def get(self, _id):
        role = RoleModel.find_by_role_id(_id)
        if role:
            return role.json(), 200
        else:
            return {'role': None}, 404


class RoleAdd(Resource):

    def post(self):
        data = request.get_json()
        if RoleModel.find_by_role_name(data['role_name']):
            return {"message": "role already exists"}, 400

        dt = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")
        role = RoleModel(role_name=data['role_name'], description=data['description'],
                         created_at=dt, updated_at=dt)
        role.save_to_db()
        return {"message": role.role_name + " is created"}, 201


class RoleList(Resource):
    def get(self):
        temp_roles = []
        for r in RoleModel.get_all_roles():
            temp_roles.append(r.json())
        return {'roles': temp_roles}

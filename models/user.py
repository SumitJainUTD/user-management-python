from db import db
from models.role import RoleModel


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(80), unique=True, nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.String(80))
    updated_at = db.Column(db.String(80))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __init__(self, public_id, user_name, password, email, created_at, updated_at, role_id):
        self.public_id = public_id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
        self.role_id = role_id

    def json(self):
        return {
            'id': self.id,
            'public_id': self.public_id,
            'user_name': self.user_name,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'role_id': self.role_id
        }

    @classmethod
    def find_by_user_name(cls, name):
        return cls.query.filter_by(user_name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_user_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def check_if_user_is_admin(cls, id):
        print("id: " +  str(id))
        user = cls.query.filter_by(id=id).first()
        print(user)
        role_id = user.role_id
        print("role id" + str(role_id))
        role = RoleModel.find_by_role_id(role_id)
        if role:
            return role.is_admin

    @classmethod
    def find_by_email_id(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

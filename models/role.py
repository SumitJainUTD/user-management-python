from db import db


class RoleModel(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.String(80))
    updated_at = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    users = db.relationship('UserModel', backref='role', lazy=True)

    def __init__(self, role_name, description, created_at, updated_at, is_admin):
        self.role_name = role_name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_admin = is_admin

    def json(self):
        return {
            'id': self.id,
            'role_name': self.role_name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_admin': self.is_admin
        }

    @classmethod
    def find_by_role_name(cls, name):
        return cls.query.filter_by(role_name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_role_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_roles(cls):
        return cls.query.all()

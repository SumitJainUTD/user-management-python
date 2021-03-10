from db import db


class Role(db.Model):
    __tablename__ = 'roles'

    _id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.String(80))
    updated_at = db.Column(db.String(80))

    def __init__(self, role_name, description, created_at, updated_at):
        self.role_name = role_name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def json(self):
        return {
            '_id': self._id,
            'role_name': self.role_name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
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
    def find_by_role_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    @classmethod
    def get_all_roles(cls):
        return cls.query.all()

import datetime
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    _id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.String(80))

    def __init__(self, user_name, password, email, created_at):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.created_at = created_at

    # def __init__(self, _id, user_name, password, email, created_at):
    #     self._id = _id
    #     self.user_name = user_name
    #     self.password = password
    #     self.email = email
    #     self.created_at = created_at

    def json(self):
        return {
            '_id': self._id,
            'user_name': self.user_name,
            'email': self.email,
            'created_at': self.created_at
        }

    # @classmethod
    # def get_user_obj(cls, user_name, password, email):
    #     cls.ids += 1
    #     return UserModel(cls.ids, user_name, password, email)
    #     UserModel.users.append(user)
    #     return user

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
    def find_by_user_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    @classmethod
    def find_by_email_id(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

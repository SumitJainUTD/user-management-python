import datetime


class UserModel:
    ids = 0
    users = []

    def __init__(self, _id, user_name, password, email):
        self._id = _id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.created_at = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    def json(self):
        return {
                '_id': self._id,
                'user_name': self.user_name,
                'email': self.email,
                'created_at': self.created_at
            }

    @classmethod
    def add_user(cls, user_name, password, email):
        cls.ids += 1
        return UserModel(cls.ids, user_name, password, email)

    @classmethod
    def find_by_user_name(cls, name):
        for u in cls.users:
            if u.user_name == name:
                return u
        return None

    @classmethod
    def find_by_user_id(cls, _id):
        for u in cls.users:
            if str(u._id) == str(_id):
                return u
        return None

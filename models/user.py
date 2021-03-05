import datetime
import sqlite3


class UserModel:
    ids = 0
    users = []

    def __init__(self, _id, user_name, password, email):
        self._id = _id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.created_at = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    def __init__(self, _id, user_name, password, email, created_at):
        self._id = _id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.created_at = created_at

    def json(self):
        return {
            '_id': self._id,
            'user_name': self.user_name,
            'email': self.email,
            'created_at': self.created_at
        }

    @classmethod
    def get_user_obj(cls, user_name, password, email):
        cls.ids += 1
        return UserModel(cls.ids, user_name, password, email)
        UserModel.users.append(user)
        return user

    @classmethod
    def add_user(cls, user_name, password, email):
        cls.ids += 1
        user = UserModel(cls.ids, user_name, password, email)
        UserModel.users.append(user)
        return user

    @classmethod
    def find_by_user_name(cls, name):
        connection = sqlite3.Connection('database.db')
        cursor = connection.cursor();

        query = "SELECT * FROM users where user_name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row:
            user = UserModel(row[0], row[1], row[2], row[3], row[4])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_user_id(cls, _id):
        connection = sqlite3.Connection('database.db')
        cursor = connection.cursor();

        query = "SELECT * FROM users where _id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = UserModel(row[0], row[1], row[2], row[3], row[4])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def delete_user_id(cls, _id):
        for u in cls.users:
            if str(u._id) == str(_id):
                cls.users.remove(u)
                return True
        return False

    @classmethod
    def find_by_email_id(cls, email):
        connection = sqlite3.Connection('database.db')
        cursor = connection.cursor();

        query = "SELECT * FROM users where email=?"
        result = cursor.execute(query, (email,))
        row = result.fetchone()
        if row:
            user = UserModel(row[0], row[1], row[2], row[3], row[4])
        else:
            user = None

        connection.close()
        return user

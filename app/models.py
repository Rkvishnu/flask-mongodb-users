# app/models.py

from app import mongo

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def from_json(json):
        return User(json['name'], json['email'], json['password'])

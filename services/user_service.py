# services/user_service.py
import os
import json
from models.user import UserModel

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")


class UserService:
    def __init__(self):
        # modelo que mexe no json
        self.model = UserModel()

    # pega todos os usuarios
    def get_all(self):
        return [u.to_dict() for u in self.model.get_all()]

    # pega usuario por id
    def get_by_id(self, user_id):
        u = self.model.get_by_id(user_id)
        return u.to_dict() if u else None

    # procura email
    def find_by_email(self, email):
        u = self.model.get_by_email(email)
        return u.to_dict() if u else None

    # cria usuario simples (sem senha)
    def create_user_simple(self, name, email, birthdate):
        users = self.model.get_all()
        last = max([u.id for u in users], default=0)
        new_id = last + 1

        # cria objeto usuario
        user = self.model._make_user(new_id, name, email, birthdate, "")
        self.model.add_user(user)
        return user

    # cria usuario com senha (registro)
    def create_user(self, name, email, password):
        users = self.model.get_all()
        last = max([u.id for u in users], default=0)
        new_id = last + 1

        user = self.model._make_user(new_id, name, email, "", password)
        self.model.add_user(user)
        return user

    # edita usuario
    def edit_user_simple(self, user_id, name, email, birthdate):
        # pega usuario
        u = self.model.get_by_id(user_id)
        if not u:
            return None

        # altera dados
        u.name = name
        u.email = email
        u.birthdate = birthdate

        # salva tudo
        self.model.save_all()
        return u

    # deleta usuario
    def delete_user(self, user_id):
        self.model.delete_user(user_id)

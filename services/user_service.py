from models.user import UserModel, User
from bottle import request
import os


class UserService:
    def __init__(self):
        self.model = UserModel()

    def get_all(self):
        return self.model.get_all()

    def get_by_id(self, uid):
        return self.model.get_by_id(uid)

    def create_user(self, name, email, password):
        # checa email
        if self.find_by_email(email):
            return None
        last = max([u.id for u in self.model.get_all()], default=0)
        new_id = last + 1
        user = User(id=new_id, name=name, email=email,
                    birthdate="", password=password)
        self.model.add_user(user)
        return user

    def find_by_email(self, email):
        for u in self.model.get_all():
            if u.email == email:
                return u
        return None

    def authenticate(self, email, password):
        u = self.find_by_email(email)
        if not u:
            return None
        if u.password == password:
            return u
        return None

    def edit_user(self, user):
        # formulario atualiza usuario (mantem password)
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        user.name = name
        user.email = email
        user.birthdate = birthdate
        self.model.update_user(user)

    def delete_user(self, uid):
        self.model.delete_user(uid)

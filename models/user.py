import json
import os

# Garante caminho correto para /data/users.json
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FILE_PATH = os.path.join(DATA_DIR, 'users.json')


class User:
    def __init__(self, id, name, email, birthdate="", password=""):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get('id'),
            data.get('name'),
            data.get('email'),
            data.get('birthdate', ""),
            data.get('password', "")
        )


class UserModel:
    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=2, ensure_ascii=False)

        self.users = self._load()

    def _load(self):
        """Carrega usuários do arquivo JSON."""
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]

    def _save(self):
        """Salva lista de usuários no JSON."""
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users],
                      f, indent=2, ensure_ascii=False)

    # CRUD básico
    def get_all(self):
        return self.users

    def get_by_id(self, user_id):
        return next((u for u in self.users if u.id == user_id), None)

    def get_by_email(self, email):
        return next((u for u in self.users if u.email == email), None)

    def add_user(self, user):
        self.users.append(user)
        self._save()

    def update_user(self, updated_user):
        for i, u in enumerate(self.users):
            if u.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                return

    def delete_user(self, user_id):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()

    # Criação rápida de usuário
    def _make_user(self, id, name, email, birthdate="", password=""):
        return User(id, name, email, birthdate, password)

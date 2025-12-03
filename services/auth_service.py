# services/auth_service.py
import os
import json
from bottle import response

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")


class AuthService:
    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2, ensure_ascii=False)

    def _load(self):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []

    def _save(self, users):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2, ensure_ascii=False)

    def _next_id(self, users):
        if not users:
            return 1
        return max(u.get("id", 0) for u in users) + 1

    def find_by_email(self, email):
        users = self._load()
        for u in users:
            if u.get("email") == email:
                return u
        return None

    # usado pelo controller: retorna user dict ou None
    def login(self, email, password):
        users = self._load()
        for u in users:
            if u.get("email") == email and u.get("password") == password:
                return u
        return None

    # usado pelo controller: tenta criar, retorna (True, user) ou (False, msg)
    def register(self, name, email, password):
        users = self._load()
        if self.find_by_email(email):
            return False, "Email já existe"
        new_id = self._next_id(users)
        user = {
            "id": new_id,
            "name": name,
            "email": email,
            "birthdate": "",   # mantemos campo para compatibilidade
            "password": password
        }
        users.append(user)
        self._save(users)
        return True, user

    # helper para setar cookie de sessão (simples)
    def set_session(self, user):
        try:
            response.set_cookie("user_id", str(user.get("id")), path="/")
            return True
        except:
            return False

    def logout(self):
        try:
            response.set_cookie("user_id", "", path="/", expires=0)
            return True
        except:
            return False

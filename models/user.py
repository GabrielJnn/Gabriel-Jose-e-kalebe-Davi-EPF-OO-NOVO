# models/user.py - Modelo de dados para Usuário
# Define a estrutura de dados de um usuário do sistema

import json
import os

# Caminhos dos arquivos de dados
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FILE_PATH = os.path.join(DATA_DIR, 'users.json')


class User:
    # Classe que representa um usuário do sistema
    def __init__(self, id, name, email, birthdate="", password=""):
        self.id = id  # ID único do usuário
        self.name = name  # Nome completo
        self.email = email  # Email para login
        self.birthdate = birthdate  # Data de nascimento (opcional)
        self.password = password  # Senha para login

    def to_dict(self):
        # Converte o objeto para dicionário (para salvar em JSON)
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        # Cria um objeto User a partir de um dicionário (do JSON)
        return cls(
            data.get('id'),
            data.get('name'),
            data.get('email'),
            data.get('birthdate', ""),
            data.get('password', "")
        )


class UserModel:
    # Classe responsável por gerenciar a persistência dos usuários em arquivo JSON
    def __init__(self):
        # Garante que a pasta de dados existe
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        # Garante que o arquivo de usuários existe
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=2, ensure_ascii=False)

        # Carrega os usuários do arquivo
        self.users = self._load()

    def _load(self):
        """Carrega usuários do arquivo JSON."""
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Converte cada dicionário em objeto User
            return [User.from_dict(item) for item in data]

    def _save(self):
        """Salva lista de usuários no JSON."""
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            # Converte objetos User para dicionários e salva
            json.dump([u.to_dict() for u in self.users],
                      f, indent=2, ensure_ascii=False)

    # === OPERAÇÕES CRUD (Create, Read, Update, Delete) ===

    def get_all(self):
        # Retorna todos os usuários
        return self.users

    def get_by_id(self, user_id):
        # Busca um usuário pelo ID
        return next((u for u in self.users if u.id == user_id), None)

    def get_by_email(self, email):
        # Busca um usuário pelo email
        return next((u for u in self.users if u.email == email), None)

    def add_user(self, user):
        # Adiciona um novo usuário à lista e salva
        self.users.append(user)
        self._save()

    def update_user(self, updated_user):
        # Atualiza um usuário existente
        for i, u in enumerate(self.users):
            if u.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                return

    def delete_user(self, user_id):
        # Remove um usuário da lista e salva
        self.users = [u for u in self.users if u.id != user_id]
        self._save()

    # === MÉTODO AUXILIAR ===
    def _make_user(self, id, name, email, birthdate="", password=""):
        # Cria um novo objeto User (método auxiliar)
        return User(id, name, email, birthdate, password)

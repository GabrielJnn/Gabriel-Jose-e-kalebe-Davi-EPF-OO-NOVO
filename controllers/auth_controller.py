# controllers/auth_controller.py
from bottle import Bottle, request, response
from controllers.base_controller import BaseController
from services.user_service import UserService

auth_routes = Bottle()
BaseController(auth_routes)  # registra / e /static no root do merge


def _get_logged_user_id():
    uid = request.get_cookie("user_id")
    try:
        return int(uid) if uid else None
    except:
        return None


@auth_routes.get('/login')
def login_get():
    return BaseController(auth_routes).render('login', error=None)


@auth_routes.post('/login')
def login_post():
    email = request.forms.get('email')
    password = request.forms.get('password')
    us = UserService()
    user = us.find_by_email(email)
    if not user or user.get('password') != password:
        return BaseController(auth_routes).render('login', error='Email ou senha inválidos')
    # set cookie simples
    response.set_cookie("user_id", str(user.get('id')), path="/")
    return BaseController(auth_routes).redirect('/plants')


@auth_routes.get('/register')
def register_get():
    return BaseController(auth_routes).render('register', error=None)


@auth_routes.post('/register')
def register_post():
    name = request.forms.get('name')
    email = request.forms.get('email')
    password = request.forms.get('password')
    us = UserService()
    if us.find_by_email(email):
        return BaseController(auth_routes).render('register', error='Email já existe')
    us.create_user(name, email, password)
    # após registrar, redireciona para login
    return BaseController(auth_routes).redirect('/login')


@auth_routes.get('/logout')
def logout():
    response.set_cookie("user_id", "", path="/", expires=0)
    return BaseController(auth_routes).redirect('/login')

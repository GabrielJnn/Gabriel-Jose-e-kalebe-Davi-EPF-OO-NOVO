# controllers/user_controller.py
from bottle import Bottle, request
from controllers.base_controller import BaseController
from services.user_service import UserService

# cria o router
user_routes = Bottle()

# cria o controller base simples
BaseController(user_routes)

# serviço que mexe no users.json
service = UserService()


@user_routes.get('/users')
def list_users():
    # pega todos os usuarios
    users = service.get_all()
    # mostra na tela
    return BaseController(user_routes).render('users', users=users)


@user_routes.get('/users/add')
def add_user_form():
    # mostra formulario vazio
    return BaseController(user_routes).render('user_form', user=None, action="/users/add")


@user_routes.post('/users/add')
def add_user_post():
    # pega dados do form
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')

    # salva usuario
    service.create_user_simple(name, email, birthdate)

    # volta pra lista
    return BaseController(user_routes).redirect('/users')


@user_routes.get('/users/edit/<uid:int>')
def edit_user_form(uid):
    user = service.get_by_id(uid)
    if not user:
        return "Usuário não encontrado"

    return BaseController(user_routes).render(
        'user_form',
        user=user,
        action=f"/users/edit/{uid}"
    )


@user_routes.post('/users/edit/<uid:int>')
def edit_user_post(uid):
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')

    service.edit_user_simple(uid, name, email, birthdate)

    return BaseController(user_routes).redirect('/users')


@user_routes.post('/users/delete/<uid:int>')
def delete_user(uid):
    service.delete_user(uid)
    return BaseController(user_routes).redirect('/users')

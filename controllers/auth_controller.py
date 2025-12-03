from bottle import Bottle, request, redirect
from controllers.base_controller import BaseController
from services.user_service import UserService

auth_routes = Bottle()

# cria BaseController apenas se este for montado separadamente (não duplicar root)
BaseController(auth_routes)  # registra '/', '/static' etc (merge segura)


class AuthController:
    def __init__(self, app):
        self.app = app
        self.user_service = UserService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', method=['GET'], callback=self.login_get)
        self.app.route('/login', method=['POST'], callback=self.login_post)
        self.app.route('/register', method=['GET'], callback=self.register_get)
        self.app.route(
            '/register', method=['POST'], callback=self.register_post)
        self.app.route('/logout', method=['GET'], callback=self.logout)

    # views simples
    def login_get(self):
        return self.app.parent.render('login', error=None) if hasattr(self.app, 'parent') else self.app.request.environ.get('bottle.request').template('login', error=None)

    def login_post(self):
        email = request.forms.get('email')
        password = request.forms.get('password')
        user = self.user_service.authenticate(email, password)
        if not user:
            return self.app.parent.render('login', error='Email ou senha inválidos') if hasattr(self.app, 'parent') else self.app.request.environ.get('bottle.request').template('login', error='Email ou senha inválidos')
        # set cookie simples
        from bottle import response
        response.set_cookie('user_id', str(user.id), path='/')
        redirect('/plants')

    def register_get(self):
        return self.app.parent.render('register', error=None) if hasattr(self.app, 'parent') else self.app.request.environ.get('bottle.request').template('register', error=None)

    def register_post(self):
        name = request.forms.get('name')
        email = request.forms.get('email')
        password = request.forms.get('password')
        # cria usuario
        created = self.user_service.create_user(name, email, password)
        if not created:
            return self.app.parent.render('register', error='Email já existe') if hasattr(self.app, 'parent') else self.app.request.environ.get('bottle.request').template('register', error='Email já existe')
        from bottle import response
        # pega id do usuario criado
        u = self.user_service.find_by_email(email)
        response.set_cookie('user_id', str(u.id), path='/')
        redirect('/plants')

    def logout(self):
        from bottle import response
        response.set_cookie('user_id', "", path='/', expires=0)
        redirect('/login')


# monta controller no Bottle local
AuthController(auth_routes)

from bottle import static_file, request


class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def _setup_base_routes(self):
        # rotas basicas
        self.app.route('/', method='GET', callback=self.home_page)
        self.app.route('/helper', method=['GET'], callback=self.helper)
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def home_page(self):
        # verifica se usuário está logado
        uid = self._get_logged_user_id()
        if uid:
            # usuário logado, vai para plantas
            return self.redirect('/plants')
        else:
            # usuário não logado, mostra página inicial
            return self.render('home')

    def _get_logged_user_id(self):
        uid = request.get_cookie("user_id")
        try:
            return int(uid) if uid else None
        except:
            return None

    def helper(self):
        return self.render('helper-final')

    def serve_static(self, filename):
        # serve arquivos estaticos
        return static_file(filename, root='./static')

    def render(self, template, **context):
        from bottle import template as b_template
        return b_template(template, **context)

    def redirect(self, path, code=302):
        from bottle import HTTPResponse, response as bottle_response
        try:
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            # fallback js
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )

# controllers/base_controller.py - Controller base com funcionalidades comuns
# Este arquivo contém funções básicas que todos os controllers usam

from bottle import static_file, request


class BaseController:
    def __init__(self, app):
        # Recebe a aplicação Bottle
        self.app = app
        # Configura as rotas básicas
        self._setup_base_routes()

    def _setup_base_routes(self):
        # === ROTAS BÁSICAS ===
        # Página inicial (/)
        self.app.route('/', method='GET', callback=self.home_page)
        # Página de ajuda (/helper)
        self.app.route('/helper', method=['GET'], callback=self.helper)
        # Servir arquivos estáticos (/static/...)
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def home_page(self):
        # Verifica se o usuário está logado
        uid = self._get_logged_user_id()
        if uid:
            # Se estiver logado, vai direto para a lista de plantas
            return self.redirect('/plants')
        else:
            # Se não estiver logado, mostra a página inicial
            return self.render('home')

    def _get_logged_user_id(self):
        # Pega o ID do usuário do cookie de sessão
        uid = request.get_cookie("user_id")
        try:
            # Converte para inteiro se existir
            return int(uid) if uid else None
        except:
            # Retorna None se não conseguir converter
            return None

    def helper(self):
        # Renderiza a página de ajuda/guia do projeto
        return self.render('helper-final')

    def serve_static(self, filename):
        # Serve arquivos estáticos (CSS, JS, imagens)
        return static_file(filename, root='./static')

    def render(self, template, **context):
        # Renderiza um template HTML com variáveis de contexto
        from bottle import template as b_template
        return b_template(template, **context)

    def redirect(self, path, code=302):
        # Redireciona o usuário para outra página
        from bottle import HTTPResponse, response as bottle_response
        try:
            # Método normal de redirecionamento
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            # Método alternativo usando JavaScript (fallback)
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )

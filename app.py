# app.py - Configuração principal da aplicação PlantsVsTime
# Esta classe configura e inicializa o servidor web Bottle

from bottle import Bottle
from config import Config


class App:
    def __init__(self):
        # Cria uma instância do framework Bottle
        self.bottle = Bottle()

    def setup_routes(self):
        # Importa e configura todas as rotas dos controllers
        from controllers import init_controllers
        init_controllers(self.bottle)

    def run(self):
        # Configura as rotas antes de iniciar o servidor
        self.setup_routes()
        # Inicia o servidor web com as configurações do Config
        self.bottle.run(
            host=Config.HOST,
            port=Config.PORT,
            debug=Config.DEBUG,
            reloader=Config.RELOADER
        )


def create_app():
    # Factory function para criar instâncias da aplicação
    return App()

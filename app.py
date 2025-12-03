from bottle import Bottle
from config import Config


class App:
    def __init__(self):
        self.bottle = Bottle()

    def setup_routes(self):
        from controllers import init_controllers
        init_controllers(self.bottle)

    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=Config.HOST,
            port=Config.PORT,
            debug=Config.DEBUG,
            reloader=Config.RELOADER
        )


def create_app():
    return App()

from bottle import Bottle
from controllers.base_controller import BaseController


def init_controllers(app: Bottle):
    """
    Inicializa rotas principais e merge das rotas dos controllers.
    """
    # cria rota base (home, static) apenas uma vez
    root = Bottle()
    BaseController(root)  # configura rotas base como / e /static
    app.merge(root)

    # importa e adiciona os controllers da app
    from controllers.auth_controller import auth_routes
    from controllers.plant_controller import plant_routes
    from controllers.watering_controller import watering_routes

    app.merge(auth_routes)
    app.merge(plant_routes)
    app.merge(watering_routes)

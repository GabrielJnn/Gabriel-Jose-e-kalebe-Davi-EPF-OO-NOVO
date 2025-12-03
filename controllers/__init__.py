# controllers/__init__.py
from bottle import Bottle
from controllers.base_controller import BaseController


def init_controllers(app: Bottle):
    # registra rotas base (/, /static) em um Bottle separado e merge
    root = Bottle()
    BaseController(root)
    app.merge(root)

    # importa e junta os routers dos controllers
    from controllers.auth_controller import auth_routes
    from controllers.user_controller import user_routes
    from controllers.plant_controller import plant_routes
    from controllers.watering_controller import watering_routes

    app.merge(auth_routes)
    app.merge(user_routes)
    app.merge(plant_routes)
    app.merge(watering_routes)

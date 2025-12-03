# controllers/__init__.py
from bottle import Bottle
from controllers.base_controller import BaseController


def init_controllers(app: Bottle):
    print("DEBUG: init_controllers called")
    # registra rotas base (/, /static) em um Bottle separado e merge
    root = Bottle()
    BaseController(root)
    app.merge(root)

    # importa e junta os routers dos controllers
    print("DEBUG: importing auth_controller")
    from controllers import auth_controller
    print("DEBUG: importing user_controller")
    from controllers import user_controller
    print("DEBUG: importing plant_controller")
    from controllers import plant_controller
    print("DEBUG: importing watering_controller")
    from controllers import watering_controller

    print("DEBUG: merging auth_routes")
    app.merge(auth_controller.auth_routes)
    print("DEBUG: merging user_routes")
    app.merge(user_controller.user_routes)
    print("DEBUG: merging plant_routes")
    app.merge(plant_controller.plant_routes)
    print("DEBUG: merging watering_routes")
    app.merge(watering_controller.watering_routes)
    print("DEBUG: all controllers merged")

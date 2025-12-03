from bottle import Bottle
from controllers.base_controller import BaseController
from services.watering_service import WateringService

watering_routes = Bottle()

# controlador pequeno (servicos ja usados no plant_controller)


class WateringController:
    def __init__(self, app):
        self.app = app
        self.service = WateringService()
        # nao precisa de rotas novas aqui, plant_controller chama service
        # criado para organizacao futura


WateringController(watering_routes)

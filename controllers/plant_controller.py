from bottle import Bottle, request, redirect
from controllers.base_controller import BaseController
from services.plant_service import PlantService
from services.user_service import UserService
from services.watering_service import WateringService

plant_routes = Bottle()
# não cria root aqui para não duplicar, apenas routes de plants


class PlantController:
    def __init__(self, app):
        self.app = app
        self.plant_service = PlantService()
        self.user_service = UserService()
        self.watering_service = WateringService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/plants', method='GET', callback=self.list_plants)
        self.app.route(
            '/plants/new', method=['GET', 'POST'], callback=self.new_plant)
        self.app.route('/plants/edit/<pid:int>',
                       method=['GET', 'POST'], callback=self.edit_plant)
        self.app.route('/plants/delete/<pid:int>',
                       method='POST', callback=self.delete_plant)
        self.app.route('/plants/<pid:int>', method='GET',
                       callback=self.view_plant)
        # rota para regar (usa watering controller também)
        self.app.route('/plants/<pid:int>/water',
                       method='POST', callback=self.water_plant)

    def _get_logged_user_id(self):
        from bottle import request
        uid = request.get_cookie('user_id')
        if not uid:
            redirect('/login')
        try:
            return int(uid)
        except:
            redirect('/login')

    def list_plants(self):
        uid = self._get_logged_user_id()
        plants = self.plant_service.get_by_owner(uid)
        return self.app.render('plants_list', plants=plants, user_id=uid)

    def new_plant(self):
        uid = self._get_logged_user_id()
        if request.method == 'GET':
            return self.app.render('plant_form', plant=None, action='/plants/new', user_id=uid, error=None)
        # POST
        name = request.forms.get('name')
        species = request.forms.get('species')
        interval = request.forms.get('interval') or 3
        self.plant_service.create(uid, name, species, int(interval))
        redirect('/plants')

    def edit_plant(self, pid):
        uid = self._get_logged_user_id()
        p = self.plant_service.find_by_id(pid)
        if not p or p['owner_id'] != uid:
            redirect('/plants')
        if request.method == 'GET':
            return self.app.render('plant_form', plant=p, action=f'/plants/edit/{pid}', user_id=uid, error=None)
        # POST
        name = request.forms.get('name')
        species = request.forms.get('species')
        interval = request.forms.get('interval') or 3
        self.plant_service.update(pid, name, species, int(interval))
        redirect('/plants')

    def delete_plant(self, pid):
        uid = self._get_logged_user_id()
        p = self.plant_service.find_by_id(pid)
        if not p or p['owner_id'] != uid:
            redirect('/plants')
        self.plant_service.delete(pid)
        redirect('/plants')

    def view_plant(self, pid):
        uid = self._get_logged_user_id()
        p = self.plant_service.find_by_id(pid)
        if not p:
            redirect('/plants')
        waterings = self.watering_service.get_by_plant(pid)
        return self.app.render('waterings_list', plant=p, waterings=waterings, user_id=uid)

    def water_plant(self, pid):
        uid = self._get_logged_user_id()
        p = self.plant_service.find_by_id(pid)
        if not p or p['owner_id'] != uid:
            redirect('/plants')
        from datetime import date
        today = date.today().isoformat()
        self.watering_service.create(pid, uid, today)
        redirect(f'/plants/{pid}')


PlantController(plant_routes)

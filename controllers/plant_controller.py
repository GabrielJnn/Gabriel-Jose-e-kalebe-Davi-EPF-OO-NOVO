# controllers/plant_controller.py
from bottle import Bottle, request, redirect
from controllers.base_controller import BaseController
from services.plant_service import PlantService
from services.watering_service import WateringService

plant_routes = Bottle()
# não registramos BaseController aqui para evitar duplicar / (já feito no __init__)


def _require_login():
    uid = request.get_cookie("user_id")
    try:
        return int(uid) if uid else None
    except:
        return None


@plant_routes.get('/plants')
def plants_list():
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    ps = PlantService()
    plants = ps.get_by_owner(uid)
    return BaseController(plant_routes).render('plants_list', plants=plants, user_id=uid)


@plant_routes.get('/plants/new')
def plant_new():
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    return BaseController(plant_routes).render('plant_form', plant=None, action='/plants/new', user_id=uid, error=None)


@plant_routes.post('/plants/new')
def plant_create():
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    name = request.forms.get('name')
    species = request.forms.get('species')
    interval = request.forms.get('interval') or 3
    ps = PlantService()
    ps.create(uid, name, species, int(interval))
    return redirect('/plants')


@plant_routes.get('/plants/edit/<pid:int>')
def plant_edit(pid):
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    ps = PlantService()
    p = ps.find_by_id(pid)
    if not p or p.get('owner_id') != uid:
        return BaseController(plant_routes).redirect('/plants')
    return BaseController(plant_routes).render('plant_form', plant=p, action=f'/plants/edit/{pid}', user_id=uid, error=None)


@plant_routes.post('/plants/edit/<pid:int>')
def plant_update(pid):
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    name = request.forms.get('name')
    species = request.forms.get('species')
    interval = request.forms.get('interval') or 3
    ps = PlantService()
    ps.update(pid, name, species, int(interval))
    return redirect('/plants')


@plant_routes.post('/plants/delete/<pid:int>')
def plant_delete(pid):
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    ps = PlantService()
    p = ps.find_by_id(pid)
    if not p or p.get('owner_id') != uid:
        return BaseController(plant_routes).redirect('/plants')
    ps.delete(pid)
    return redirect('/plants')


@plant_routes.get('/plants/<pid:int>')
def plant_detail(pid):
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    ps = PlantService()
    p = ps.find_by_id(pid)
    if not p:
        return BaseController(plant_routes).redirect('/plants')
    ws = WateringService()
    waterings = ws.get_by_plant(pid)
    return BaseController(plant_routes).render('waterings_list', plant=p, waterings=waterings, user_id=uid)

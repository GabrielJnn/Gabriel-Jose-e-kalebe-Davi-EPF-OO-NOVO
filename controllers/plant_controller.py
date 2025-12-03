# controllers/plant_controller.py - Controller das Plantas
# Gerencia todas as operações relacionadas às plantas dos usuários

from bottle import Bottle, request, redirect
from controllers.base_controller import BaseController
from services.plant_service import PlantService
from services.watering_service import WateringService

# Cria um grupo de rotas específico para plantas
plant_routes = Bottle()
# Nota: não registramos BaseController aqui para evitar duplicar a rota /


def _require_login():
    # Função auxiliar para verificar se o usuário está logado
    uid = request.get_cookie("user_id")
    try:
        return int(uid) if uid else None
    except:
        return None


@plant_routes.get('/plants')
def plants_list():
    # === LISTAR PLANTAS DO USUÁRIO ===
    # Verifica se o usuário está logado
    uid = _require_login()
    if not uid:
        # Se não estiver logado, redireciona para login
        return BaseController(plant_routes).redirect('/login')

    # Busca todas as plantas do usuário logado
    ps = PlantService()
    plants = ps.get_by_owner(uid)

    # Renderiza a página com a lista de plantas
    return BaseController(plant_routes).render('plants_list', plants=plants, user_id=uid)


@plant_routes.get('/plants/new')
def plant_new():
    # === FORMULÁRIO PARA CRIAR NOVA PLANTA ===
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')

    # Mostra o formulário vazio para criar uma nova planta
    return BaseController(plant_routes).render('plant_form', plant=None, action='/plants/new', user_id=uid, error=None)


@plant_routes.post('/plants/new')
def plant_create():
    # === SALVAR NOVA PLANTA ===
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')

    # Pega os dados do formulário
    name = request.forms.get('name')
    species = request.forms.get('species')
    interval = request.forms.get('interval') or 3  # padrão 3 dias se não informado

    # Salva a nova planta no banco de dados
    ps = PlantService()
    ps.create(uid, name, species, int(interval))

    # Redireciona para a lista de plantas
    return redirect('/plants')


@plant_routes.get('/plants/<pid:int>/edit')
def plant_edit(pid):
    uid = _require_login()
    if not uid:
        return BaseController(plant_routes).redirect('/login')
    ps = PlantService()
    p = ps.find_by_id(pid)
    if not p or p.get('owner_id') != uid:
        return BaseController(plant_routes).redirect('/plants')
    return BaseController(plant_routes).render('plant_form', plant=p, action=f'/plants/{pid}/edit', user_id=uid, error=None)


@plant_routes.post('/plants/<pid:int>/edit')
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


@plant_routes.post('/plants/<pid:int>/delete')
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

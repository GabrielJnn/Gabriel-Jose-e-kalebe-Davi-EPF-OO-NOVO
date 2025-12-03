# controllers/watering_controller.py
from bottle import Bottle, request, redirect
from services.watering_service import WateringService
from services.plant_service import PlantService

watering_routes = Bottle()


@watering_routes.post('/plants/<pid:int>/water')
def water_plant(pid):
    uid = request.get_cookie("user_id")
    try:
        uid = int(uid) if uid else None
    except:
        uid = None
    if not uid:
        return redirect('/login')
    ps = PlantService()
    p = ps.find_by_id(pid)
    if not p or p.get('owner_id') != uid:
        return redirect('/plants')
    from datetime import date
    today = date.today().isoformat()
    ws = WateringService()
    ws.create(pid, uid, today)
    return redirect(f'/plants/{pid}')

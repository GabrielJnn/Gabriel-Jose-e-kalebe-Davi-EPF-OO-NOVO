# services/plant_service.py - Serviço de Plantas
# Esta classe gerencia todas as operações relacionadas às plantas (CRUD)

import os
import json
from config import Config

# Caminhos dos arquivos de dados
DATA_DIR = Config.DATA_PATH
PLANTS_FILE = os.path.join(DATA_DIR, 'plants.json')


def _ensure():
    # Garante que a pasta de dados existe
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Garante que o arquivo de plantas existe (cria vazio se não existir)
    if not os.path.exists(PLANTS_FILE):
        with open(PLANTS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)


class PlantService:
    def __init__(self):
        # Inicializa o serviço garantindo que os arquivos existem
        _ensure()

    def _read(self):
        with open(PLANTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write(self, data):
        with open(PLANTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _next_id(self, items):
        if not items:
            return 1
        return max(i['id'] for i in items) + 1

    def get_all(self):
        return self._read()

    def get_by_owner(self, owner_id):
        # === BUSCAR PLANTAS DO USUÁRIO COM STATUS DE REGA ===
        # Esta função retorna as plantas do usuário com informações calculadas sobre próximas regas

        from services.watering_service import WateringService
        from datetime import datetime, timedelta

        ws = WateringService()

        # Filtra apenas as plantas que pertencem ao usuário
        plants = [p for p in self._read() if p['owner_id'] == owner_id]

        # === CALCULAR STATUS DE REGA PARA CADA PLANTA ===
        for plant in plants:
            plant_waterings = ws.get_by_plant(plant['id'])
            if plant_waterings:
                # Ordenar por data (mais recente primeiro) e pegar a primeira
                sorted_waterings = sorted(plant_waterings, key=lambda x: x['date'], reverse=True)
                last_watering_date = sorted_waterings[0]['date']
                plant['last_watering'] = last_watering_date

                # Calcular quantos dias faltam para a próxima rega
                try:
                    last_date = datetime.strptime(last_watering_date, '%Y-%m-%d').date()
                    interval_days = int(plant.get('watering_interval_days', 3))
                    next_watering = last_date + timedelta(days=interval_days)
                    today = datetime.now().date()

                    if next_watering > today:
                        days_until_next = (next_watering - today).days
                        plant['days_until_next'] = days_until_next
                        if days_until_next == 0:
                            plant['watering_status'] = 'urgent'
                            plant['watering_message'] = '🔥 Regar hoje!'
                        elif days_until_next == 1:
                            plant['watering_status'] = 'soon'
                            plant['watering_message'] = '🕐 Regar amanhã'
                        else:
                            plant['watering_status'] = 'ok'
                            plant['watering_message'] = f'✅ {days_until_next} dias'
                    else:
                        days_overdue = (today - next_watering).days
                        plant['days_until_next'] = -days_overdue  # negativo = atrasado
                        plant['watering_status'] = 'overdue'
                        plant['watering_message'] = f'⚠️ {days_overdue} dias atrasada'
                except (ValueError, KeyError):
                    plant['days_until_next'] = None
                    plant['watering_status'] = 'unknown'
                    plant['watering_message'] = '❓ Erro no cálculo'
            else:
                # Nunca foi regada
                plant['last_watering'] = None
                plant['days_until_next'] = None
                plant['watering_status'] = 'never'
                plant['watering_message'] = '❓ Nunca regada'
                plant['days_until_next_watering'] = None
                plant['watering_status'] = 'never_watered'

        return plants

    def find_by_id(self, pid):
        for p in self._read():
            if p['id'] == pid:
                return p
        return None

    def create(self, owner_id, name, species, interval):
        items = self._read()
        pid = self._next_id(items)
        rec = {"id": pid, "owner_id": owner_id, "name": name,
               "species": species, "watering_interval_days": int(interval)}
        items.append(rec)
        self._write(items)
        return rec

    def update(self, pid, name, species, interval):
        items = self._read()
        for i, p in enumerate(items):
            if p['id'] == pid:
                items[i]['name'] = name
                items[i]['species'] = species
                items[i]['watering_interval_days'] = int(interval)
                self._write(items)
                return items[i]
        return None

    def delete(self, pid):
        items = [p for p in self._read() if p['id'] != pid]
        self._write(items)

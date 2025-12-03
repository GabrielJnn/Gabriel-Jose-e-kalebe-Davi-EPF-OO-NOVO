import os
import json
from config import Config

DATA_DIR = Config.DATA_PATH
PLANTS_FILE = os.path.join(DATA_DIR, 'plants.json')


def _ensure():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(PLANTS_FILE):
        with open(PLANTS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)


class PlantService:
    def __init__(self):
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
        return [p for p in self._read() if p['owner_id'] == owner_id]

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

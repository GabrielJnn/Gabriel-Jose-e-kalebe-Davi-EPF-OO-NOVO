# services/watering_service.py
import os
import json
from config import Config

DATA_DIR = Config.DATA_PATH
W_FILE = os.path.join(DATA_DIR, 'waterings.json')


def _ensure():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(W_FILE):
        with open(W_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)


class WateringService:
    def __init__(self):
        _ensure()

    def _read(self):
        with open(W_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write(self, data):
        with open(W_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _next_id(self, items):
        if not items:
            return 1
        return max(i['id'] for i in items) + 1

    def get_all(self):
        return self._read()

    def get_by_plant(self, plant_id):
        return [w for w in self._read() if w['plant_id'] == plant_id]

    def create(self, plant_id, user_id, date):
        items = self._read()
        wid = self._next_id(items)
        rec = {"id": wid, "plant_id": plant_id,
               "user_id": user_id, "date": date}
        items.append(rec)
        self._write(items)
        return rec

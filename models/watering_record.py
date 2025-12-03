# models/watering_record.py
class WateringRecord:
    def __init__(self, id, plant_id, user_id, date):
        self.id = id
        self.plant_id = plant_id
        self.user_id = user_id
        self.date = date

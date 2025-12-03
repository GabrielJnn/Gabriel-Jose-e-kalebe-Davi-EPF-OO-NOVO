# models/plant.py
class Plant:
    def __init__(self, id, owner_id, name, species, watering_interval_days):
        self.id = id
        self.owner_id = owner_id
        self.name = name
        self.species = species
        self.watering_interval_days = watering_interval_days

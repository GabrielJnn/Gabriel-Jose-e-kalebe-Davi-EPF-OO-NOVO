# models/plant.py - Modelo de dados para Planta
# Define a estrutura de dados de uma planta no sistema PlantsVsTime

class Plant:
    # Classe que representa uma planta cadastrada no sistema
    def __init__(self, id, owner_id, name, species, watering_interval_days):
        self.id = id  # ID único da planta
        self.owner_id = owner_id  # ID do usuário dono da planta
        self.name = name  # Nome da planta (ex: "Orquídea")
        self.species = species  # Espécie da planta (ex: "Flor")
        self.watering_interval_days = watering_interval_days  # A cada quantos dias regar

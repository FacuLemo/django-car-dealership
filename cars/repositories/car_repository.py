from cars.models import Car
from utils.base_repo import BaseRepository

class CarRepository(BaseRepository):
    def __init__(self):
        self.model = Car
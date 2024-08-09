from cars.models import CarModel
from utils.base_repo import BaseRepository


class CarModelRepository(BaseRepository):
    def __init__(self):
        self.model = CarModel

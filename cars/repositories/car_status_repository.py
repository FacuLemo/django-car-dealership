from cars.models import CarStatus
from utils.base_repo import BaseRepository


class CarStatusRepository(BaseRepository):
    def __init__(self):
        self.model = CarStatus

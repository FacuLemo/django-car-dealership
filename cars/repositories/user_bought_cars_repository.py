from cars.models import UserBoughtCars
from utils.base_repo import BaseRepository


class UserBoughtCarsRepository(BaseRepository):
    def __init__(self):
        self.model = UserBoughtCars

from cars.models import UserBoughtCars
from typing import Optional
from django.db import models

from utils.base_repo import BaseRepository


class UserBoughtCarsRepository(BaseRepository):
    def __init__(self):
        self.model = UserBoughtCars

    def filter_by_user_id(self, uid: int) -> Optional[models.Model]:
        return self.model.objects.filter(user_id=uid).all()

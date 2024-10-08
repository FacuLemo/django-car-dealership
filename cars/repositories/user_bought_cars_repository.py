from typing import Optional

from django.db import models

from cars.models import UserBoughtCars
from utils.base_repo import BaseRepository


class UserBoughtCarsRepository(BaseRepository):
    def __init__(self):
        self.model = UserBoughtCars

    def filter_by_user_id(self, uid: int) -> Optional[models.Model]:
        return self.model.objects.filter(user_id=uid).all()

    def make_sale(self, user, car):
        sale = self.model(user=user, car=car)
        sale.save()

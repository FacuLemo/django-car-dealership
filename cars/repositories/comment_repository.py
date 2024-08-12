from cars.models import Car, Comment
from utils.base_repo import BaseRepository


class CommentRepository(BaseRepository):
    def __init__(self):
        self.model = Comment

    def get_by_car(self, car: Car):
        return self.model.objects.filter(car__id__exact=car.id)

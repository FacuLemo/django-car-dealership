from cars.models import Category
from utils.base_repo import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self):
        self.model = Category

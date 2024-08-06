from utils.base_repo import BaseRepository
from cars.models import Category

class CategoryRepository(BaseRepository):
    def __init__(self):
        self.model = Category
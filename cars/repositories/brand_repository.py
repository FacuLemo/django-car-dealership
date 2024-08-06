from cars.repositories.base import BaseRepository
from cars.models import Brand

class BrandRepository(BaseRepository):
    def __init__(self):
        self.model = Brand
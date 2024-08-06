from utils.base_repo import BaseRepository
from cars.models import Brand

class BrandRepository(BaseRepository):
    def __init__(self):
        self.model = Brand
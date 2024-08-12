from cars.models import Brand
from utils.base_repo import BaseRepository


class BrandRepository(BaseRepository):
    def __init__(self):
        self.model = Brand

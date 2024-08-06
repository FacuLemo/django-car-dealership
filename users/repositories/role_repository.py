from utils.base_repo import BaseRepository
from users.models import CosmeticRole

class CosmeticRoleRepository(BaseRepository):
    def __init__(self):
        self.model = CosmeticRole
from users.models import CosmeticRole
from utils.base_repo import BaseRepository


class CosmeticRoleRepository(BaseRepository):
    def __init__(self):
        self.model = CosmeticRole

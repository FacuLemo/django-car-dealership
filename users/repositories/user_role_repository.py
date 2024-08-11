from users.models import UserCosmeticRoles
from typing import Optional
from django.db import models

from utils.base_repo import BaseRepository


class UserRolesRepository(BaseRepository):
    def __init__(self):
        self.model = UserCosmeticRoles

    def filter_by_user_id(self, uid: int) -> Optional[models.Model]:
        return self.model.objects.filter(user_id=uid).all()

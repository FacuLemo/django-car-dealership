from django.contrib.auth.models import User

from utils.base_repo import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        self.model = User

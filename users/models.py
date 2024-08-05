from django.contrib.auth.models import User
from django.db import models


class CosmeticRole(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserCosmeticRoles(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    cosmetic_role = models.ForeignKey(
        CosmeticRole,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

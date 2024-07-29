from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class CosmeticRole(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AccountCosmeticRoles(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    cosmetic_role = models.ForeignKey(
        CosmeticRole,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

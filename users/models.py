from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class CosmeticRole(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_('name')
    )
    color = models.CharField(
        max_length=100,
        verbose_name=_('color')
    )

    def __str__(self):
        return self.name


class UserCosmeticRoles(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    cosmetic_role = models.ForeignKey(
        CosmeticRole,
        on_delete=models.CASCADE,
        verbose_name=_('cosmetic_role')
    )

    def __str__(self):
        return self.cosmetic_role.name

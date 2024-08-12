from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from cars.repositories.user_bought_cars_repository import UserBoughtCarsRepository
from users.repositories.user_repository import UserRepository
from users.repositories.user_role_repository import UserRolesRepository


class RoleView(View):
    model = User
    repo = UserRepository
    repocars = UserBoughtCarsRepository
    reporoles = UserRolesRepository


class UserProfileView(RoleView):
    template_name = "users/profile.html"

    def get(self, request, id):
        repo = self.repo()
        repocars = self.repocars()
        reporoles = self.reporoles()
        user = repo.get_or_404(id)
        bought_cars = repocars.filter_by_user_id(user.id)
        cosmetic_roles = reporoles.filter_by_user_id(user.id)

        return render(
            request,
            self.template_name,
            dict(
                user=user,
                bought_cars=bought_cars,
                cosmetic_roles=cosmetic_roles,
            ),
        )

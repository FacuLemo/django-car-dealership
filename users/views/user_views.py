from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from cars.repositories.user_bought_cars_repository import UserBoughtCarsRepository
from users.repositories.user_repository import UserRepository


class RoleView(View):
    model = User
    repo = UserRepository
    repocars = UserBoughtCarsRepository


class UserProfileView(RoleView):
    template_name = "users/profile.html"

    def get(self, request, id):
        repo = self.repo()
        repocars = self.repocars()
        user = repo.get_or_404(id)
        bought_cars = repocars.filter_by_property_name(user_id, user.id)

        return render(
            request,
            self.template_name,
            dict(
                user=user,
                bought_cars=bought_cars,
            ),
        )

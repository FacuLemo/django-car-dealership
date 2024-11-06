from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from cars.repositories.user_bought_cars_repository import UserBoughtCarsRepository
from users.repositories.user_repository import UserRepository
from users.repositories.user_role_repository import UserRolesRepository

from users.models import Profile

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

class ToggleLangView(RoleView):
    def post(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        print("🚀 ~ profile:", profile.lang)
        if profile:
            profile.lang = "es" if profile.lang  == "en" else "en"
            profile.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
from django.shortcuts import redirect, render
from django.views import View

from users.forms import UserRoleForm
from users.models import UserCosmeticRoles
from users.repositories.user_role_repository import UserRolesRepository


class UserRolesView(View):
    model = UserCosmeticRoles
    repo = UserRolesRepository
    form_class = UserRoleForm


class UserRolesListView(UserRolesView):
    template_name = "user_roles/list.html"

    def get(self, request):
        repo = self.repo()
        user_roles = repo.get_all()

        return render(
            request,
            self.template_name,
            dict(user_roles=user_roles),
        )


class UserRolesCreateView(UserRolesView):
    template_name = "user_roles/create.html"

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(form=form),
        )

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect("user_role_list")

        return render(
            request,
            "user_roles/create.html",
            dict(form=form),
        )


class UserRolesUpdateView(UserRolesView):
    template_name = "user_roles/update.html"

    def get(self, request, id):
        repo = self.repo()
        user_role = repo.get_or_404(id)
        form = self.form_class(instance=user_role)

        return render(
            request,
            self.template_name,
            dict(
                form=form,
                user_role=user_role,
            ),
        )

    def post(self, request, id):
        repo = self.repo()
        user_role = repo.get_or_404(id)
        form = self.form_class(request.POST, instance=user_role)
        if form.is_valid():
            form.save()
            return redirect("user_role_list")
        return render(
            request,
            self.template_name,
            dict(form=form),
        )


class UserRolesDeleteView(UserRolesView):
    def post(self, request, id):
        repo = self.repo()
        brand = repo.get_by_id(id)
        repo.delete(brand)
        return redirect("user_role_list")

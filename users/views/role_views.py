from django.shortcuts import redirect, render
from django.views import View

from users.forms import CosmeticRoleForm
from users.models import CosmeticRole
from users.repositories.role_repository import CosmeticRoleRepository


class RoleView(View):
    model = CosmeticRole
    repo = CosmeticRoleRepository
    form_class = CosmeticRoleForm


class RoleListView(RoleView):
    template_name = "roles/list.html"

    def get(self, request):
        repo = self.repo()
        roles = repo.get_all()

        return render(
            request,
            self.template_name,
            dict(roles=roles),
        )


class RoleCreateView(RoleView):
    template_name = "roles/create.html"

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
            return redirect("role_list")

        return render(
            request,
            "roles/create.html",
            dict(form=form),
        )


class RoleUpdateView(RoleView):
    template_name = "roles/update.html"

    def get(self, request, id):
        repo = self.repo()
        role = repo.get_or_404(id)
        form = self.form_class(
            instance=role,
        )

        return render(
            request,
            self.template_name,
            dict(
                form=form,
                role=role,
            ),
        )

    def post(self, request, id):
        repo = self.repo()
        role = repo.get_or_404(id)
        form = self.form_class(
            request.POST,
            instance=role,
        )
        if form.is_valid():
            form.save()
            return redirect("role_list")
        return render(
            request,
            self.template_name,
            dict(form=form),
        )


class RoleDeleteView(RoleView):
    def post(self, request, id):
        repo = self.repo()
        brand = repo.get_by_id(id)
        repo.delete(brand)
        return redirect("role_list")

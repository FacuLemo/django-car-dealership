from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from cars.forms import BrandForm
from cars.models import Brand
from cars.repositories.brand_repository import BrandRepository


class BrandView(View):
    model = Brand
    repo = BrandRepository
    form_class = BrandForm


class BrandListView(BrandView):
    template_name = "brands/list.html"

    def get(self, request):
        repo = self.repo()
        brands = repo.get_all()

        return render(
            request,
            self.template_name,
            dict(brands=brands),
        )


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, BrandView):
    template_name = "brands/create.html"
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(form=form),
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("brand_list")

        return render(
            request,
            "brands/create.html",
            dict(form=form),
        )


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, BrandView):
    template_name = "brands/update.html"
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def get(self, request, id):
        repo = self.repo()
        brand = repo.get_or_404(id)
        form = self.form_class(instance=brand)

        return render(
            request,
            self.template_name,
            dict(
                form=form,
                brand=brand,
            ),
        )

    def post(self, request, id):
        repo = self.repo()
        brand = repo.get_or_404(id)
        form = self.form_class(
            request.POST,
            request.FILES,
            instance=brand,
        )
        if form.is_valid():
            form.save()
            return redirect("brand_list")
        return render(
            request,
            self.template_name,
            dict(
                form=form,
            ),
        )


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, BrandView):
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def post(self, request, id):
        repo = self.repo()
        brand = repo.get_by_id(id)
        repo.delete(brand)
        return redirect("brand_list")

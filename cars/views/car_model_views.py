from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarModelForm
from cars.models import CarModel
from cars.repositories.car_model_repository import CarModelRepository


class CarModelView(View):
    model = CarModel
    repo = CarModelRepository
    form_class = CarModelForm


class CarModelListView(CarModelView):
    template_name = "car_model/list.html"

    def get(self, request):
        repo = self.repo()
        car_models = repo.get_all()

        return render(
            request,
            self.template_name,
            dict(car_models=car_models),
        )


class CarModelCreateView(LoginRequiredMixin, PermissionRequiredMixin, CarModelView):
    template_name = "car_model/create.html"
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
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect("car_model_list")

        return render(
            request,
            "car_model/create.html",
            dict(form=form),
        )


class CarModelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, CarModelView):
    template_name = "car_model/update.html"
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def get(self, request, id):
        repo = self.repo()
        car_model = repo.get_or_404(id)
        form = self.form_class(instance=car_model)

        return render(
            request,
            self.template_name,
            dict(
                form=form,
                car_model=car_model,
            ),
        )

    def post(self, request, id):
        repo = self.repo()
        car_model = repo.get_or_404(id)
        form = self.form_class(request.POST, instance=car_model)

        if form.is_valid():
            form.save()
            return redirect("car_model_list")

        return render(
            request,
            self.template_name,
            dict(form=form),
        )


class CarModelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, CarModelView):
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def post(self, request, id):
        repo = self.repo()
        car_model = repo.get_by_id(id)
        repo.delete(car_model)
        return redirect("car_model_list")

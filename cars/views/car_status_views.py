from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarStatusForm
from cars.models import CarStatus
from cars.repositories.car_status_repository import CarStatusRepository


class CarStatusView(View):
    model = CarStatus
    repo = CarStatusRepository
    form_class = CarStatusForm


class CarStatusListView(CarStatusView):
    template_name = "car_status/list.html"

    def get(self, request):
        repo = self.repo()
        car_status = repo.get_all()

        return render(
            request,
            self.template_name,
            dict(statuses=car_status),
        )


class CarStatusCreateView(LoginRequiredMixin, PermissionRequiredMixin, CarStatusView):
    template_name = "car_status/create.html"
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
            return redirect("car_status_list")

        return render(
            request,
            "car_status/create.html",
            dict(form=form),
        )


class CarStatusUpdateView(LoginRequiredMixin, PermissionRequiredMixin, CarStatusView):
    template_name = "car_status/update.html"
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def get(self, request, id):
        repo = self.repo()
        car_status = repo.get_or_404(id)
        form = self.form_class(instance=car_status)

        return render(
            request,
            self.template_name,
            dict(
                form=form,
                car_status=car_status,
            ),
        )

    def post(self, request, id):
        repo = self.repo()
        car_status = repo.get_or_404(id)
        form = self.form_class(request.POST, instance=car_status)

        if form.is_valid():
            form.save()
            return redirect("car_status_list")

        return render(
            request,
            self.template_name,
            dict(form=form),
        )


class CarStatusDeleteView(LoginRequiredMixin, PermissionRequiredMixin, CarStatusView):
    permission_required = "is_staff"

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect("index")

    def post(self, request, id):
        repo = self.repo()
        car_status = repo.get_by_id(id)
        repo.delete(car_status)
        return redirect("car_status_list")

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarForm, CommentForm
from cars.models import Car
from cars.repositories.car_repository import CarRepository
from cars.repositories.comment_repository import CommentRepository
from cars.repositories.user_bought_cars_repository import UserBoughtCarsRepository


class CarView(View):
    model = Car
    repo = CarRepository
    form_class = CarForm


class CarListView(CarView):
    template_name = "car/list.html"

    def get(self, request):
        brand_search = request.GET.get("brand")
        category_search = request.GET.get("category")
        status_search = request.GET.get("status")
        repo = self.repo()

        if category_search is not None and category_search != "":
            cars = repo.filter_by_property_name(
                "category",
                category_search,
            )
        else:
            cars = repo.get_all()

        if brand_search is not None and brand_search != "":
            cars = cars.filter(
                car_model__brand__name__icontains=brand_search,
            )

        if status_search is not None and status_search != "":
            cars = cars.filter(car_status__name=status_search)

        return render(
            request,
            self.template_name,
            dict(cars=cars),
        )


class CarDetailView(CarView):
    template_name = "car/detail.html"

    def get(self, request, id):
        repo = self.repo()
        car = repo.get_or_404(id)
        comrepo = CommentRepository()
        comform = CommentForm(
            initial={
                "user": request.user,
                "car": car,
            }
        )
        comments = comrepo.get_by_car(car=car)

        return render(
            request,
            self.template_name,
            dict(
                car=car,
                comments=comments,
                comment_form=comform,
            ),
        )


class CarCreateView(LoginRequiredMixin, CarView):
    template_name = "car/create.html"

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(
                form=form,
            ),
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.seller = request.user
            obj.save()
            return redirect("car_list")

        return render(
            request,
            self.template_name,
            dict(form=form),
        )


class CarUpdateView(LoginRequiredMixin, CarView):
    template_name = "car/update.html"

    def get(self, request, id):
        repo = self.repo()
        car = repo.get_or_404(id)
        form = self.form_class(instance=car)

        return render(
            request,
            self.template_name,
            dict(
                form=form,
            ),
        )

    def post(self, request, id):
        repo = self.repo()
        car = repo.get_or_404(id)
        form = self.form_class(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect("car_list")

        return render(
            request,
            self.template_name,
            dict(form=form),
        )


class CarDeleteView(LoginRequiredMixin, CarView):
    def post(self, request, id):
        repo = self.repo()
        car = repo.get_by_id(id)
        repo.delete(car)
        return redirect("car_list")


class CarSaleView(LoginRequiredMixin, CarView):
    def post(self, request, id):
        repo = self.repo()
        sale_repo = UserBoughtCarsRepository()

        car = repo.get_by_id(id)
        user = request.user

        repo.set_sold(car)
        sale_repo.make_sale(user, car)

        return redirect(request.META["HTTP_REFERER"])

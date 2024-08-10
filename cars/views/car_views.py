from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarForm
from cars.models import Car
from cars.repositories.car_repository import CarRepository

class CarView(View):
    model = Car
    repo = CarRepository
    form_class = CarForm
    
class CarListView(CarView):
    template_name = "car/list.html"
    
    def get(self, request):
        repo = self.repo()
        cars = repo.get_all()
        
        return render(
            request,
            self.template_name,
            dict(cars=cars)
        )

class CarCreateView(LoginRequiredMixin, CarView):
    template_name = "car/create.html"
    
    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(form=form)
        )
        
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('car_list')
        
        return render(
            request,
            self.template_name,
            dict(form=form)
        )
        
class CarUpdateView(LoginRequiredMixin, CarView):
    template_name = 'car/update.html'
    
    def get(self, request, id):
        repo = self.repo()
        car = repo.get_or_404(id)
        form = self.form_class(instance=car)
        
        return render(
            request,
            self.template_name,
            dict(
                form=form,
            )
        )
        
    def post(self, request, id):
        repo = self.repo()
        car = repo.get_or_404(id)
        form = self.form_class(request.POST, instance=car)
        
        if form.is_valid():
            form.save()
            return redirect('car_list')
        
        return render(
            request,
            self.template_name,
            dict(form=form)
        )
        
class CarDeleteView(LoginRequiredMixin, CarView):
    def post(self, request, id):
        repo = self.repo()
        car = repo.get_by_id(id)
        repo.delete(car)
        return redirect('car_list')
        
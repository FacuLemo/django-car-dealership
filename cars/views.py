from django.shortcuts import (
    render,
    redirect
)
from django.views import View
from cars.forms import BrandForm
from cars.models import Brand
from cars.repositories.brand_repository import BrandRepository

class BrandView(View):
    model = Brand
    repo = BrandRepository
    form_class = BrandForm
    
class BrandListView(BrandView):
    template_name = 'brands/list.html'
    
    def get(self, request):
        repo = self.repo()
        brands = repo.get_all()
        
        return render(
            request,
            self.template_name,
            dict(
                brands=brands
            )
        )
    
class BrandCreateView(BrandView):
    template_name = 'brands/create.html'
    
    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
        
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('brand_list')

        return render(
            request,
            'brands/create.html',
            dict(
                form=form
            )
        )
        
class BrandUpdateView(BrandView):
    template_name = 'brands/create.html'
    
    def get(self, request, id):
        repo = self.repo()
        brand = repo.get_or_404(id)
        form = self.form_class(instance=brand)
                
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
        
    def post(self, request, id):
        repo = self.repo()
        brand = repo.get_or_404(id)
        form = self.form_class(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
        
class BrandDeleteView(BrandView):
    def post(self, request, id):
        repo = self.repo()
        brand = repo.get_by_id(id)
        repo.delete(brand)
        return redirect('brand_list')
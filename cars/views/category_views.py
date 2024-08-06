from django.shortcuts import (
    render,
    redirect
)
from django.views import View
from cars.forms import CategoryForm
from cars.models import Category
from cars.repositories.category_repository import CategoryRepository

class CategoryView(View):
    model = Category
    repo = CategoryRepository
    form_class = CategoryForm
    
class CategoryListView(CategoryView):
    template_name = "categories/list.html"
    
    def get(self, request):
        repo = self.repo()
        categories = repo.get_all()
        
        return render(
            request,
            self.template_name,
            dict(
                categories=categories
            )
        )
        
class CategoryCreateView(CategoryView):
    template_name = "categories/create.html"
    
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
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('category_list')
        
        return render(
            request,
            "categories/create.html",
            dict(
                form=form
            )
        )
        
class CategoryUpdateView(CategoryView):
    template_name = 'categories/create.html'
    
    def get(self, request, id):
        repo = self.repo()
        category = repo.get_or_404(id)
        form = self.form_class(instance=category)
        
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
        
    def post(self, request, id):
        repo = self.repo()
        category = repo.get_or_404(id)
        form = self.form_class(request.POST, instance=category)
        
        if form.is_valid():
            form.save()
            return redirect('category_list')
        
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )
        
class CategoryDeleteView(CategoryView):
    def post(self, request, id):
        repo = self.repo()
        category = repo.get_by_id(id)
        repo.delete(category)
        return redirect('category_list')
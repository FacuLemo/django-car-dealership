from django.shortcuts import (
    render,
    redirect
)
from django.views import View
from cars.forms import BrandForm

class BrandView(View):
    form_class = BrandForm
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
            return redirect('brand_create')

        return render(
            request,
            'brands/create.html',
            dict(
                form=form
            )
        )
            
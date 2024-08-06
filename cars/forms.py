from django import forms
from cars.models import (
    Brand,
    CarModel,
    Car,
    Category
)
from utils.check_exists import check_exists
        
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            "name",
            "image"
        ]
        widgets = {
            "name": forms.TextInput(),
            "image": forms.FileInput()
        }
        
    def clean_name(self):
        name = check_exists(self, 'name')
        return name
    
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     name_exists = Brand.objects.filter(name=name).exists()
    #     if name_exists:
    #         raise ValidationError('Esta marca ya está registrada')
    #     return name
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = [
            "name",
            "year",
            "brand"
        ]
        widgets = {
            "name": forms.TextInput(),
            "year": forms.DateInput(),
            "brand": forms.Select(attrs={'readonly': 'readonly'})
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name"
        ]
        widgets = {
            "name": forms.TextInput()
        }
        
        
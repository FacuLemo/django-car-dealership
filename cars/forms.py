from django import forms
from cars.models import (
    Brand,
    CarModel,
    Car,
)
from django.core.exceptions import ValidationError

def check_exists(form, propertyName):
    property = form.cleaned_data.get(propertyName)
    instance = type(form.save(commit=False))
    kwargs = {
        '{0}'.format(propertyName): property
    }
    property_exists = instance.objects.filter(**kwargs).exists()
    print(property_exists)
    if property_exists:
        raise ValidationError(f"{property} ya existe")
    return property
            
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
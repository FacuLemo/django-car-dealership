from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from utils.check_exists import check_exists
from users.models import CosmeticRole

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(
    #     required = True,
    #     help_text = "Email Requerido"
    # )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',

        ]
        
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'first_name': forms.TextInput(
                attrs={'required': 'required'}
            ),
            'last_name': forms.TextInput
        }
    
    def clean_email(self):
        email = check_exists(self, 'email')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.password = self.cleaned_data.get('password1')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user
    
class CosmeticRoleForm(forms.ModelForm):
    class Meta:
        model = CosmeticRole
        fields = [
            'name',
            'color',
        ]
        
        widgets = {
            'name': forms.TextInput(),
            'color': forms.TextInput()
        }
        
    def clean_name(self):
        name = check_exists(self, 'name')
        return name
    
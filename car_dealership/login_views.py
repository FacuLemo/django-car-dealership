from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import (
    redirect,
    render,
)
from django.views import View

from users.forms import UserRegisterForm
from users.models import Profile

class LoginView(View):
    def get(self, request):
        return render(
            request,
            "login/login.html",
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user:
                login(request, user)
                return redirect("index")

        return redirect("login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = "login/register.html"

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
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, lang='es')
            login(request, user)
            return redirect("index")

        return render(
            request,
            self.template_name,
            dict(
                form=form,
            ),
        )

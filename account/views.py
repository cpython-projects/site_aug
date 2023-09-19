import urllib

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserLoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def logout_user(request):
    logout(request)
    return redirect('cafe:home')


# Create your views here.
class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get_success_url(self):

        url = self.request.GET.get('next') or self.request.POST.get('next') or '/'

        return url
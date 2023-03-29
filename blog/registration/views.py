from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse


# Create your views here.
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'


    def get_success_url(self) -> str:
        return reverse('main:blogger-detail', args=[str(self.request.user.id)])

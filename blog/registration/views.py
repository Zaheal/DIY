from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic


# Create your views here.
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'


    def get_success_url(self) -> str:
        return reverse('main:blogger-detail', args=[str(self.request.user.id)])


class RegisterUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registrate.html'
    success_url = reverse_lazy('registration:login')

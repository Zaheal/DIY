from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'registration'

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("registration/", views.RegisterUser.as_view(), name='registrate'),
]

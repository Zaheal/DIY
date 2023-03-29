from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include('main.urls')),
    path("account/", include('registration.urls')),
] 
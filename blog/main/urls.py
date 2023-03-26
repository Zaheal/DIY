from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path("", views.index, name='index'),
    path("blogs/", views, name='blogs'),
    path("bloggers/", views, name='bloggers'),
    path("blogger/<int:pk>/", views, name='bloger-detail'),
    path("<int:pk>/", views, name="blog-detail"),
    path("<int:pk>/create/", views, "comment-create")
]
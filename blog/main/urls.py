from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path("", views.index, name='index'),
    path("blogs/", views.BlogsListView.as_view(), name='blogs'),
    path("bloggers/", views.BloggerListView.as_view(), name='bloggers'),
    path("blogger/<int:pk>/", views.BloggerDetailView.as_view(), name='blogger-detail'),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog-detail"),
    # path("<int:pk>/create/", views, "comment-create")
]
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic

from .models import Blog, Comment

# Create your views here.
def index(request):
    """
    Функция отображения домашней страницы сайта.
    """

    num_blogs = Blog.objects.count()
    num_comments = Comment.objects.count()
    num_bloggers = User.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'num_blogs': num_blogs, 'num_bloggers': num_bloggers, 'num_comments': num_comments, 'num_visits': num_visits}

    return render(
        request,
        'index.html',
        context=context
    )


class BlogsListView(generic.ListView):
    model = Blog
    template_name = 'main/blog_list.html'
    paginate_by = 5


class BloggerListView(generic.ListView):
    model = User
    template_name = 'main/blogger_list.html'
    paginate_by = 5


    
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog_detail.html"


class BloggerDetailView(generic.DetailView):
    model = User
    template_name = "main/blogger_detail.html"
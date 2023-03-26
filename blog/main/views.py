from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic

from .models import Blog, Comments

# Create your views here.
def index(request):
    """
    Функция отображения домашней страницы сайта.
    """

    num_blogs = Blog.objects.count()
    num_comments = Comments.objects.count()
    num_bloggers = User.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'num_blogs': num_blogs, 'num_bloggers': num_bloggers, 'num_comments': num_comments, 'num_visits': num_visits}

    return render(
        request,
        'index.html',
        context=context
    )

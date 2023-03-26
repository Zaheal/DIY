from django.db import models
from django.urls import reverse
from django.utils import timezone

import datetime


class Comments(models.Model):
    """
    Модель, хранящая в себе комментарии, сделанные некоторыми авторами к блогам.
    """

    date_of_creation = models.DateField(default=timezone.now)
    content = models.CharField(max_length=200)
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    author = models.ForeignKey("Blogger", on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f'{self.author}, {self.blog.title}'
    

class Blog(models.Model):
    """
    Модель для блога.
    """

    date_of_creation = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100, help_text="Title for your blog.")
    text = models.TextField(help_text="Enter your main text here.")
    author = models.ForeignKey("Blogger", on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['date_of_creation']


    def __str__(self) -> str:
        return self.title
    

    def get_absolute_url(self):
        return reverse("main:blog-detail", args=[str(self.id)])
    

class Blogger(models.Model):
    """
    Модель для хранения данных автора.
    """

    nick = models.CharField(max_length=15, help_text="Enter your nickname here")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_creation = models.DateField(default=timezone.now)


    def __str__(self) -> str:
        return self.nick
    

    def get_absolute_url(self):
        return reverse("main:blogger-detail", args=[str(self.id)])
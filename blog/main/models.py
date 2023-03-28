from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Comment(models.Model):
    """
    Модель, хранящая в себе комментарии, сделанные некоторыми авторами к блогам.
    """

    date_of_creation = models.DateField(default=timezone.now)
    content = models.CharField(max_length=200)
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['-date_of_creation']


    def __str__(self) -> str:
        return f'{self.author}: {self.blog.title}'
    

class Blog(models.Model):
    """
    Модель для блога.
    """

    date_of_creation = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100, help_text="Title for your blog.")
    text = models.TextField(help_text="Enter your main text here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['-date_of_creation']


    def __str__(self) -> str:
        return f'{self.title}, ({str(self.author)})'
    

    def get_absolute_url(self):
        return reverse("main:blog-detail", args=[str(self.id)])
    


from django.test import TestCase
from django.contrib.auth.models import User

from main.models import Blog, Comment

import datetime


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username='Some', password='12345')
    
    
    def test_str_method_blog(self):
        test_user = User.objects.get(username='Some')
        blog = Blog.objects.create(title='some', text='some', author=test_user)
        self.assertEqual(str(blog), f'{blog.title}, ({str(blog.author)})')
    

    def test_meta_ordering(self):
        test_user = User.objects.get(id=1)
        Blog.objects.create(title='some', text='some', author=test_user)
        Blog.objects.create(title='bome', text='bome', author=test_user, date_of_creation=datetime.datetime(2023, 3, 28, 18, 18, 18, 331178, datetime.timezone.utc))
        blog1 = Blog.objects.get(id=2)
        self.assertEqual(Blog.objects.all()[0].date_of_creation, blog1.date_of_creation)


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username="Some", password='12345')
        blog = Blog.objects.create(title='some', text='some', author=user)
        Comment.objects.create(content='some', blog=blog, author=user)

    
    def test_str_method(self):
        com = Comment.objects.get(id=1)
        self.assertEqual(str(com), f'{com.author}: {com.blog.title}')


    def test_meta_ordering(self):
        user = User.objects.get(id=1)
        blog = Blog.objects.get(id=1)
        Comment.objects.create(content='url', blog=blog, author=user, date_of_creation=datetime.datetime(2023, 3, 28, 18, 18, 18, 331178, datetime.timezone.utc))
        com = Comment.objects.get(id=2)
        self.assertEqual(Comment.objects.all()[0].date_of_creation, com.date_of_creation)







from django.test import TestCase
from django.contrib.auth.models import User

from main.models import Blog, Comments


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(username='Some', password='12345')
    
    
    def test_str_method_blog(self):
        test_user = User.objects.get(username='Some')
        blog = Blog.objects.create(title='some', text='I like you', author=test_user)
        self.assertEqual(str(blog), f'{blog.title}, ({str(blog.author)})')
    

     












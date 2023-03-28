from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from main.models import Blog, Comment

class BlogsListPageTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        u = User.objects.create_user(username='Some', password='12345')    
        Blog.objects.create(title='Title book', text='Text book', author=u)


    def setUp(self) -> None:
        self.client = Client()


    def test_pages_uses_correct_template(self):

        templates_pages_name = {
            'index.html': reverse('main:index'),
            'main/blog_list.html': reverse('main:blogs'),
            'main/blog_detail.html': reverse('main:blog-detail', args=[1]),
        }
        
        for template, reverse_name in templates_pages_name.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.client.get(reverse_name)
                self.assertTemplateUsed(response, template)
    
    

class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username='Some', password='12345')
        
        for num in range(7):
            #Добавить сюда же comments
            Blog.objects.create(title=f'title{num}', text=f'text{num}', author=user)


    def setUp(self) -> None:
        self.client = Client()

    
    def test_first_page_contains_five_records(self):
        response = self.client.get(reverse("main:blogs"))
        self.assertEqual(len(response.context['blog_list']), 5)

    
    def test_second_page_contains_two_records(self):
        response = self.client.get(reverse('main:blogs') + "?page=2")
        self.assertEqual(len(response.context['blog_list']), 2)


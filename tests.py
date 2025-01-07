from rest_framework.test import APITestCase,APIRequestFactory
from .views import PostListCreateView
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class HelloWorldTestCase(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse('posts_home'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello World")
        
class PostListCreateTestCase(APITestCase):
    def setUp(self):
        self.factory=APIRequestFactory()
        self.view=PostListCreateView.as_view()
        self.url=reverse("list_posts")
        self.user=User.objects.create(
            username="segun",
            email="segun@app.com",
            password="password123"
        )
    def test_list_posts(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_post_creation(self):
        sample_post={
            "title":"sample post",
            "content":"sample content"
        }
        request=self.factory.post(self.url, sample_post)
        request.user = self.user
        response= self.view(request)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
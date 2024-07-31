import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from src.book.models import Book, Author
from src.book.serializers import CreateBookSerializer


@pytest.fixture
def test_data():
    """Поднимает временные данные."""
    user = User.objects.create_superuser(username='testuser', password='12345')
    Author.objects.create(first_name='Vadim', last_name='asd', stryear_of_birth=1928, hyear_of_death=2012)
    author = Author.objects.all().first()
    Book.objects.create(name='Test', author=author, pages=1050, published_at=1975, owner=user)


@pytest.mark.django_db
class TestBook(APITestCase):

    def setUp(self):
        self.client.login(username='testuser', password='12345')

    @pytest.mark.usefixtures()
    def test_get_book_list(self):
        """GET запрос к списку книг."""
        url = reverse('book-books')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.usefixtures('test_data')
    def test_post_book_list(self):
        """POST запрос к списку книг."""
        url = reverse('book-books')
        data = CreateBookSerializer(Book.objects.all().first()).data
        response = self.client.post(url, data=data, status='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == data

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')


        self.book1 = Book.objects.create(title="Harry Potter 1", author="J.K. Rowling", publication_year=1997)
        self.book2 = Book.objects.create(title="Game of Thrones", author="George R.R. Martin", publication_year=1996)

        self.book_list_url = reverse('book-list') 

def test_list_books(self):
    response = self.client.get(self.book_list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2) 


def test_create_book(self):
    data = {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937
    }
    response = self.client.post(self.book_list_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)
    self.assertEqual(Book.objects.get(id=response.data['id']).title, "The Hobbit")


def test_update_book(self):
    url = reverse('book-detail', args=[self.book1.id])
    data = {"title": "Harry Potter Updated", "author": "J.K. Rowling", "publication_year": 1997}
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book1.refresh_from_db()
    self.assertEqual(self.book1.title, "Harry Potter Updated")
    
def test_delete_book(self):
    url = reverse('book-detail', args=[self.book2.id])
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 1)


def test_filter_by_author(self):
    response = self.client.get(f"{self.book_list_url}?author=J.K. Rowling")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['author'], "J.K. Rowling")

def test_search_by_title(self):
    response = self.client.get(f"{self.book_list_url}?search=Harry")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertIn("Harry", response.data[0]['title'])


def test_ordering_by_publication_year_desc(self):
    response = self.client.get(f"{self.book_list_url}?ordering=-publication_year")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['publication_year'], 1997)

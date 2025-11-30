from rest_framework import generics, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['title', 'author__name', 'publication_year']

    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year']
    ordering = ['publication_year']

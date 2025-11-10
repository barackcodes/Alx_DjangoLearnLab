from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


from django.views.generic.detail import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
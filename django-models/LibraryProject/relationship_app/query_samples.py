import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from .models import Author, Book, Library, Librarian


author_name = "Barrack"
books = Book.objects.filter(author__name=author_name)
print(books)


library_name = "Free Library"
books_in_library = Library.objects.get(name=library_name).books.all()
print(books_in_library)

librarian = Librarian.objects.get(library__name=library_name)
print(librarian)

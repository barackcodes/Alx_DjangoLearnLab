import os
import sys
import django

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

settings_module = None
for entry in os.listdir(project_root):
    candidate = os.path.join(project_root, entry)
    if os.path.isdir(candidate) and os.path.exists(os.path.join(candidate, 'settings.py')):
        settings_module = f"{entry}.settings"
        break

if settings_module is None:
    print("ERROR: Could not find a Django settings.py in any subfolder of the project root.")
    print("Make sure you run this from the 'django-models' project root and that a settings.py exists.")
    sys.exit(1)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
django.setup()

from .models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist

print("\n1) Query all books by a specific author")
author_name = "Barrack" 
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    if books_by_author.exists():
        print(f"Books by '{author_name}':")
        for b in books_by_author:
            print(" -", b.title)
    else:
        print(f"No books found for author '{author_name}'.")
except Author.DoesNotExist:
    print(f"Author '{author_name}' does not exist in the database.")


print("\n2) List all books in a library")
library_name = "Free Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    if library_books.exists():
        print(f"Books in library '{library_name}':")
        for b in library_books:
            print(" -", b.title)
    else:
        print(f"No books currently associated with library '{library_name}'.")
except Library.DoesNotExist:
    print(f"Library '{library_name}' does not exist in the database.")

print("\n3) Retrieve the librarian for a library")
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian for '{library_name}': {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian is assigned to library '{library_name}'.")
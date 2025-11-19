from .models import Author, Book, Library, Librarian

author_name = "Author Name"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

library_name = "Library Name"
library = Library.objects.get(name=library_name)
library_books = library.books.all()

library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)

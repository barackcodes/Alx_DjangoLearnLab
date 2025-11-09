from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

<<<<<<< HEAD

class Book(models.Model):
    title = models.CharField(max_length=100)
=======
class Book(models.Model):
    title = models.CharField(max_length=200)
>>>>>>> 79f5061 (Add relationship_app with advanced model relationships)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

<<<<<<< HEAD

class Library(models.Model):
    name = models.CharField(max_length=100)
=======
class Library(models.Model):
    name = models.CharField(max_length=150)
>>>>>>> 79f5061 (Add relationship_app with advanced model relationships)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

<<<<<<< HEAD

=======
>>>>>>> 79f5061 (Add relationship_app with advanced model relationships)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
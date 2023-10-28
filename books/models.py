from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=260)
    subtitle = models.CharField(max_length=260)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.title}'
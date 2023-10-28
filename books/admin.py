from django.contrib import admin
from . import models as books_models

# Register your models here.

admin.site.register(books_models.Book)
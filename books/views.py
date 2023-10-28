from django.shortcuts import render
from . import models as books_models

from django.views.generic import ListView

# Create your views here.

class BookListView(ListView):
    model = books_models.Book
    template_name = 'book_list.html'

from django.shortcuts import render

from rest_framework import generics
from books import models as books_models
from . import serializer as api_serializers

# Create your views here.

class BookApiList(generics.ListAPIView):
    queryset = books_models.Book.objects.all()
    serializer_class = api_serializers.BookSerializer
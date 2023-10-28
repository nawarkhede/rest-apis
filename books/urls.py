from django.urls import path
from . import views as books_views

urlpatterns = [
    path('', books_views.BookListView.as_view(), name='book_list'),
]

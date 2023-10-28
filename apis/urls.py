from django.urls import path
from . import views as apis_views

urlpatterns = [
    
    path("", apis_views.BookApiList.as_view(), name='book_list')
]

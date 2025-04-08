from rest_framework import generics 

from books.models import Book
from .serializers import BookSerializer 

class BookAPIView(generics.ListAPIView): # generics.ListAPIView = лише для read-only
    queryset = Book.objects.all()
    serializer_class = BookSerializer
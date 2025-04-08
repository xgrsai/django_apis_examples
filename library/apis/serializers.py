"""процес перетворення складних об’єктів (наприклад, моделей Django) у простий формат, який легко передати (наприклад, JSON)."""
from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")
from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

class BookListView(ListView): # Це створення класу BookListView, який успадковує від вбудованого класу ListView з Django. Клас ListView автоматично генерує список об'єктів з бази даних і відображає їх у вигляді списку на веб-сторінці.
    """в якійсь мірі простіше це написати ніж робити типове view"""
    model = Book #Це вказує, що для цього виду (view) ми будемо використовувати модель Book. Модель Book визначає структуру нашої бази даних для книг, наприклад, назву, автора та інші властивості книги.
    template_name = "book_list.html"
    #context_object_name = 'book_list' # для імені в контекст

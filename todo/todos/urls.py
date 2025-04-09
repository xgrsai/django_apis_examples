# todos/urls.py
from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns = [
path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"), # буде брати з первинним ключем
path("", ListTodo.as_view(), name="todo_list"), # загалом перегляд 
]
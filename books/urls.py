from django.urls import path, include

from .views import BookListView

app_name = "books"
urlpatterns = [
    path("", BookListView.as_view(), name="home"), # Використовуємо метод as_view(), щоб перетворити цей клас у функцію, яку можна викликати для обробки запиту. Django обробляє це автоматично для кожного класу View.
]

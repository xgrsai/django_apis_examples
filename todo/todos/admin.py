from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    """Клас TodoAdmin додається, щоб налаштувати поведінку Django Admin для цієї моделі. Без нього - стандартний вигляд, але з можна точніше контролювати, які поля відображаються і як вони виглядають у списках та інших секціях адмінки."""
    list_display = (
    "title",
    "body",
    )
admin.site.register(Todo, TodoAdmin)

from django.urls import path, include

from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.post_list, name = "post_list"), #перегляд  усіх постів
    path("<int:post_id>/", views.post_one, name = "post_one"), #перегляд одного посту
    #створення одного посту
    #видалення одного посту
    #оновлення одного посту
]

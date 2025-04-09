from django.urls import path, include

from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.post_list, name = "post_list") #перегляд  усіх постів
    #перегляд одного посту
    #створення одного посту
    #видалення одного посту
    #оновлення одного посту
]

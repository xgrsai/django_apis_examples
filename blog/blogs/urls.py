from django.urls import path, include

from . import views

app_name = "blogs"
urlpatterns = [
    path("", include("")) #перенляд блогів усіх
    #перенляд одного блогу
    #створення одного блогу
    #видалення одного блогу
    #оновлення одного блогу
]

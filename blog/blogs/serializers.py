from rest_framework import serializers # необхідний елемент
from django.contrib.auth.models import User

from .models import Post, Image, File # які моделі

class ImageSerializer(serializers.ModelSerializer): # поки без файлу
    class Meta:
        model = Image
        fields = [
           "image",
        ]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "file",
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
        ]                

class PostSerializer(serializers.ModelSerializer): #клас для серіалізатора
    images = ImageSerializer(many=True) # вкладений серіалізатор (щоб назва поля в цьому серіалізаторі співпадала треба доддати до відповідного зовн ключа (моделі Post в цьому випадку) моделі Image - related_name)
    author = UserSerializer() # тут можна так лишити бо в нас є це поле в моделі тому не додаємо related_name
    files = FileSerializer(many=True) # з дужками це створення екземпляру

    class Meta:
        model = Post # посилання на клас
        fields = [
            "title",
            "body",
            "author",
            "created_at",
            "updated_at",
            "images", # відноситься до related_name зовн ключа вкладеної моделі, бо типу ми можемо витягати всі зображення поста через post.images.all()
            "files", 
        ]


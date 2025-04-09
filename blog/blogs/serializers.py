from rest_framework import serializers # необхідний елемент

from .models import Post # які моделі

class PostSerializer(serializers.ModelSerializer): #клас для серіалізатора
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "author",
            "created_at",
            "updated_at",
        ]
        
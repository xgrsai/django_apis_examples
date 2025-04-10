from rest_framework import serializers # необхідний елемент

from .models import Post, Image # які моделі

class ImageSerializer(serializers.ModelSerializer): # поки без файлу
    class Meta:
        model = Image
        fields = [
           "image",
        ]        

class PostSerializer(serializers.ModelSerializer): #клас для серіалізатора
    images = ImageSerializer(many=True) # вкладений серіалізатор
    
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "author",
            "created_at",
            "updated_at",
            "images", # відноситься до related_name зовн ключа вкладеної моделі, бо типу ми можемо витягати всі зображення поста через post.images.all() 
        ]


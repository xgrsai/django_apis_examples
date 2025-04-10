from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post, Image
from .serializers import PostSerializer, ImageSerializer

@api_view(['GET']) # щоб розрізняти де яка view
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True) #Без many=True Django REST Framework думає, що серіалізує один обʼєкт, а йому передає QuerySet, тому він не працює так, як очікуєш.
    return Response(serializer.data)

@api_view(['GET'])
def post_one(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post, many = False) #many=False бо це вже об'єкт а не queryset
    return Response(serializer.data)

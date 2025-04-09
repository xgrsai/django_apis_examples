from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

@api_view(['GET']) # щоб розрізняти де яка view
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True) #Без many=True Django REST Framework думає, що серіалізує один обʼєкт, а йому передає QuerySet, тому він не працює так, як очікуєш.
    return Response(serializer.data)


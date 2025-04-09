from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"title: {self.title} created: {self.created_at} updated: {self.created_at}" 

class Image(models.Model):
    image = models.ImageField(upload_to="images/") # воно якби що створить собі папку

class File(models.Model):
    file = models.FileField(upload_to="otherfiles/")   
from django.contrib import admin

from .models import Post, File, Image

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(File)

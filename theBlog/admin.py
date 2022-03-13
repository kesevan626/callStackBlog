from django.contrib import admin
from .models import Categories, Post, Room, Topic, Comment

# Register your models here.

admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Comment)
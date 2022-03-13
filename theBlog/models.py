from distutils.command import upload
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# from django_resized import ResizedImageField

# Create your models here.
class Categories(models.Model):
            name= models.CharField(max_length=200)

            def __str__(self):
                        return self.name
            def get_absolute_url(self):
                return reverse("add-post")
                    

                    
class Room(models.Model): 
            creator= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
            name = models.CharField(max_length=250, null=True , blank=True)
            tag = models.ManyToManyField('Categories')
            description = models.TextField(null=True, blank=True)
            updated = models.DateTimeField(auto_now=True)
            created = models.DateTimeField(auto_now_add=True)

            def __str__(self):
                return self.name 
            def get_absolute_url(self):
                return reverse("home")
            
class Topic(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    participates = models.ManyToManyField(User, related_name='participate')
    def __str__(self):
                        return self.title

                    
class Post(models.Model):
            author = models.ForeignKey(User, on_delete=models.CASCADE)
            category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True, default='none')
            title = models.CharField(max_length=250)
            body = models.TextField()
            postImage = models.ImageField(upload_to='Featured-image/', null=True, blank=True)
            updated = models.DateTimeField(auto_now=True)
            created = models.DateTimeField(auto_now_add=True)

            class Meta:
                  ordering = [ '-updated', '-created']
                  
            def __str__(self): 
                return self.title
            
            def get_absolute_url(self,*args, **kwargs):
                return reverse("home")


                    
            @property
            def get_photo_url(self):
                if self.postImage and hasattr(self.postImage, 'url'):
                            return self.postImage
                else:  
                   return 'images/user.jpg'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Post, on_delete=models.CASCADE, )
    body = models.TextField(null=False,blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    class Meta:
                  ordering = ['-created']
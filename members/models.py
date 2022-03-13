import email
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
          user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
          avatar = models.ImageField(upload_to='profile-image/', null=True, blank=True)
          firstname = models.CharField(max_length=250)
          lastname = models.CharField(max_length=250)
          email = models.EmailField()
          bio = models.TextField()

          def __str__(self):
                    return self.user.username
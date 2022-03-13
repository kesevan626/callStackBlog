
from re import template
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from .models import  Profile
from .forms import UpdateProfileForm
# Create your views here.

class UserRegister(SuccessMessageMixin,generic.CreateView):
            form_class = UserCreationForm
            template_name = 'registration/register.html'
            success_url = '/login/'
            
                   
@login_required(login_url='login')
def UserProfile(request, pk):
          user = User.objects.get(id=pk)
          user_room = user.room_set.all()
          user_post = user.post_set.all()
          context = {"user": user, 'user_room': user_room, 'user_post': user_post}
          return render(request, 'userProfile.html', context)

class Userprofile(generic.CreateView):  
                    model = Profile
                    form_class = UpdateProfileForm                        
                    template_name= 'UpdateProfile.html'

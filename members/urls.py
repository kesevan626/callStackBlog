from django.urls import path
from members.views import UserRegister, Userprofile
from . import views

urlpatterns = [
            path('register/', UserRegister.as_view(), name="register-user"),
            path('profile/<int:pk>/', views.UserProfile, name="user-profile"),
           path('update-profile/', Userprofile.as_view(), name="update-profile")
            ]
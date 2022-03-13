from unicodedata import name
from django.urls import path
from . import views
from .views import AddpostView, UpdatePostView,  deletePostView,  NewCategory, deleteCommentView, deleteTopicView, AddRoomView,deleteRoomView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Home, name='home' ),
    path('add-post/',login_required(AddpostView.as_view(), login_url='login') , name='add-post' ),
    path('add-category/', login_required(NewCategory.as_view(), login_url='login'), name='add-category' ),
    path('article-detail/<int:pk>/',views.ArticleDetail, name='Detail-View' ),
    path('Edit-post/<int:pk>/',login_required( UpdatePostView.as_view() , login_url='login'),  name='Update-post', ),
    path('delete-post/<int:pk>/',login_required( deletePostView.as_view(),  login_url='login'), name='delete-post' ),
    
     path('delete-message/<int:pk>/',login_required( deleteCommentView.as_view(), login_url='login'), name='delete-message' ),
     path('delete-Topic/<int:pk>/', login_required(deleteTopicView.as_view(), login_url='login'), name='delete-topic' ),
    path('delete-Room/<int:pk>/', login_required(deleteRoomView.as_view(), login_url='login'), name='delete-room' ),

    path('Room/<int:pk>/<str:cat>',views.roomPage, name='room-page' ),
    path('add-room/',login_required(AddRoomView.as_view(), login_url='login') , name='add-room' ),
    # path('Room/<str:pk>/',views.roomPage, name='room-page' ),AddRoomView   redirect_field_name='login'),

    path('discuss/<int:pk>/',views.TopicDisccusionPage, name='topic-page' ),
]

from msilib.schema import ListView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import Post,  Categories, Room, Topic, Comment
from .forms import AddpostForm, EditpostForm, AddRoomForm
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def Home(request):
            bob = 'home'
            Categories_list = Categories.objects.all().annotate(post_count=Count('post'))
            post_list = Post.objects.all()
            count_post = Post.objects.all()
            room = Room.objects.all()
            q = request.GET.get('q')
            if request.GET.get('q')  == None:          
                    p = Paginator(post_list, 4)
                    page_num = request.GET.get('page', 1)
                    try:
                        page = p.page(page_num)
                    except EmptyPage:
                            page = p.page(1)
            else :
                     page= Post.objects.all().filter(
                    Q(category__name__icontains=q) |
                     Q(title__icontains=q))
            context = {'Categories_list': Categories_list,'room': room, 'page': page, 'count_post ': count_post, 'bob': bob }
            return render (request, 'home.html', context)
    
   
class NewCategory(CreateView):     
          model = Categories  
          template_name = 'addCategory.html'    
          fields = '__all__'

def ArticleDetail(request,pk):
        Categories_list = Categories.objects.all()
        post = Post.objects.get(id=pk)
        post_message= post.comment_set.all()
        if request.method == 'POST':
                if request.POST.get('body') != "":
                        comment = Comment.objects.create(
                                user = request.user,
                                room = post,
                                body = request.POST.get('body')
                                )
                        return redirect('Detail-View', post.pk)
                else:
                        return redirect('Detail-View', post.pk)
        context = {'post': post,' post_message':  post_message, ' Categories_list':  Categories_list}
        return render (request, 'ArticleDetail.html', context)
    
class AddpostView(CreateView):
            model = Post
            form_class = AddpostForm
            template_name = 'AddpostView.html'

class AddRoomView(CreateView):
            model = Room
            form_class = AddRoomForm
            template_name = 'AddroomForm.html'
            
class UpdatePostView(UpdateView):
            model = Post
            form_class = EditpostForm
            template_name = 'editPost.html'
           

class deletePostView(DeleteView):
            model = Post
            template_name = 'deletePost.html'
            success_url = reverse_lazy('home')

class deleteCommentView(DeleteView):
            model = Comment
            template_name = 'deletePost.html'
            success_url = reverse_lazy('home')

class deleteTopicView(DeleteView):
            model = Topic
            template_name = 'deletePost.html'
            success_url = reverse_lazy('home')
                  
class deleteRoomView(DeleteView):
            model = Room
            template_name = 'deletePost.html'
            success_url = reverse_lazy('home')
            
def roomPage(request, pk, cat):
        room = Room.objects.get(id=pk, name=cat )
        room_topic = room.topic_set.all()
        if request.method == 'POST':
                title = request.POST.get('title').strip()
                if title != "":      
                          title = Topic.objects.create(
                                room = room,
                                title = request.POST.get('title')
                                )
                          messages.success(request, "Topic created Successfully") 
                          title.save()
                          return redirect('room-page', room.pk, room.name)
                else:
                        messages.error(request, "Invalid Topic")                      
        context = {'room_topic': room_topic,'room':  room}
        return render(request, 'room_page.html', context)

def TopicDisccusionPage(request, pk):
        topic = Topic.objects.get(id=pk)
        context = {'topic': topic}
        return render(request, 'TopicDisccusionPage.html', context)
                  
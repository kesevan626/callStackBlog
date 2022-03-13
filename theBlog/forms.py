from multiprocessing.sharedctypes import Value
from .models import Post, Room
from django import forms


class AddpostForm(forms.ModelForm):
            class Meta:
                        model = Post
                        fields = ['title','author', 'category', 'body', 'postImage']

                        widgets = {
                                    'author': forms.Select(attrs={'class': 'form-control '}),
                                    'title': forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'What your post title'}),
                                    'category': forms.Select(attrs={'class': 'form-select'}),
                                    'body': forms.Textarea(attrs={'class': 'form-control'}),
                                    }

class EditpostForm(forms.ModelForm):
            class Meta:
                        model = Post
                        fields = ['title', 'category', 'body', 'postImage']

                        widgets = {
                                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                                    'category': forms.Select(attrs={'class': 'form-control'}),
                                    'body': forms.Textarea(attrs={'class': 'form-control'}),
                                    }

class AddRoomForm(forms.ModelForm):
            class Meta:
                        model = Room
                        fields = ['creator','name', 'description']

                        widgets = {
                                    'creator': forms.Select(attrs={'class': 'form-control '}),
                                    'name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'What your Room name?'}),
                              
                                    'description': forms.Textarea(attrs={'class': 'form-control'}),
                                    }
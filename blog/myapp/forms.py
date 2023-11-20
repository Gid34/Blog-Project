from django import forms 
from django.contrib.auth.forms import UserCreationForm #built in creation form
from django.contrib.auth.models import User 
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"] #WHY IS THIS NTO SHOWING ThE TEXT FIELDS?

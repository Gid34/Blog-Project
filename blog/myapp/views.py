from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import reverse

from .models import *
from .forms import *

# Create your views here.

# class HomeView(ListView):
#     model = Item
#     paginate_by = 10
#     template_name = "home.html"


def home_page_logged_in(request):
    return render(request, "base/home_page_logged_in.html")
    

def home_page(request):
    return render(request, "base/home_page.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'] #from the name = "username" store it in a variable on the left
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used') #Check if email exists, if yes, return message
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used ') 
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, 
                 first_name=first_name, last_name=last_name) #Create user
                user.save();
                return redirect('/')
        else:
            messages.info(request, 'Password is not the same')
            return redirect('register')
    else:
        return render(request, "user_authentication/register.html")

# #BACK UP SIGN IN CODE
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            auth.login(request, user)

            return redirect('/') 

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('/sign-in')
    else:
        return render(request, "user_authentication/sign-in.html")

#CORRECT ALREADY - 11-07-2023
#11-8 login not working/ always finding for registration/login
#Must be when I ran website project
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/') #CORRECT DONT CHANGE

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('/login') #CORRECT DONT CHANGE

    else:
        return render(request, "user_authentication/login.html")

def log_out(request): 
    auth.logout(request)
    return redirect('/')


#Testing with default variable name [DO NOT DELETE]
# def logout(request): 
#     auth.logout(request)
#     return redirect('/')
    #For some reason always returns the Django Admin Page
    #Use log_out for now


def display_feedback(request):
    posts = Post.objects.all()
    return render(request,"posts/display_feedback.html", {'posts' : posts})

def individual_feedback(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,"posts/individual_feedback.html", {'individual_posts' : posts})
    #the values in {'individual_posts' : posts} doesn't have to be the same!!!
    #it is {{individual_posts}} THAT MUST BE QUERIED IN THE HTML FILE.
    
# @login_required(login_url = "/login")
# def create_feedback(request):
#     if request.method == 'POST':
#         create_post = CreatePost(request.POST)
#         if create_post.is_valid():
#             create_post = create_post.save(commit=False) #post is just a variable name
#             create_post.author_id =  request.user #access the user currently signed in
#             create_post.save()
#             return redirect('/feedback')
#     else:
#         create_post = CreatePost()
#     return render(request, "posts/create_feedback.html",  {"create_post" : create_post} )

@login_required(login_url = "/login")
def create_feedback(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            create_post = form.save(commit=False) #post is just a variable name
            create_post.author_id =  request.user #This is needed if you add the models.ForeignKey(User, on_delete = models.CASCADE) in models
            #essentially it takes the current logged in user and stores it as author_id
            create_post.save()
            return redirect('/feedback')
    else:
        form = PostForm()
    return render(request, "posts/create_feedback.html",  {"form" : form} )

def check_delete(request):
    # posts = Post.objects.all()
    # posts = Post.objects.all().values()[1]
    # posts = Post.objects.values_list('author_id','id','title')
    # return render(request, "base/check_delete.html",  {"posts" : posts} )
    return render(request, "base/check_delete.html")

def delete(request, pk):
    post_id = Post.objects.get(id=pk)
    print(post_id)
    post_id.delete()

    return redirect('/feedback')
#Simple Delete Function, Since we have implemented  {% if user == post.author_id %} in html file,
#it should work that only author can delete posts for now.

#This Code is Complete
class DestinationDetailView(DetailView):
    model = Destination
    template_name = "base/destination_catalogue.html"
    #The Problem was the path. Need to find fix for it to be uniform later

#This Code is NOT THE FIX
# def destinations(request):
#     context = {
#         'destinations': Destination.objects.all()
#     }
#     return render(request, "destination_catalogue.html", context)

#Test for destinations
# def test_destinations(request):
#     return render(request, "base/destination_catalogue.html")



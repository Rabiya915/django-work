from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def forms(request):
    if request.method == 'POST':
       data = request.POST
       title = data.get('title')
       author = data.get('author')
       published_date = data.get('published_date')

       print(title)
       print(author)
       print(published_date)

       Book.objects.create(title = title,
                           author = author,
                           published_date = published_date)
                                
       return redirect('/forms.html/')

    return render(request, 'forms.html/')

def submit(request):
    return render(request,'submit.html')

def books(request):
    return render(request, 'book.html')

def book_detail_1(request):
    return render(request, 'book_detail_1.html')

def book_detail_2(request):
    return render(request, 'book_detail_2.html')

def book_detail_3(request):
    return render(request, 'book_detail_3.html')


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('forms.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
    
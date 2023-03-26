from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm

def login_view(request):
    """
    Display login form to manage note data.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('note_list')
        else:
            messages.error(request, 'Invalid username or password.')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    """
    Display singup form to register user.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def custom_logout(request):
    """
    Logout from the system and redirect to login form..
    """
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    games = Game.objects.all()
    context = {'games' : games}
    return render(request, 'game/home.html', context)


def signUp(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserRegistrationForm()
	context = {'form' : form}
	return render (request, "game/signUp.html", context)


def signIn(request):
    if request.method == "POST":
	    form = UserLoginForm(request, request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    messages.info(request, f"You are now logged in as {username}.")
			    return redirect("home")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = UserLoginForm()
    context= {'form' : form}
    return render(request, "game/signin.html", context)


def signOut(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


@login_required(login_url='login')
def pongGame(request):
    return render(request, 'game/pongGame.html')

@login_required(login_url='login')
def snakeGame(request):
    return render(request, 'game/snakeGame.html')

@login_required(login_url='login')
def tictactoeGame(request):
    return render(request, 'game/tictactoeGame.html')

@login_required(login_url='login')
def wordScrambleGame(request):
    return render(request, 'game/wordScrambleGame.html')

def main(request):
    return render(request, 'game/main.html')
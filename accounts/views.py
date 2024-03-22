from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.template.defaulttags import csrf_token


def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@csrf_exempt
def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def Logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')




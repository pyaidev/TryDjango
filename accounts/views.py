from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def _login_view(request):
    query_dict = request.POST
    username = query_dict.get('username')
    password = query_dict.get('password')
    if request.method == 'POST':
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "bunday foydalanuvchi mavjud emas"}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/login.html')


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)



@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'accounts/logout.html')


def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from .forms import UserRegistrationForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request, 'accounts_temps/login.html',{})

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            username= form.cleaned_data.get('username')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            return redirect('login')
        return redirect('signup')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts_temps/register.html',{'form':form})
def logout_view(request):
    logout(request)
    return redirect('home')
def password_reset_view(request):
    pass
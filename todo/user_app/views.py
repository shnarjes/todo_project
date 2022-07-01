
# Create your views here.

from django.contrib.auth import authenticate, logout as _logout, login as _login,get_user_model
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from todo import settings
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.core.cache import caches


from .forms import RegisterForm ,LoginForm






User = get_user_model()

@require_http_methods(["GET", "POST"])
def login(request):
    login_form = LoginForm(request.POST or None)
    if request.method == "GET":
        next = request.GET.get("next", "")
        if next:
            return render(request, 'login.html', {'login_form': login_form,'next':next})
        else:
            return render(request, 'login.html', {'login_form': login_form,})

    else:
        login_form = LoginForm(request.POST or None)
        print(request.POST)
        print('im mast')
        if login_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(request, email=email, password=password)
            if user is not None: 
                _login(request , user) 
                return redirect('todoapp:projectlist')
            else:
                return render(request, 'login.html', {'login_form': login_form, 'errors':'This user does not exists.'})
        else:
            return render(request, 'login.html', {'login_form': login_form,'errors':'The information is wrong'})


def logout(request):
    _logout(request)
    return redirect('home')

@require_http_methods(["GET", "POST"])
def register(request):
    register_form = RegisterForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'register.html', {'register_form': register_form})
    elif request.method == "POST":
        if register_form.is_valid():
            user=register_form.save(commit=True)
            return redirect('user_app:login')
        else:
            return render(request, 'register.html', {'register_form': register_form, 'errors':register_form.errors})





        

from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin

from .models import Professor

# Create your views here.

def registerView(request):
    if request.method == 'POST':

        # user registration process
        professor = {
            'name': request.POST['name'],
            'cpf': request.POST['cpf'],
            'phone_number': request.POST['phone_number'],
            'especiality': request.POST['especiality'],
            'email': request.POST['email'],
            'address': request.PORT['address'],
            'birth_date': request.POST['birth_date'],
            'username': request.POST['username'],
            'password': request.POST['password'],
        }
        if request.POST['password'] == request.POST['repassword']:
            if User.objects.filter(username=professor['username']).exists() or User.objects.filter(email=professor['email']).exists():
                messages.warning(request, 'Username or email is already taken.')
                return redirect('professor:register')
            else:
                # registration
                password = professor.pop('password')
                username = professor.pop('username')
                user = User.objects.create_user(username=username, password=password)
                user.save()
                professor['user'] = user
                professor = Professor(**professor)
                professor.save()
                messages.success(request, 'Registration created! You can login to your account.')
                return redirect('professor:login')
        else:
            messages.warning(request, 'Passwords do not match.')
            return redirect('professor:register')
    else:
        return render(request, 'register-professor.html')
    
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome, ' + username)
            return redirect('professor:campus')
        else:
            messages.error(request, 'Check your information and try again!')
            return redirect('professor:login')
    else:
        return render(request, 'login.html')
    
def professorView(request):
    return render(request,'professor_perfil.html')

def logoutView(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('professor:login')
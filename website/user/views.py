from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
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

from .models import UserStudent
from professor.models import Professor

# Create your views here.

def registerView(request):
    if request.method == 'POST':

        # user registration process
        student = {
            'name': request.POST['name'],
            'cpf': request.POST['cpf'],
            'gender': request.POST['gender'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'birth_date': request.POST['birth_date'],
            'username': request.POST['username'],
            'password': request.POST['password'],
        }
        if request.POST['password'] == request.POST['repassword']:
            if User.objects.filter(username=student['username']).exists() or User.objects.filter(email=student['email']).exists():
                messages.warning(request, 'Username or email is already taken.')
                return redirect('user:register')
            else:
                # registration
                password = student.pop('password')
                username = student.pop('username')
                user = User.objects.create_user(username=username, password=password)
                user.save()
                student['user'] = user
                student = UserStudent(**student)
                student.save()
                messages.success(request, 'Registration created! You can login to your account.')
                return redirect('user:login')
        else:
            messages.warning(request, 'Passwords do not match.')
            return redirect('user:register')
    else:
        return render(request, 'register-aluno.html')
    
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome, ' + username)
            user = User.objects.get(username=username)
            print(user)
            user_st = UserStudent.objects.filter(user=user)
            if(len(user_st) < 1):
                return redirect(f"professor:campus", user.id)
            else:
                info = {'user': user_st[0]}
                return render(request, "pagina-aluno.html",info)
        else:
            messages.error(request, 'Check your information and try again!')
            return redirect('user:login')
    else:
        return render(request, 'login.html')
    
def studentView(request, id):
    user = UserStudent.objects.get(user_id=id)
    info = {'user': user}
    return render(request, "pagina-aluno.html",info)

def calendarView(request, id):
    user = UserStudent.objects.get(user_id=id)
    info = {'user': user}
    return render(request, "calendario-aluno.html",info)

def listaOficinasView(request, id):
    user = UserStudent.objects.get(user_id=id)
    info = {'user': user}
    return render(request, "calendario-aluno.html",info)

def listaOficinasView(request, id):
    user = UserStudent.objects.get(user_id=id)
    info = {'user': user}
    return render(request, "tela_listar_oficina.html", info)

def logoutView(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('user:login')
from django.shortcuts import render
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
from .models import Workshops

# Create your views here.

def createOficinaForm(request):
    if request.method == 'POST':

        # user registration process
        oficina = {
            'name': request.POST['name'],
            'hour': request.POST['hour'],
            'room': request.POST['room'],
            'desc': request.POST['desc'],
        }
        oficina = Workshops(**oficina)
        oficina.save()
        messages.success(request, 'Oficina registrada com sucesso.')
        return redirect('professor:campus')
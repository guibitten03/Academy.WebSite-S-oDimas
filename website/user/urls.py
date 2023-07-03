from django.urls import path

from . import views
from .models import UserStudent

app_name = 'user'
urlpatterns = [
    path('register-aluno/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('<int:id>/campus/', views.studentView, name='campus'),
    path('logout/', views.logoutView, name='logout'),
    path('<int:id>/calendario/', views.calendarView, name='calendar'),
    path('<int:id>/minhas-oficinas/', views.listaOficinasView, name='lista-oficina'),
]
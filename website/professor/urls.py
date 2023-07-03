from django.urls import path

from . import views
from user.views import loginView

app_name = 'professor'
urlpatterns = [
    path('register-professor/', views.registerView, name='register'),
    path('login/', loginView, name='login'),
    path('<int:pk>/campus/', views.professorView, name='campus'),
    path('<int:pk>/calendario/', views.calendarView, name='calendar'),
    path('<int:pk>/criar-oficinas/', views.criarOficinasView, name='criar-oficinas'),
    path('logout/', views.logoutView, name='logout'),
]
from django.urls import path

from . import views

app_name = 'professor'
urlpatterns = [
    path('register-professor/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('campus/', views.professorView, name='campus'),
    path('logout/', views.logoutView, name='logout'),
]
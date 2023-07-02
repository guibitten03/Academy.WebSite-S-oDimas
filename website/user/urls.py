from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('register-aluno/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('campus/', views.studentView, name='campus'),
    path('logout/', views.logoutView, name='logout'),
]
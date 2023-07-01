from django.urls import path
from . import views


urlpatterns = [
    path('register-admin/', views.registerAdminView),
    path('register-professor/', views.registerProfessorView),
    path('register-aluno/', views.registerAlunoView),
    path('login/', views.loginView),
]

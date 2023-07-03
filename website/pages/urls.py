from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('register-admin/', views.registerAdminView, name='adm-sign'),
    path('register-professor/', views.registerProfessorView, name='professor-sign'),
    path('register-aluno/', views.registerAlunoView, name='student-sign'),
    path('login/', views.loginView, name='login'),
    path('gallery/', views.galleryView, name="gallery")
]

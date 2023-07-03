from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request, 'home.html')

def registerAdminView(request):
    return render(request,'register-admin.html')

def registerProfessorView(request):
    return render(request,'register-professor.html')

def registerAlunoView(request):
    return render(request,'register-aluno.html')

def loginView(request):
    return render(request,'login.html')

def galleryView(request):
    return render(request, 'galeria.html')
from django.shortcuts import render

# Create your views here.

def registerAdminView(request):
    return render(request,'register-admin.html')

def registerProfessorView(request):
    return render(request,'register-professor.html')

def registerAlunoView(request):
    return render(request,'register-aluno.html')

def loginView(request):
    return render(request,'login.html')
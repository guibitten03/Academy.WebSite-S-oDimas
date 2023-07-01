from django.shortcuts import render

# Create your views here.

def registerAdminView(request):
    return render(request,'register-admin.html')

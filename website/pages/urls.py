from django.urls import path
from . import views


urlpatterns = [
    path('register-admin/', views.registerAdminView),
]

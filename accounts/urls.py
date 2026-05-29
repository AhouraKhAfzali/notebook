from django.urls import path
from . import views

urlpatterns = [
    path('register/student/', views.register_student, name='register_student'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),
]

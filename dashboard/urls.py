from django.urls import path, include

urlpatterns = [
    path('student/', include('dashboard.student.urls')),
    path('teacher/', include('dashboard.teacher.urls')),
]

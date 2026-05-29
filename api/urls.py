from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from . import views

urlpatterns = [
    # JWT APIs
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # auto complete APIs
    path('auto-complete/university/', views.autocomplete_institution, name='auto-complete-institution'),
    path('auto-complete/major/', views.autocomplete_major, name='auto-complete-major'),
    path('auto-complete/teacher/', views.autocomplete_teacher, name='auto-complete-teacher'),
    # # apps APIs
    # path('learning/', include('domains.learning.urls')),
    # path('contents/', include('domains.contents.urls')),
    # path('work/', include('domains.work.urls')),
]

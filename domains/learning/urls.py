"""
# apps/your_app/urls.py
from django.urls import path
from .views import (
    ClassCreate,
    ClassList,
    ClassDetail,
    ClassUpdate,
    ClassDelete,
    ClassFilter,

    EnrollmentCreate,
    EnrollmentList,
    EnrollmentDetail,
    EnrollmentUpdate,
    EnrollmentDelete,
    EnrollmentFilter,
)

urlpatterns = [
    # Class urls
    path("classes/", ClassList.as_view(), name="class-list"),
    path("classes/filter/", ClassFilter.as_view(), name="class-filter"),
    path("classes/create/", ClassCreate.as_view(), name="class-create"),
    path("classes/<int:pk>/", ClassDetail.as_view(), name="class-detail"),
    path("classes/<int:pk>/update/", ClassUpdate.as_view(), name="class-update"),
    path("classes/<int:pk>/delete/", ClassDelete.as_view(), name="class-delete"),
    # Enrollment urls
    path("enrollment/", EnrollmentList.as_view(), name="enrollment-list"),
    path("enrollment/filter/", EnrollmentFilter.as_view(), name="enrollment-filter"),
    path("enrollment/create/", EnrollmentCreate.as_view(), name="enrollment-create"),
    path("enrollment/<int:pk>/", EnrollmentDetail.as_view(), name="enrollment-detail"),
    path("enrollment/<int:pk>/update/", EnrollmentUpdate.as_view(), name="enrollment-update"),
    path("enrollment/<int:pk>/delete/", EnrollmentDelete.as_view(), name="enrollment-delete"),
]
"""
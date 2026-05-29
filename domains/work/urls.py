"""
from django.urls import path
from .views import (
    AssignmentCreate,
    AssignmentList,
    AssignmentDetail,
    AssignmentUpdate,
    AssignmentDelete,
    AssignmentFilter,

    SubmissionCreate,
    SubmissionList,
    SubmissionDetail,
    SubmissionUpdate,
    SubmissionDelete,
    SubmissionFilter,
)

urlpatterns = [
    # Class urls
    path("assignment/", AssignmentList.as_view(), name="assignment-list"),
    path("assignment/filter/", AssignmentFilter.as_view(), name="assignment-filter"),
    path("assignment/create/", AssignmentCreate.as_view(), name="assignment-create"),
    path("assignment/<int:pk>/", AssignmentDetail.as_view(), name="assignment-detail"),
    path("assignment/<int:pk>/update/", AssignmentUpdate.as_view(), name="assignment-update"),
    path("assignment/<int:pk>/delete/", AssignmentDelete.as_view(), name="assignment-delete"),
    # Submission urls
    path("submission/", SubmissionList.as_view(), name="submission-list"),
    path("submission/filter/", SubmissionFilter.as_view(), name="submission-filter"),
    path("submission/create/", SubmissionCreate.as_view(), name="submission-create"),
    path("submission/<int:pk>/", SubmissionDetail.as_view(), name="submission-detail"),
    path("submission/<int:pk>/update/", SubmissionUpdate.as_view(), name="submission-update"),
    path("submission/<int:pk>/delete/", SubmissionDelete.as_view(), name="submission-delete"),
]
"""
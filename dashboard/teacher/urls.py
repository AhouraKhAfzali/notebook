from django.urls import path
from dashboard.teacher import views

urlpatterns = [

    # base urls
    path(
        'profile/',
        views.profile,
        name='dash-teachers-profile'
    ),

    # courses urls
    path(
        'courses/create/',
        views.courses_create,
        name='dash-teachers-courses-create'
    ),
    path(
        'courses/',
        views.courses_mine,
        name='dash-teachers-courses-mine'
    ),
    path(
        'courses/<int:pk>/show/',
        views.courses_show,
        name='dash-teachers-courses-show'
    ),
    path(
        'courses/<int:pk>/edit/',
        views.courses_edit,
        name='dash-teachers-courses-edit'
    ),
    path(
        'courses/<int:pk>/delete/',
        views.courses_delete,
        name='dash-teachers-courses-delete'
    ),

    # contents urls
    path(
        'contents/create/<int:pk>/',
        views.contents_create,
        name='dash-teachers-contents-create'
    ),
    path(
        'contents/<int:pk>/edit/',
        views.contents_edit,
        name='dash-teachers-contents-edit'
    ),
    path(
        'contents/<int:pk>/delete/',
        views.contents_delete,
        name='dash-teachers-contents-delete'
    ),

    # enrollments urls
    path(
        'enrollment/<int:pk>/accept/',
        views.enrollment_accept,
        name='dash-teachers-enrollment-accept'
    ),
    path(
        'enrollment/<int:pk>/reject/',
        views.enrollment_reject,
        name='dash-teachers-enrollment-reject'
    ),

    # assignments urls
    path(
        'assignments/create/<int:pk>/',
        views.assignments_create,
        name='dash-teachers-assignments-create'
    ),
    path(
        'assignments/<int:pk>/show/',
        views.assignments_show,
        name='dash-teachers-assignments-show'
    ),
    path('assignments/<int:pk>/edit/',
         views.assignments_edit,
         name='dash-teachers-assignments-edit'
    ),
    path('assignments/<int:pk>/delete/',
         views.assignments_delete,
         name='dash-teachers-assignments-delete'
    ),

    # submissions urls
    path(
        'submissions/<int:pk>/grade/',
        views.submissions_grade,
        name='dash-teachers-submissions-grade'
    ),
]

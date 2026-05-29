from django.urls import path
from dashboard.student import views

urlpatterns = [

    # base urls
    path(
        'profile/',
        views.profile,
        name='dash-students-profile'
    ),

    # courses urls
    path(
        'courses/',
        views.courses_mine,
        name='dash-students-courses-mine'
    ),
    path(
        'courses/all/',
        views.courses_all,
        name='dash-students-courses-all'
    ),
    path(
        'courses/<int:pk>',
        views.courses_detail,
        name='dash-students-courses-detail'
    ),
    path(
        'courses/<int:pk>/show/',
        views.courses_show,
        name='dash-students-courses-show'
    ),
    path(
        'courses/<int:pk>/enroll/',
        views.courses_enroll,
        name='dash-students-courses-enroll'
    ),

    # assignments urls
    path(
        'assignments/<int:pk>/',
        views.assignments_show,
        name='dash-students-assignments-show'
    ),

    # submissions urls
    path(
        'submissions/create/<int:pk>/',
        views.submissions_create,
        name='dash-students-submissions-create'
    ),
]

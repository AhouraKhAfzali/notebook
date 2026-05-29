# django imports
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from utils.decorators import handle_service_errors
# form imports
from domains.work.forms import SubmissionForm
# services imports
from domains.learning.services import course_service, enrollment_service
from domains.work.services import assignment_service, submission_service


# ------------------------------ Other views ------------------------------
def profile(request):
    courses = course_service.filter_courses(students=request.user)
    return render(request, template_name="dashboard/student/profile.html", context={"courses": courses})


# ------------------------------ Class views ------------------------------
def courses_all(request):
    query_dict = request.GET.dict()
    objects = course_service.filter_courses(**query_dict)
    return render(request, template_name="dashboard/student/courses_all.html", context={"objects": objects})


def courses_mine(request):
    query_dict = request.GET.dict()
    query_dict["students"] = request.user.id
    objects = course_service.filter_courses(**query_dict)
    return render(request, template_name="dashboard/student/courses_mine.html", context={"objects": objects})

@handle_service_errors()
def courses_detail(request, pk):
    object = course_service.get_courses_by_id(pk)
    return render(request, template_name="dashboard/student/courses_detail.html", context={"object": object})

@handle_service_errors()
def courses_show(request, pk):
    context = {
        "object": course_service.get_courses_by_id(pk),
        "assignments": assignment_service.filter_assignments(course_obj_id=pk),
    }
    return render(request, template_name="dashboard/student/courses_show.html", context=context)

@handle_service_errors()
def courses_enroll(request, pk):
    object = enrollment_service.create_enrollment(student=request.user, course_obj_id=pk)
    messages.success(request, message="Your enrollment request has been sent")
    return redirect(reverse(viewname="dash-students-courses-detail", kwargs={"pk": pk}))


# ------------------------------ Assignment views ------------------------------
@handle_service_errors()
def assignments_show(request, pk):
    content = {
        "assignment": assignment_service.get_assignment_by_id(pk),
        "submissions_graded": submission_service.filter_submissions(assignment_id=pk, student_id=request.user.id, graded=True),
        "submissions_ungraded": submission_service.filter_submissions(assignment_id=pk, student_id=request.user.id, graded=False)
    }
    return render(request, template_name="dashboard/student/assignments_show.html", context=content)


# ------------------------------ Submission views ------------------------------
def submissions_create(request, pk):
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.assignment = assignment_service.get_assignment_by_id(pk)
            instance.student = request.user
            instance.save()
            messages.success(request, message="Your submission has been submitted")
            return redirect(reverse(viewname="dash-students-assignments-show", kwargs={"pk": pk}))
    else:
        form = SubmissionForm()
    return render(request, template_name="dashboard/student/submissions_create.html", context={"form": form, "assignment": pk})

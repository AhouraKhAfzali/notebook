# django imports
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from utils.decorators import handle_service_errors
# form imports
from domains.contents.forms import ContentsForm, ContentsEditForm
from domains.learning.forms import CourseForm, CourseEditForm
from domains.work.forms import AssignmentForm, AssignmentEditForm, SubmissionGradeForm
# services imports
from domains.learning.services import course_service, enrollment_service
from domains.work.services import assignment_service, submission_service
from domains.contents.services import content_service


# ------------------------------ Main views ------------------------------
def profile(request):
    courses = course_service.filter_courses(teacher=request.user)
    return render(request, template_name="dashboard/teacher/profile.html", context={"courses": courses})


# ------------------------------ Course views ------------------------------
def courses_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = request.user
            instance.save()
            messages.success(request, message="New course has been created")
            return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": instance.id}))
    else:
        form = CourseForm()
    return render(request, template_name="dashboard/teacher/courses_create.html", context={"form": form})

def courses_mine(request):
    query_dict = request.GET.dict()
    query_dict["teacher"] = request.user.id
    objects = course_service.filter_courses(**query_dict)
    return render(request, template_name="dashboard/teacher/courses_mine.html", context={"objects": objects})

@handle_service_errors()
def courses_show(request, pk):
    context = {
        "object": course_service.get_courses_by_id(pk),
        "contents": content_service.filter_contents(course_obj_id=pk),
        "assignments": assignment_service.filter_assignments(course_obj_id=pk),
        "enrollments": enrollment_service.filter_enrollments(course_obj_id=pk, status="pending"),
    }
    return render(request, template_name="dashboard/teacher/courses_show.html", context=context)

@handle_service_errors()
def courses_edit(request, pk):
    object = course_service.get_courses_by_id(pk)
    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, message="Course has been edited")
            return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": pk}))
    else:
        form = CourseEditForm(instance=object)
    return render(request, template_name="dashboard/teacher/courses_edit.html", context={"form": form, "pk": pk})

@handle_service_errors()
def courses_delete(request, pk):
    course_service.delete_course(pk)
    messages.success(request, message="Course has been deleted")
    return redirect(reverse("dash-teachers-profile"))


# ------------------------------ Contents views ------------------------------
@handle_service_errors()
def contents_create(request, pk):
    if request.method == "POST":
        form = ContentsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course_obj = course_service.get_courses_by_id(pk)
            instance.created_by = request.user
            instance.save()
            messages.success(request, message="New content has been created")
            return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": pk}))
    else:
        form = ContentsForm()
    return render(request, template_name="dashboard/teacher/contents_create.html", context={"form": form, "pk": pk})

@handle_service_errors()
def contents_edit(request, pk):
    object = content_service.get_content_by_id(pk)
    if request.method == "POST":
        form = ContentsEditForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, message="Content has been edited")
            return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": object.course_obj.id}))
    else:
        form = ContentsEditForm(instance=object)
    return render(request, template_name="dashboard/teacher/contents_edit.html", context={"form": form, "pk": pk})

@handle_service_errors()
def contents_delete(request, pk):
    object = content_service.get_content_by_id(pk)
    content_service.delete_content(pk)
    messages.success(request, message="Content has been deleted")
    return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": object.course_obj_id}))

# ------------------------------ Enrollment views ------------------------------
@handle_service_errors()
def enrollment_accept(request, pk):
    object = enrollment_service.accept_enrollment(pk)
    messages.success(request, message=f"Enrollment request for student {object.student.first_name} {object.student.last_name} has been accepted")
    return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": object.course_obj.id}))

@handle_service_errors()
def enrollment_reject(request, pk):
    object = enrollment_service.reject_enrollment(pk)
    messages.warning(request,message=f"Enrollment request for student {object.student.first_name} {object.student.last_name} has been rejected")
    return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": object.course_obj.id}))


# ------------------------------ Assignment views ------------------------------
@handle_service_errors()
def assignments_create(request, pk):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course_obj = course_service.get_courses_by_id(pk)
            instance.created_by = request.user
            instance.save()
            messages.success(request, message="New assignment has been created")
            return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": pk}))
    else:
        form = AssignmentForm()
    return render(request, template_name="dashboard/teacher/assignments_create.html", context={"form": form, "pk": pk})

@handle_service_errors()
def assignments_show(request, pk):
    content = {
        "assignment": assignment_service.get_assignment_by_id(pk),
        "submissions_graded": submission_service.filter_submissions(assignment_id=pk, graded=True),
        "submissions_ungraded": submission_service.filter_submissions(assignment_id=pk, graded=False),
    }
    return render(request, template_name="dashboard/teacher/assignments_show.html", context=content)

@handle_service_errors()
def assignments_edit(request, pk):
    object = assignment_service.get_assignment_by_id(pk)
    if request.method == "POST":
        form = AssignmentEditForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, message="Assignment has been edited")
            return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": object.course_obj.id}))
    else:
        form = AssignmentEditForm(instance=object)
    return render(request, template_name="dashboard/teacher/assignments_edit.html", context={"form": form, "pk": pk})

@handle_service_errors()
def assignments_delete(request, pk):
    object = assignment_service.get_assignment_by_id(pk)
    assignment_service.delete_assignment(pk)
    messages.success(request, message="Assignment has been deleted")
    return redirect(reverse("dash-teachers-courses-show", kwargs={"pk": object.course_obj_id}))


# ------------------------------ Submission views ------------------------------
@handle_service_errors()
def submissions_grade(request, pk):
    if request.method == "POST":
        form = SubmissionGradeForm(request.POST)
        if form.is_valid():
            data =form.cleaned_data
            object = submission_service.grade_submission(submission_id=pk, grade=data["grade"], feedback=data["feedback"])
            messages.success(request, f"Your grade and feedback for submission of student {object.student.first_name} {object.student.last_name} has been submitted")
            return redirect(reverse("dash-teachers-assignments-show", kwargs={"pk": object.assignment_id}))
    else:
        form = SubmissionGradeForm()
    return render(request, template_name="dashboard/teacher/submissions_grade.html", context={"form": form, "pk": pk})

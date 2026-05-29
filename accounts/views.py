from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, login, logout, update_session_auth_hash
from .forms import StudentUserForm, TeacherUserForm, CustomAuthenticationForm, CustomPasswordChangeForm


# getting user model
User = get_user_model()


# student register view
def register_student(request):
    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                email=data["email"],
                phone_number=data["phone_number"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                password=data["password"],
                role="student"
            )
            login(request, user)
            return redirect(reverse('dash-students-profile'))
    else:
        form = StudentUserForm()
    return render(request, template_name="accounts/register_student.html", context={"form": form})


# teacher register view
def register_teacher(request):
    if request.method == 'POST':
        form = TeacherUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                email=data["email"],
                phone_number=data["phone_number"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                password=data["password"],
                role="teacher"
            )
            login(request, user)
            return redirect(reverse("dash-teachers-profile"))
    else:
        form = TeacherUserForm()
    return render(request, template_name="accounts/register_teacher.html", context={"form": form})


# login view
def log_in(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                if request.user.role == "student":
                    return redirect(reverse("dash-students-profile"))
                else:
                    return redirect(reverse("dash-teachers-profile"))
    else:
        form = CustomAuthenticationForm()
    return render(request, template_name="accounts/login.html", context={"form": form})


# log out view
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    messages.success(request, message="Successfully logged out of your account")
    return redirect(reverse("home"))


# password change view
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, message="Your password was successfully updated")
            if request.user.role == "student":
                return redirect(reverse("dash-students-profile"))
            else:
                return redirect(reverse("dash-teachers-profile"))
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, template_name='accounts/change_password.html', context={'form': form})


# delete account view
def delete_account(request):
    user = request.user
    user.delete()
    logout(request)
    messages.success(request, message="Successfully deleted your account")
    return redirect(reverse("home"))

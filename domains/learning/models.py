from django.db import models
from django.db.models import Q

# Create your models here.
class Course(models.Model):

    # primary information
    name = models.CharField(max_length=100, verbose_name="Course Name")

    # secondary information
    teacher = models.ForeignKey("accounts.User", related_name="courses_teacher", on_delete=models.CASCADE, verbose_name="Course Teacher") # related to one teacher
    students = models.ManyToManyField("accounts.User", blank=True, related_name="courses_student", verbose_name="Course Students") # related to many students
    description = models.TextField(null=True, blank=True, verbose_name="Course Description")
    institution = models.ForeignKey("academia.Institution", related_name="courses", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Course Institution")  # related to one institution
    subject = models.ForeignKey("academia.Subject", related_name="courses", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Course Subject")  # related to one subject
    cover = models.ImageField(upload_to="courses", null=True, blank=True, verbose_name="Course Cover")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["created_at", "updated_at", "name"]


    def __str__(self):
        return f"{self.name}, {self.teacher.first_name} {self.teacher.last_name}"

class Enrollment(models.Model):

    # Roles
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    # primary information
    student = models.ForeignKey("accounts.User", related_name="enrollments", on_delete=models.CASCADE, verbose_name="Enrollment Student")
    course_obj = models.ForeignKey("learning.Course", related_name="enrollments", on_delete=models.CASCADE, verbose_name="Enrollment Course")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending", verbose_name="Enrollment Status")

    # secondary information
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        ordering = ["student", "created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course_obj"],
                condition=Q(status="pending")|Q(status="accepted"),
                name="unique_pending_enrollment"
            ),
            # models.UniqueConstraint(
            #     fields=["student", "course_obj"],
            #     condition=Q(status="accepted"),
            #     name="unique_accepted_enrollment"
            # ),
        ]

    def clean(self):
        pass

    def __str__(self):
        return f"{self.course_obj.name}, {self.student.first_name} {self.student.last_name}"


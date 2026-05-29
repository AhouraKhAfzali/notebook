from django.db import models

# Create your models here.
class Assignment(models.Model):
    STATUS_CHOICES = (
        ('active', 'active'),
        ('inactive', 'Inactive'),
        ('closed', 'closed'),
    )
    # primary information
    title = models.CharField(max_length=255, verbose_name="Title")
    course_obj = models.ForeignKey("learning.Course", on_delete=models.CASCADE, related_name="work", verbose_name="Course")
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="work", verbose_name="Created by")
    max_score = models.PositiveIntegerField(default=20, verbose_name="Maximum Score Available")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    # secondary information
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"{self.title} ({self.course_obj})"

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"
        ordering = ['course_obj', 'created_at', 'title']


class Submission(models.Model):
    # primary information
    assignment = models.ForeignKey("work.Assignment", on_delete=models.CASCADE, related_name="submissions", verbose_name="Assignment")
    student = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="submissions", verbose_name="Student")
    text = models.TextField(max_length=1000, verbose_name="Submission Text")
    file = models.FileField(upload_to="submissions/", null=True, blank=True, verbose_name="Submission File")
    graded = models.BooleanField(default=False, verbose_name="Grading Status")
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Grade")
    feedback = models.TextField(null=True, blank=True, verbose_name="Teacher Feedback")
    # secondary information
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted at")
    graded_at = models.DateTimeField(null=True, blank=True, verbose_name="Graded at")

    def __str__(self):
        return f"{self.student}, {self.assignment}"

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"
        ordering = ['assignment', 'submitted_at']

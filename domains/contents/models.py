from django.db import models


# contents model
class Contents(models.Model):

    # primary information
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    file = models.FileField(upload_to='contents/files/', verbose_name="Media/File")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")
    edited_at = models.DateTimeField(auto_now=True, verbose_name="Edited at")
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE, verbose_name="Created by")
    course_obj = models.ForeignKey("learning.Course", on_delete=models.CASCADE, verbose_name="Course")

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"
        ordering = ["uploaded_at", "edited_at"]

    def __str__(self):
        return self.title

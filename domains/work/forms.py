from django import forms
from .models import Assignment, Submission

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'max_score', 'description')

class AssignmentEditForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'max_score', 'description', 'status')

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('text', 'file')

class SubmissionGradeForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('grade', 'feedback')

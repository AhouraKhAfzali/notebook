from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'institution', 'subject', 'cover']

    widgets = {
        'name': forms.TextInput(attrs={'placeholder': ''}),
        'description': forms.Textarea(attrs={'placeholder': ''}),
    }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'institution', 'subject', 'cover']

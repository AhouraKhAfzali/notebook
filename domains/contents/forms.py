from django import forms
from .models import Contents

class ContentsForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['title', 'description', 'file']

class ContentsEditForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['title', 'description', 'file']

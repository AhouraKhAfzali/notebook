from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# student user form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'phone_number', 'first_name', 'last_name', 'password'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


# teacher user form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email', 'phone_number', 'first_name', 'last_name', 'password'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': ''}),
            'phone_number': forms.TextInput(attrs={'placeholder': ''}),
            'first_name': forms.TextInput(attrs={'placeholder': ''}),
            'last_name': forms.TextInput(attrs={'placeholder': ''}),
            'password': forms.PasswordInput(attrs={'placeholder': ''}),
        }

# custom login form
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override placeholders
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['password'].widget.attrs['placeholder'] = ''

# password change form
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override placeholders
        self.fields['old_password'].widget.attrs['placeholder'] = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = ''

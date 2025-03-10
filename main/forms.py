from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput

from .models import Student
# - Create a User
class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Authenticate a user (Model Form)
class LoginForm(AuthenticationForm):

    
    password = forms.CharField(widget=PasswordInput())


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
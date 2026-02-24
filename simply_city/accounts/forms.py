from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    is_driver = forms.BooleanField(required=False, label="Register as Driver")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'is_driver', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
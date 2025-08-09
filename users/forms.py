from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import User, Company, Customer


class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")



class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email] ,widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password1 = forms.CharField(
    required=True, 
    widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
    help_text="Must contain at least 8 characters, including letters, numbers, and special characters."
    )    
    password2 = forms.CharField(required=True , widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    birth = forms.DateField(required=True , widget=DateInput())
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2","birth")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_Customer = True
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            Customer.objects.create(user=user , birth=self.cleaned_data["birth"])
        return user



class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email])

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            Company.objects.create(user=user)
        return user


class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def get_user(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = authenticate(email=email, password=password)
        return user
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = 'off'

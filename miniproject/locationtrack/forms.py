from django import forms
from .models import Student




class StudentForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField(min_value=18)
    nationality = forms.CharField(max_length=100)
    college = forms.CharField(max_length=100)
    college_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    location_consent = forms.BooleanField()
from django import forms
from . import models

class signUpForm(forms.ModelForm):

    class Meta:
        model = models.Signup
        fields = ["userName", "email", "password"]


class loginForm(forms.ModelForm):
    
    class Meta:
        model = models.Login
        fields = ["userName", "password"]

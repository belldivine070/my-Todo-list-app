from django.shortcuts import render
from django.views import generic
from .models import Signup, Home
from .forms import signUpForm, loginForm
from django.urls import reverse_lazy

 
from django.contrib import messages
from django.shortcuts import render
from django.views import generic
from .models import Signup, Home, Login
from .forms import signUpForm, loginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Index(generic.FormView):
    model = Signup
    form_class = signUpForm
    field = all
    template_name = "index.html"
    success_url = reverse_lazy("Login")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)
    

class Login(generic.FormView):
    model = Login
    form_class = loginForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('Home')

class Home(generic.TemplateView):
    template_name = "home.html"
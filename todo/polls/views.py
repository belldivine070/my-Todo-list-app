from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from .models import Signup, Home, Login
from .forms import signUpForm, loginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



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
    



# class Login(generic.FormView):
#     model = Login
#     form_class = loginForm
#     template_name = "login.html"

#     def get_success_url(self):
#         return reverse_lazy('Home')


# class Login(generic.FormView):
#     form_class = loginForm
#     template_name = "login.html"

#     def get_success_url(self):
#         return reverse_lazy('Home')

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(self.request, username=username, password=password)

#         if user is not None:
#             login(self.request, user)
#             return super().form_valid(form)
#         else:
#             form.add_error(None, "Invalid username or password")
#             return self.form_invalid(form)


# class Login(generic.FormView):
#     template_name = 'login.html'  # Template for rendering the form
#     form_class = loginForm  # The form class to use
#     success_url = reverse_lazy('home')  # URL to redirect to after successful login
#     field = all

#     def form_valid(self, form):
#         # Get the username and password from the form
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']

#         # Authenticate the user
#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             # Log the user in
#             login(self.request, user)
#             return super().form_valid(form)  # Redirect to success_url
#         else:
#             # Handle invalid login (e.g., show an error message)
#             form.add_error(None, "Invalid username or password")  # Add a non-field error
#             return self.form_invalid(form)  # Re-render the form with errors

# class Login(generic.FormView):
#     form_class = loginForm
#     template_name = "login.html"
#     success_url = reverse_lazy("Home")

#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, {"form" : form})
    
#     def post(self, request):
#         if request.method == "POST":
#             form = loginForm(self.form_class(data=request.POST))  # Correct way
#             if form.is_valid():
#                 userName = form.cleaned_data.get("userName")
#                 password = form.cleaned_data.get("password")

#                 user =authenticate(username = userName, password = password)

#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, f"You are logged in  as {userName}")
#                     return redirect('Home')
#                 else:
#                     messages.error(request, "Error")
#             else:
#                 messages.error(request, "Username or password incorrect")
#         form = loginForm()
#         return render(request, "home.html", {"form": userName} )


class Login(generic.View):
    form_class = loginForm
    template_name = "login.html"
    success_url = "Home"  # Name of the URL to redirect to after login

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)  # Correct initialization
        if form.is_valid():
            username = form.cleaned_data.get("username")  # Ensure field name matches
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in as {username}")
                return redirect(self.success_url)
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Username or password incorrect")

        # If the form is invalid or authentication fails, re-render the form
        return render(request, self.template_name, {"form": form})

    

class Home(generic.TemplateView):
    template_name = "home.html"
from django.contrib import admin
from .models import Signup
from .forms import signUpForm


# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    form = signUpForm  # Use your custom form here
    list_display = ('userName', 'email', 'password', 'created_at')  # Columns to show in the admin list view

# Register the model and admin class
admin.site.register(Signup, MyModelAdmin)

from django.urls import  path
from .import views


urlpatterns = [
    path("", views.Index.as_view(), name="Index"),
    path("Login/", views.Login.as_view(), name="Login"),
    path("Home/", views.Home.as_view(), name="Home")
]

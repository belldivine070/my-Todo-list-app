from django.db import models

# Create your models here.
class Signup(models.Model):
    userName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.userName} {self.email} {self.created_at}"
    

class Login(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Home(models.Model):
    details = models.ForeignKey(to=Login, on_delete=models.CASCADE)
    
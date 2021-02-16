from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.IntegerField(default='123', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
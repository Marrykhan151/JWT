from django.db import models

# Create your models here.


class Employee(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Student(AbstractUser):
    courses_cleared = models.CharField(max_length=255, blank=True)
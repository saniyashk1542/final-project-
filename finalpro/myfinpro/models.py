# Create your models here.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def _str_(self):
        return f"{self.first_name} {self.last_name}"
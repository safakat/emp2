import employe
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class EmployeeList(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_no = models.CharField(max_length=10,null=False,blank=False)
    employee_name = models.CharField(max_length=100,null=False,blank=False)
    employee_age = models.IntegerField()

    def __str__(self):
        return str(self.employee_name)
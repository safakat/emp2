from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from employe.models import EmployeeList

# Register your models here.

admin.site.register(EmployeeList)
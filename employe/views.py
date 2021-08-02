from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from employe.models import EmployeeList
from employe.serializers import EmployeeSerializer

# Create your views here.


class Employees(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EmployeeList.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployee(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EmployeeList.objects.all()
    serializer_class = EmployeeSerializer

class UpdateEmployee(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EmployeeList.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployee(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EmployeeList.objects.all()
    serializer_class = EmployeeSerializer
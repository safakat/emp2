from rest_framework.serializers import ModelSerializer
from employe.models import EmployeeList

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeList
        # fields = ('employee_no','employee_name','employee_age')
        fields = "__all__"
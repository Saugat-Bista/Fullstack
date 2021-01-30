from rest_framework import serializers
from .models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('department_id', 'department_name', 'department_created')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('employee_id', 'employee_name', 'employee_department', 'date_joined', 'employee_photo')

from django.db import models

class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    department_created = models.DateField(auto_now_add=True)
    
class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_department = models.CharField(max_length=100)
    date_joined = models.DateField()
    employee_photo = models.CharField(max_length=100)

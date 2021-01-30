from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departmentList(request):
    queryset = Departments.objects.all()
    if queryset:
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('No Departments Found!!', status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departmentDetail(request, id):
    queryset = Departments.objects.get(department_id=id)
    serializer = DepartmentSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def departmentCreate(request): 
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response('Could Not Create Department!!', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def departmentUpdate(request, id): 
    queryset = Departments.objects.get(department_id=id)
    serializer = DepartmentSerializer(instance=queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('Could Not Update Department!!', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def departmentDelete(request, id):
    queryset = Departments.objects.get(department_id=id)
    queryset.delete()
    return Response('Department Deleted!!', status=status.HTTP_200_OK)

@api_view(['GET'])
def employeeList(request):
    queryset = Employees.objects.all()
    if queryset:
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('No Employees Found!!', status=status.HTTP_204_NO_CONTENT)  

@api_view(['GET'])
def employeeDetail(request, id):
    queryset = Employees.objects.get(employee_id=id)
    serializer = EmployeeSerializer(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def employeeCreate(request): 
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response('Could Not Create Employee!!', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def employeeUpdate(request, id): 
    queryset = Employees.objects.get(employee_id=id)
    serializer = EmployeeSerializer(instance=queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response('Could Not Update Employee!!', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def employeeDelete(request, id):
    queryset = Employees.objects.get(employee_id=id)
    queryset.delete()
    return Response('Employee Deleted!!', status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def saveImage(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return Response(file_name, status=status.HTTP_200_OK)
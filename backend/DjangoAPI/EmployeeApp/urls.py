from django.contrib import admin
from django.urls import path

from .views import departmentList, departmentDetail, departmentCreate, departmentUpdate, departmentDelete
from .views import employeeList, employeeDetail, employeeCreate, employeeUpdate, employeeDelete
from .views import saveImage

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('department-list/', departmentList),
    path('department-details/<int:id>/', departmentDetail),
    path('department-create/', departmentCreate),
    path('department-update/<int:id>', departmentUpdate),
    path('department-delete/<int:id>/', departmentDelete),
    
    path('employee-list/', employeeList),
    path('employee-details/<int:id>/', employeeDetail),
    path('employee-create/', employeeCreate),
    path('employee-update/<int:id>/', employeeUpdate),
    path('employee-delete/<int:id>/', employeeDelete),

    path('save-image/', saveImage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
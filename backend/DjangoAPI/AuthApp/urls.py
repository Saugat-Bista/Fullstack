from django.urls import path, include
from DjangoAPI.views import time

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]
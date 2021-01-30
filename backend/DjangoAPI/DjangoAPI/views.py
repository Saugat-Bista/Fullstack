from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def time(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return Response("Current time is: " + date, status=status.HTTP_200_OK)
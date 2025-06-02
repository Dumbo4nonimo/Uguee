from django.shortcuts import render

def welcome(request):
    return render(request, 'api/welcome.html')

#Token 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({
        "mensaje": f"Hola, {request.user.username}. Has accedido a una vista protegida con JWT."
    })

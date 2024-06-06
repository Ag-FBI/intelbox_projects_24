from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from.serializers import InfoSerializer
from .models import Info
from rest_framework.response import Response

@api_view(['POST', 'GET'])
def info(request):
    if request.method == 'POST':
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data=data, status=status.HTTP_201_CREATED, template_name="plate_reader/process_frame.html")
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        instances = Info.objects.all()
        serializer = InfoSerializer(instances, many=True)
        return Response(serializer.data)


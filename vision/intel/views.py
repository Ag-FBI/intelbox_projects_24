from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonInfoSerializer
from .models import PersonInfo
from rest_framework.response import Response



@api_view(["GET", "POST"])
def test_response(request, pk=None):
    if request.method == "GET":
        if pk is not None:
                instance = get_object_or_404(PersonInfo, pk=pk)
                serializer = PersonInfoSerializer(instance)
                return Response(serializer.data)
        instance = PersonInfo.objects.all()
        serializer = PersonInfoSerializer(instance, many=True)
        return Response(serializer.data)

        
    if request.method == "POST":
            data = request.data
            serializer = PersonInfoSerializer(data)
            return Response(serializer.data)

